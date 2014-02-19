<?xml version="1.0" encoding="utf-8"?>
<iso:pattern id="Rule 3"  xmlns:iso="http://purl.oclc.org/dsdl/schematron" >
   <iso:rule context="//md:IDPSSODescriptor">                                  
      <iso:assert 
         test="md:NameIDFormat[text() != '']">
Warning (03): Each IDPSSODescriptor should contain NameIDFormatwith one or more values  
      </iso:assert>   
   </iso:rule>
        
   <iso:rule context="//md:SPSSODescriptor">                                  
      <iso:assert 
         test="md:NameIDFormat[text() != '']">
Warning (03): Each SPSSODescriptor should contain NameIDFormat with one or more values
      </iso:assert>  
   </iso:rule>
</iso:pattern>
