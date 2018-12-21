from .helpers import get_data


def rule_01(data):
    """
    @entityID values should be a URI starting with http://, https:// or urn:
    """
    pattern =['urn:', 'http://', 'https://']
    value = data.get_element('EntityDescriptor')['@entityID']

    for p in pattern:
        if value.startswith(p):
            return True

    return False


def rule_02(data):
    """
    This NameIDFormat may not be supported. Supported values for NameIDFormat are:
        urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
        urn:oasis:names:tc:SAML:2.0:nameid-format:transient
    """
    pattern = [
        'urn:oasis:names:tc:SAML:2.0:nameid-format:persistent',
        'urn:oasis:names:tc:SAML:2.0:nameid-format:transient',
        ''
    ]
    value = data.get_element('NameIDFormat')

    if len(value) == 0:
        return False

    for v in value:
        if str(v) not in pattern:
            return False

    return True


def rule_03(data):
    """
    Each IDPSSODescriptor should contain NameIDFormat with one or more values
    """
    value = data.get_element('IDPSSODescriptor').get_element('NameIDFormat')

    return not(len(value) == 0)


def rule_04(data):
    """
    Each SPSSODescriptor should contain NameIDFormat with one or more values
    """
    value = data.get_element('SPSSODescriptor').get_element('NameIDFormat')

    return not(len(value) == 0)


def rule_05(data):
    """
    EntityDescriptor should contain an Organization
    """
    value = data.get_element('EntityDescriptor').get_element('Organization')

    return not(len(value) == 0)


def rule_06(data):
    """
    EntityDescriptor should contain ContactPerson with a contactType of \"support\" and at least one EmailAddress
    """
    value = data.get_element('EntityDescriptor').get_element('ContactPerson')

    for v in value:
        if v['@contactType'] == 'support' and 'md:EmailAddress' in v.keys():
            return True

    return False


def rule_07(data):
    """
    EntityDescriptor should contain ContactPerson with a contactType of \"technical\" and at least one EmailAddress
    """
    value = data.get_element('EntityDescriptor').get_element('ContactPerson')

    for v in value:
        if v['@contactType'] == 'technical' and 'md:EmailAddress' in v.keys():
            return True

    return False


def rule_09(data):
    """
    IDPSSODescriptor must contain a SingleSignOnService with Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\"
    """
    return data.get_element('IDPSSODescriptor').get_element('SingleSignOnService')['@Binding'] == 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'


def rule_10(data):
    """
    IDPSSODescriptor contains saml2:Attribute elements; but some implementations may not understand this.
    """
    return len(data.get_element('IDPSSODescriptor').get_element('saml:Attribute', ignore_namespaces=False) == 0)


def rule_11(data):
    """
    SPSSODescriptor should contain an AssertionConsumerService with Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\"
    """
    for d in data.get_element('SPSSODescriptor').get_element('AssertionConsumerService', as_list=True):
        if d['@Binding'] == 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST':
            return True

    return False


def rule_12(data):
    """
    Message": "IDPSSODescriptor/SPSSODescriptor must contain alg:DigestMethod
    """
    return \
        len(data.get_element('IDPSSODescriptor').get_element('alg:DigestMethod', ignore_namespaces=False)) > 0 or \
        len(data.get_element('SPSSODescriptor').get_element('alg:DigestMethod', ignore_namespaces=False)) > 0


def rule_13(data):
    """
    IDPSSODescriptor/SPSSODescriptor must contain SigningMethod
    """
    return \
        len(data.get_element('IDPSSODescriptor').get_element('alg:SigningMethod', ignore_namespaces=False)) > 0 or \
        len(data.get_element('SPSSODescriptor').get_element('alg:SigningMethod', ignore_namespaces=False)) > 0


def rule_14(data):
    """
    IDPSSODescriptor should contain discovery hints
    """
    return len(data.get_element('IDPSSODescriptor').get_element('Extensions').get_element('DiscoHints')) > 0


def rule_15(data):
    """
    IDPSSODescriptor/SPSSODescriptor should contain SingleLogoutService
    """
    return \
        len(data.get_element('IDPSSODescriptor').get_element('SingleLogoutService')) > 0 or \
        len(data.get_element('SPSSODescriptor').get_element('SingleLogoutService')) > 0


def rule_16(data):
    """
    AttributeConsumingService is deprecated if EntityCategory has an fixed set of RequestedAttributes.
    """
    value = data.get_element('EntityDescriptor')

    return len(value.get_element('SPSSODescriptor').get_element('AttributeConsumingService')) > 0 and \
        value.get_element('AttributeValue') in ['http://www.ref.gv.at/ns/names/agiz/pvp/egovtoken', 'http://www.ref.gv.at/ns/names/agiz/pvp/egovtoken-charge']


