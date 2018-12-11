RULES = {
    'rule01W': {
        'context': "md:EntityDescriptor",
        'test_rule': '''
            normalize-space(text()) = 'urn:oasis:names:tc:SAML:2.0:nameid-format:persistent' 
            or normalize-space(text()) = 'urn:oasis:names:tc:SAML:2.0:nameid-format:transient'
            or normalize-space(text()) = ''
        ''',
        'message': "@entityID values should be a URI starting with http://, https:// or urn:"
    },

    'rule02W': {
        'context': "md:NameIDFormat",
        'test_rule': "starts-with(@entityID,'https://') or starts-with(@entityID,'http://') or starts-with(@entityID,'urn:')",
        'message': '''
            This NameIDFormat may not be supported. Supported values for NameIDFormat are:
                urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
                urn:oasis:names:tc:SAML:2.0:nameid-format:transient
        '''
    },

    'rule03W': {
        'context': "//md:IDPSSODescriptor",
        'test_rule': "md:NameIDFormat[text() != '']",
        'message': "Each IDPSSODescriptor should contain NameIDFormat with one or more values",
    },

    'rule23E': {
        'context': "alg:DigestMethod",
        'test_rule': '''
            normalize-space(@Algorithm)='http://www.w3.org/2001/04/xmlenc#sha256'
            or normalize-space(@alg:Algorithm)='http://www.w3.org/2001/04/xmlenc#sha256'
            or normalize-space(@Algorithm)='http://www.w3.org/2000/09/xmldsig#sha1'
            or normalize-space(@alg:Algorithm)='http://www.w3.org/2000/09/xmldsig#sha1'
            or normalize-space(@Algorithm)='http://www.w3.org/2001/04/xmlenc#sha512'
            or normalize-space(@alg:Algorithm)='http://www.w3.org/2001/04/xmlenc#sha512'
            or normalize-space(@Algorithm)='http://www.w3.org/2001/04/xmlenc#ripemd160'
            or normalize-space(@alg:Algorithm)='http://www.w3.org/2001/04/xmlenc#ripemd160'
        ''',
        'message': '''
            alg:DigestMethod element may only contain following @Algorithm values:
                http://www.w3.org/2000/09/xmldsig#sha1
                http://www.w3.org/2001/04/xmlenc#sha256
                http://www.w3.org/2001/04/xmlenc#sha512
                http://www.w3.org/2001/04/xmlenc#ripemd160
        ''',
        'severity': "Error"
    },
}


def get_rule(id, context, test_rule, message, severity='Warning'):
    template = '''
<?xml version="1.0" encoding="utf-8"?>
<iso:pattern id="{id}" xmlns:iso="http://purl.oclc.org/dsdl/schematron" >
  <iso:rule context="{context}">
    <iso:assert test="{test_rule}">
"{id}": {{ "Severity": "{severity}",
         "Message": "{message}",
    </iso:assert>
  </iso:rule>
</iso:pattern>
'''

    return template.format_map(locals())


if __name__ == "__main__":
    for id in RULES:
        print(get_rule(id, **RULES[id]))
