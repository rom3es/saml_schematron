from helpers import *

print(starts_with(
    get_data('../../testdata/rule01W_OK_1.xml').get_element('EntityDescriptor')['@entityID'],
    ['urn:', 'http://', 'https://'],
    '@entityID values should be a URI starting with http://, https:// or urn:'
))


print(in_range(
    get_data('../../testdata/rule02W_fail.xml').get_element('NameIDFormat'),
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


print(contain(
    get_data('../../testdata/rule03W_idp_fail.xml').get_element('EntityDescriptor').get_element('ContactPerson'),
    '@contactType',
    'support',
    'EmailAddress',
    'EntityDescriptor should contain ContactPerson with a contactType of "support" and at least one EmailAddress'
))


print(contain(
    get_data('../../testdata/rule03W_idp_fail.xml').get_element('EntityDescriptor').get_element('ContactPerson'),
    '@contactType',
    'technical',
    'EmailAddress',
    'EntityDescriptor should contain ContactPerson with a contactType of "technical" and at least one EmailAddress'
))


print(in_range(
    get_data('../../testdata/rule02W_fail.xml').get_element('IDPSSODescriptor').get_element('SingleSignOnService')['Binding'],
    [
        'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'
    ],
    'IDPSSODescriptor must contain a SingleSignOnService with Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"'
))

print(in_range(
    get_data('../../testdata/rule02W_fail.xml').get_element('SPSSODescriptor').get_element('AssertionConsumerService')['Binding'],
    [
        'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'
    ],
    'SPSSODescriptor should contain an AssertionConsumerService with Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"'
))