<?xml version="1.0" encoding="utf-8"?>
<iso:pattern id="Rule 20" xmlns:iso="http://purl.oclc.org/dsdl/schematron" >
  <iso:rule context="//md:SPSSODescriptor">                                  
    <iso:assert test="md:Extensions/init:RequestInitiator">
Warning (20): SPSSODescriptor should include init:RequestInitiator
    </iso:assert>
  </iso:rule>
</iso:pattern>