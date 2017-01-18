## ! Important Notice !

This Proof of Concept plugin is unmaintained and significantly outdated.

Refer to the http://opal.openhealthcare.org.uk documentation for current information about Opal


This is zendesk - an [OPAL](https://github.com/openhealthcare/opal) plugin.

## Installation

1. Add to your application's INSTALLED_APPLICATIONS.
   
    'zendesk',

2. Add the ZENDESK_HOST setting. 

This setting should be without the scheme (http://) or any trailing slash so for example: 

    ZENDESK_HOST = 'yourinstitution.zendesk.com'
