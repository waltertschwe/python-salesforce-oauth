Salesforce Micro Service
========================

This project provides the middleware layer between Salesforce and custom built applications

Authentication
==============

This package currently supports Username and Password and JWT Bearer Token Flow::

Update the .env with client credenitals for the grant type being used

Required values for Username and Password grant type:

::

        SALESFORCE_OAUTH_CONSUMER_TOKEN
        SALESFORCE_OAUTH_CONSUMER_SECRET
        SALESFORCE_USER
        SALESFORCE_PASSWORD
        SALESFORCE_ACCESS_TOKEN_URL

Required values for JWT grant type:

::

        SALESFORCE_OAUTH_CONSUMER_TOKEN
        SALESFORCE_CERTIFICATE
        SALESFORCE_USER
        SALESFORCE_PRIVATE_KEY
        

