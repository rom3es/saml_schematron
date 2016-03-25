<?xml version="1.0" standalone="yes"?>


<!--PATTERN single sign on-->



	<!--RULE -->

<axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" xmlns:sch="http://www.ascc.net/xml/schematron" xmlns:iso="http://purl.oclc.org/dsdl/schematron" xmlns:xalan="http://xml.apache.org/xalan" match="//md:IDPSSODescriptor" priority="1001" mode="M0">

		<!--ASSERT -->
<axsl:choose><axsl:when test="md:SingleSignOnService"/><axsl:otherwise><axsl:message>
Error (44): IDPSSODescriptor does not contain a SingleSignOnService“
     XPATH: <axsl:call-template name="xpathgetter"/> validation rule: (md:SingleSignOnService)</axsl:message></axsl:otherwise></axsl:choose><axsl:apply-templates select="*|comment()|processing-instruction()" mode="M0"/></axsl:template>

	<!--RULE -->

<axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" xmlns:sch="http://www.ascc.net/xml/schematron" xmlns:iso="http://purl.oclc.org/dsdl/schematron" xmlns:xalan="http://xml.apache.org/xalan" match="//md:IDPSSODescriptor" priority="1000" mode="M0">

		<!--ASSERT -->
<axsl:choose><axsl:when test="md:SingleSignOnService[normalize-space(@Binding)='urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST']"/><axsl:otherwise><axsl:message>
Error (44): IDPSSODescriptor must contain a SingleSignOnService with Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST“
     XPATH: <axsl:call-template name="xpathgetter"/> validation rule: (md:SingleSignOnService[normalize-space(@Binding)='urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'])</axsl:message></axsl:otherwise></axsl:choose><axsl:apply-templates select="*|comment()|processing-instruction()" mode="M0"/></axsl:template><axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" match="text()" priority="-1" mode="M0"/><axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" match="@*|node()" priority="-2" mode="M0">
  <axsl:apply-templates select="*|comment()|processing-instruction()" mode="M0"/>
</axsl:template>
