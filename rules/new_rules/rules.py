import xmltodict
import re
from collections import OrderedDict


class InputData():
    def __init__(self, data):
        self._doc = data

    def get_element(self, name, root=None):
        if root is None:
            root = self._doc

        if not isinstance(root, OrderedDict):
            return InputData(None)

        for element_name in root:
            raw_element_name = re.sub(r'^\w+:([\s\S]+)', r'\1', element_name)

            if raw_element_name == name:
                return InputData(root[element_name])

            if isinstance(root[element_name], OrderedDict):
                result = self.get_element(name, root[element_name])

                if len(result) != 0:
                    return result

        return InputData(OrderedDict())

    def __getitem__(self, index):
        if not isinstance(self._doc, list):
            return self._doc[index]
        else:
            for i in self._doc:
                try:
                    return i[index]
                except KeyError:
                    continue

            return None

    def __len__(self):
        return len(self._doc)

    def __str__(self):
        return str(self._doc)

    def __iter__(self):
        return self._doc.__iter__()


def starts_with(data, pattern, message):
    for p in pattern:
        if data.startswith(p):
            return 'ok'

    return message


def in_range(data, pattern, message):
    if len(data) == 0:
        return message

    for d in data:
        if str(d) not in pattern:
            return message

    return 'ok'


# def not_in_range(data, pattern, message):
#     for d in data:
#         if str(d) in pattern:
#             return message
#
#     return 'ok'


def not_empty(data, message):
    if len(data) == 0:
        return message

    for d in data:
        if len(d) == 0:
            return message

    return 'ok'


def get_data(path):
    with open(path) as fd:
        return InputData(xmltodict.parse(fd.read()))



print(get_data('../../testdata/rule03W_idp_fail.xml').get_element('EntityDescriptor').get_element('ContactPerson')['@contactType'])


exit()

print(starts_with(
    get_data('../../testdata/rule01W_OK_1.xml').get_element('EntityDescriptor')['@entityID'],
    ['urn:', 'http://', 'https://'],
    '@entityID values should be a URI starting with http://, https:// or urn:'
))


print(in_range(
    get_data('../../testdata/rule02W_OK.xml').get_element('NameIDFormat'),
    [
        'urn:oasis:names:tc:SAML:2.0:nameid-format:persistent',
        'urn:oasis:names:tc:SAML:2.0:nameid-format:transient',
        ''
    ],
    'This NameIDFormat may not be supported. Supported values for NameIDFormat are:\n    urn:oasis:names:tc:SAML:2.0:nameid-format:persistent\n    urn:oasis:names:tc:SAML:2.0:nameid-format:transient'
))


print(not_empty(
    get_data('../../testdata/rule03W_idp_fail.xml').get_element('IDPSSODescriptor').get_element('NameIDFormat'),
    'Each IDPSSODescriptor should contain NameIDFormat with one or more values'
))


print(not_empty(
    get_data('../../testdata/rule03W_idp_fail.xml').get_element('SPSSODescriptor').get_element('NameIDFormat'),
    'Each SPSSODescriptor should contain NameIDFormat with one or more values'
))

print(not_empty(
    get_data('../../testdata/rule03W_idp_fail.xml').get_element('EntityDescriptor'),
    'EntityDescriptor should contain an Organization'
))

print(in_range(
    get_data('../../testdata/rule03W_idp_fail.xml').get_element('EntityDescriptor').get_element('ContactPerson')['@contactType'],
    ['support'],
    'EntityDescriptor should contain an Organization'
))
