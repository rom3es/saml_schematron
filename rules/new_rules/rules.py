import xmltodict
from collections import OrderedDict


class InputData():
    def __init__(self, xml_file):
        with open(xml_file) as fd:
            self._doc = xmltodict.parse(fd.read())

    def get_element(self, name, root=None):
        if root is None:
            root = self._doc

        for element_name in root:
            if element_name == name:
                return root[element_name]

            if isinstance(root[element_name], OrderedDict):
                result = self.get_element(name, root[element_name])

                if result is not None:
                    return result

        return None


def rule02(data):
    try:
        assert data.get_element('md:NameIDFormat') in ['urn:oasis:names:tc:SAML:2.0:nameid-format:persistent', 'urn:oasis:names:tc:SAML:2.0:nameid-format:transient', '']
    except AssertionError:
        return 'This NameIDFormat may not be supported. Supported values for NameIDFormat are:\n    urn:oasis:names:tc:SAML:2.0:nameid-format:persistent\n    urn:oasis:names:tc:SAML:2.0:nameid-format:transient'

    return 'ok'


def rule01(data):
    def starts_with(data, pattern):
        for p in pattern:
            if data.startswith(p):
                return True

        return False

    try:
        assert starts_with(data.get_element('md:EntityDescriptor')['@entityID'], ['urn:', 'http://', 'https://'])
    except AssertionError:
        return '@entityID values should be a URI starting with http://, https:// or urn:'

    return 'ok'


def starts_with(data, pattern, message):
    if not isinstance(pattern, list):
        pattern = [pattern]

    for p in pattern:
        if data.startswith(p):
            return 'ok'

    return message


print(rule01(InputData('../../testdata/rule01W_OK_1.xml')))
print(rule02(InputData('../../testdata/rule02W_fail.xml')))

print(starts_with(
    InputData('../../testdata/rule02W_fail.xml').get_element('md:EntityDescriptor')['@entityID'],
    ['urn:', 'http://', 'https://'],
    '@entityID values should be a URI starting with http://, https:// or urn:'
))