def rule_17(data):
    """
    SPSSODescriptor should include Extensions/DiscoveryResponse
    """
    return len(data.get_element('SPSSODescriptor').get_element('Extensions').get_element('DiscoveryResponse')) > 0


def rule_18(data):
    """
    EntityAttributes containing an EntityCategory need to be direct descendants of EntityDescriptor
    TODO: implement
    """
    pass


def rule_19(data):
    """
    EntityCategories should be restricted to these values:\n  http://www.ref.gv.at/ns/names/agiz/pvp/egovtoken,\n  http://www.ref.gv.at/ns/names/agiz/pvp/egovtoken-charge
    """
    value = data.get_element('EntityDescriptor').get_element('Extensions').get_element('EntityAttributes').get_element('Attribute').get_element('AttributeValue', as_list=True)

    for v in value:
        if v not in ['http://www.ref.gv.at/ns/names/agiz/pvp/egovtoken', 'http://www.ref.gv.at/ns/names/agiz/pvp/egovtoken-charge']:
            return False

    return True


def rule_20(data):
    """
    SPSSODescriptor should include init:RequestInitiator
    """
    return len(data.get_element('SPSSODescriptor').get_element('Extensions').get_element('RequestInitiator')) > 0


def rule_21(data):
    """
    SPSSODescriptor should include a mdui:UIInfo element
    """
    return len(data.get_element('SPSSODescriptor').get_element('Extensions').get_element('UIInfo')) > 0


def rule_22(data):
    """
    UIInfo must include a non-empty DisplayName
    """
    try:
        for d in data.get_element('UIInfo').get_element('DisplayName', as_list=True):
            if not len(d['#text']):
                return False

        return True
    except KeyError:
        return False


def rule_23(data):
    """
    alg:DigestMethod element may only contain following @Algorithm values:
        http://www.w3.org/2000/09/xmldsig#sha1
        http://www.w3.org/2001/04/xmlenc#sha256
        http://www.w3.org/2001/04/xmlenc#sha512
        http://www.w3.org/2001/04/xmlenc#ripemd160
    """
    pattern = [
        'http://www.w3.org/2001/04/xmlenc#sha256',
        'http://www.w3.org/2000/09/xmldsig#sha1',
        'http://www.w3.org/2001/04/xmlenc#sha512',
        'http://www.w3.org/2001/04/xmlenc#ripemd160',
    ]

    return data.get_element('DigestMethod')['@Algorithm'] in pattern


def rule_24(data):
    """
    Each alg:SigningMethod may only contain following @Algorithm values: \
        http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
        http://www.w3.org/2000/09/xmldsig#rsa-sha1
        http://www.w3.org/2001/04/xmldsig-more#rsa-sha384
        http://www.w3.org/2001/04/xmldsig-more#rsa-sha512
        http://www.w3.org/2001/04/xmldsig-more#rsa-ripemd160
        http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256
        http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384
        http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512
    """
    pattern = [
        'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
        'http://www.w3.org/2000/09/xmldsig#rsa-sha1',
        'http://www.w3.org/2001/04/xmldsig-more#rsa-sha384',
        'http://www.w3.org/2001/04/xmldsig-more#rsa-sha512',
        'http://www.w3.org/2001/04/xmldsig-more#rsa-ripemd160',
        'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256',
        'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384',
        'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512',
    ]

    for d in data.get_element('SigningMethod', as_list=True):
        if d['@Algorithm'] not in pattern:
            return False

    return True


def rule_25(data):
    """
    DigestMethod element should not contain @Algorithm value http://www.w3.org/2000/09/xmldsig#sha1
    """
    for d in data.get_element('DigestMethod', as_list=True):
        if d['@Algorithm'] == 'http://www.w3.org/2000/09/xmldsig#sha1':
            return False

    return True


def rule_26(data):
    """
    SigningMethod element should not contain @Algorithm value http://www.w3.org/2000/09/xmldsig#rsa-sha1
    """
    for d in data.get_element('SigningMethod', as_list=True):
        if d['@Algorithm'] == 'http://www.w3.org/2000/09/xmldsig#rsa-sha1':
            return False

    return True


def rule_27(data):
    """
    MinKeySize must be greater or equal to 2048 if Algorithm starts with http://www.w3.org/2001/04/xmldsig-more#rsa
    """
    for d in data.get_element('SigningMethod', as_list=True):
        if d['@Algorithm'].startswith('http://www.w3.org/2001/04/xmldsig-more#rsa') and int(d['@MinKeySize']) < 2048:
            return False

    return True


def rule_28(data):
    """
    MinKeySize must be greater or equal to 256 if Algorithm starts with http://www.w3.org/2001/04/xmldsig-more#ecdsa
    """
    for d in data.get_element('SigningMethod', as_list=True):
        if d['@Algorithm'].startswith('http://www.w3.org/2001/04/xmldsig-more#ecdsa') and int(d['@MinKeySize']) < 256:
            return False

    return True


