import argparse
import logging, os, re, sys
import lxml.etree as etree
from lxml.isoschematron import Schematron
import abstract_invocation

class CliParser(abstract_invocation.AbstractInvocation):
    """ define CLI invocation for validate.  Test runner can use this by passing testargs """
    def __init__(self, testargs=None):
        self._parser = argparse.ArgumentParser(description='SAML metadata validation')
        self._parser.add_argument('-r', '--ruledir', dest='ruledir',
            help='directory to find rule xsl file')
        self._parser.add_argument('-p', '--profile', dest='profile',
            help='profile defining a set of rules')
        self._parser.add_argument('-v', '--verbose', dest='verbose', action="store_true")
        self._parser.add_argument('metadatafile', type=argparse.FileType('r'),
            help='metadata file name')
        self._parser.add_argument('rule', nargs='*',
            help='rule name (schematron file name, without extension')

        if (testargs):
            self.args = self._parser.parse_args(testargs)
        else:
            self.args = self._parser.parse_args()  # regular case: use sys.argv

class ValidatorResult:
    def __init__(self):
        pass


class Validator:
    """
    Validate SAML Metadata according to a specified set of Schematron rules
    """
    def __init__(self, invocation):
        self.args = invocation.args
        self.projdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        if self.args.verbose:
            print('self.projdir = ' + self.projdir)
            print('metadatafile = ' + self.args.metadatafile.name)
            print('rules: ' + ', '.join(self.args.rule))
        if getattr(self.args, 'ruledir', None):
            self.schtrondir = self.args.ruledir
        else:
            self.schtrondir = os.path.join(self.projdir, 'rules', 'schtron_exp')

    def validate(self) -> ValidatorResult:
        md_dom = etree.parse(self.args.metadatafile.name)
        for e in md_dom.findall('{urn:oasis:names:tc:SAML:2.0:metadata}EntitiesDescriptor'):
            if self.args.verbose: print('entityID: ' + e.attrib['entityID'])
        schtron_dom = etree.parse(os.path.join(self.schtrondir, self.args.rule[0] + '_exp.sch'))
        schtron_val = Schematron(schtron_dom, error_finder=Schematron.ASSERTS_AND_REPORTS)
        validator_result = ValidatorResult()
        result = schtron_val.validate(md_dom)
        if result:
            validator_result.level = 'OK'
            validator_result.message_one_line = ''
            validator_result.message_formatted = ''
        else:
            m_dom = etree.XML(schtron_val.error_log.last_error.message)
            validator_result.level = schtron_val.error_log.last_error.level_name
            validator_result.message_formatted = m_dom.find('{http://purl.oclc.org/dsdl/svrl}text').text
            validator_result.message_one_line = re.sub(r'\s+', ' ', validator_result.message_formatted)
        return validator_result


def run_me(testrunnerInvocation=None):
    if testrunnerInvocation:
        # CLI args and logger set by unit test
        invocation = testrunnerInvocation
    else:
        invocation = CliParser()
    validator = Validator(invocation)
    return validator.validate()


if __name__ == '__main__':
    if sys.version_info < (3, 4):
        raise "must use python 3.4 or higher"
    val_result = run_me()
    print(val_result.level)
    print(val_result.message_formatted)
    print(val_result.message_one_line)
