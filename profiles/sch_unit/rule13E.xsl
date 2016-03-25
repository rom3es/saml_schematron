<?xml version="1.0" standalone="yes"?>


<!--PATTERN Rule 13-->



	<!--RULE -->

<axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" xmlns:sch="http://www.ascc.net/xml/schematron" xmlns:iso="http://purl.oclc.org/dsdl/schematron" xmlns:xalan="http://xml.apache.org/xalan" match="//md:IDPSSODescriptor" priority="1001" mode="M0">

		<!--ASSERT -->
<axsl:choose><axsl:when test="descendant::alg:SigningMethod"/><axsl:otherwise><axsl:message>
Error (13): IDPSSODescriptor must contain SigningMethod
     XPATH: <axsl:call-template name="xpathgetter"/> validation rule: (descendant::alg:SigningMethod)</axsl:message></axsl:otherwise></axsl:choose><axsl:apply-templates select="*|comment()|processing-instruction()" mode="M0"/></axsl:template>

	<!--RULE -->

<axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" xmlns:sch="http://www.ascc.net/xml/schematron" xmlns:iso="http://purl.oclc.org/dsdl/schematron" xmlns:xalan="http://xml.apache.org/xalan" match="//md:SPSSODescriptor" priority="1000" mode="M0">

		<!--ASSERT -->
<axsl:choose><axsl:when test="descendant::alg:SigningMethod"/><axsl:otherwise><axsl:message>
Error (13): SPSSODescriptor must contain SigningMethod
     XPATH: <axsl:call-template name="xpathgetter"/> validation rule: (descendant::alg:SigningMethod)</axsl:message></axsl:otherwise></axsl:choose><axsl:apply-templates select="*|comment()|processing-instruction()" mode="M0"/></axsl:template><axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" match="text()" priority="-1" mode="M0"/><axsl:template xmlns:axsl="http://www.w3.org/1999/XSL/Transform" match="@*|node()" priority="-2" mode="M0">
  <axsl:apply-templates select="*|comment()|processing-instruction()" mode="M0"/>
</axsl:template>