def rule_29(data):
    """
    alg:SigningMethod must have an attribute MaxKeySize
    """
    for d in data.get_element('SigningMethod', as_list=True):
        if '@MaxKeySize' not in d.keys():
            return False

    return True


def rule_30(data):
    """
    AssertionConsumerService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact is deprecated\"
    """
    for d in data.get_element('AssertionConsumerService', as_list=True):
        if d['@Binding'] == 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact':
            return False

    return True


def rule_31(data):
    """
    @entityID length should not exceed 80 characters
    """
    return len(data.get_element('EntityDescriptor')['@entityID']) <= 80


def rule_32(data):
    """
    IDPSSODescriptor  must contain a mdui:UIInfo element
    """
    return len(data.get_element('IDPSSODescriptor').get_element('Extensions').get_element('UIInfo')) > 0


def rule_33(data):
    """
    IDPSSODescriptor/SPSSODescriptor should contain alg:DigestMethod
    """
    return len(data.get_element('IDPSSODescriptor').get_element('Extensions').get_element('DigestMethod')) > 0 or \
        len(data.get_element('SPSSODescriptor').get_element('Extensions').get_element('DigestMethod')) > 0


def rule_34(data):
    """
    IDPSSODescriptor/SPSSODescriptor should contain alg:SigningMethod
    """
    return len(data.get_element('IDPSSODescriptor').get_element('Extensions').get_element('SigningMethod')) > 0 or \
        len(data.get_element('SPSSODescriptor').get_element('Extensions').get_element('SigningMethod')) > 0


def rule_35(data):
    """
    protocolSupportEnumeration should contain only \"urn:oasis:names:tc:SAML:2.0:protocol\" (-> remove support for legacy protocols)
    """
    return data.get_element('IDPSSODescriptor')['@protocolSupportEnumeration'] == 'urn:oasis:names:tc:SAML:2.0:protocol'


def rule_36(data):
    """
    IDPSSODescriptor must contain a SingleSignOnService with Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\"
    """
    for d in data.get_element('IDPSSODescriptor').get_element('SingleSignOnService', as_list=True):
        if d['@Binding'] == 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST':
            return True

    return False


def rule_37(data):
    """
    Each IDPSSODescriptor/SPSSODescriptor must contain at least one KeyDescriptor with a use=\"signing\" attribute
    """
    for d in [data.get_element('IDPSSODescriptor').get_element('KeyDescriptor'), data.get_element('SPSSODescriptor').get_element('KeyDescriptor')]:
        try:
            if d['@use'] == 'signing':
                return True
        except KeyError:
            continue

    return False


def rule_38(data):
    """
    Each alg:SigningMethod may only contain following @Algorithm values:\
        http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
        http://www.w3.org/2001/04/xmldsig-more#rsa-sha512
        http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256
        http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512
    """
    pattern = [
        'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256',
        'http://www.w3.org/2001/04/xmldsig-more#rsa-sha512',
        'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256',
        'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512',
    ]

    for d in data.get_element('SigningMethod', as_list=True):
        if d['@Algorithm'] not in pattern:
            return False

    return True


def rule_39(data):
    """
    alg:DigestMethod element may only contain following @Algorithm values:
        http://www.w3.org/2001/04/xmlenc#sha256
        http://www.w3.org/2001/04/xmlenc#sha512
        http://www.w3.org/2001/04/xmlenc#ripemd160
    """
    pattern = [
        'http://www.w3.org/2001/04/xmlenc#sha256',
        'http://www.w3.org/2001/04/xmlenc#sha512',
        'http://www.w3.org/2001/04/xmlenc#ripemd160',
    ]

    for d in data.get_element('DigestMethod', as_list=True):
        if d['@Algorithm'] not in pattern:
            return False

    return True


def rule_40(data):
    """
    md:EncryptionMethod element may only contain following  values:
        http://www.w3.org/2001/04/xmlenc#aes128-cbc
        http://www.w3.org/2001/04/xmlenc#aes256-cbc
        http://www.w3.org/2009/xmlenc11#aes128-gcm
        http://www.w3.org/2009/xmlenc11#aes256-gcm
        http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p
        http://www.w3.org/2009/xmlenc11#ECDH-ES
    """
    pattern = [
        'http://www.w3.org/2001/04/xmlenc#aes128-cbc',
        'http://www.w3.org/2001/04/xmlenc#aes256-cbc',
        'http://www.w3.org/2009/xmlenc11#aes128-gcm',
        'http://www.w3.org/2009/xmlenc11#aes256-gcm',
        'http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p',
        'http://www.w3.org/2009/xmlenc11#ECDH-ES',
    ]

    for d in data.get_element('EncryptionMethod', as_list=True):
        try:
            if d['@Algorithm'] not in pattern:
                return False
        except TypeError:
            return False

    return True
