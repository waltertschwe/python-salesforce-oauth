import os 
import time
import jwt
import pem
import requests
import json
import base64
from calendar import timegm
from datetime import datetime, timedelta
from simple_salesforce import Salesforce
from os.path import join, dirname
from dotenv import Dotenv

""" SalesForce Authentication """
class SalesForceOAuth:
    
    """ Sets up environment values for all grant types """
    def __init__(self):
        dotenv_path = Dotenv(join(dirname(__file__), '..', '.env'))
        os.environ.update(dotenv_path)

        self.consumer_key = os.environ.get("SALESFORCE_OAUTH_CONSUMER_TOKEN")
        self.consumer_secret = os.environ.get("SALESFORCE_OAUTH_CONSUMER_SECRET")
        self.api_domain = os.environ.get("SALESFORCE_API_DOMAIN")
        self.access_token_url = os.environ.get("SALESFORCE_ACCESS_TOKEN_URL") 
        self.username = os.environ.get("SALESFORCE_USER")
        self.password = os.environ.get("SALESFORCE_PASSWORD") 

    """ Determines OAuth Grant Type and runs method 
        returns a dictionary consisinting of an instance_url and access_token
    """
    def getAccessToken(self, grant_type):
        self.grant_type = grant_type
        if grant_type == 'password':
            token = self.passwordGrantType()
        elif grant_type == 'jwt':
            token = self.jwtGrantType()
        elif grant_type == 'web-server':
            self.webGrantType()
        else:
            pass
        
        return token

    """ Password Grant Type for user/server credentials
        need a client_id and client_secret
        returns a dictionary consisting of an instance_url and access_token 
        used to make API calls
    """
    def passwordGrantType(self):
        token = dict()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        post_data = {'grant_type': self.grant_type,
                     'client_id': self.consumer_key,
                     'client_secret': self.consumer_secret,
                     'username': self.username,
                     'password': self.password }

        result = requests.post(self.access_token_url, data=post_data, headers=headers)
        data = json.loads(result.text)
        access_token = data['access_token']
        instance_url = data['instance_url']
        token = { 'instance_url' : instance_url, 'access_token' : access_token } 
        return token 

    """ JWT Token Grant Type - key based authentication 
        returns a dictionary consisting of an instance_url and access_token 
        used to make API calls
    """
    def jwtGrantType(self):
        token = dict()
        certfile = os.environ.get("SALESFORCE_PRIVATE_KEY")

        with open(certfile, "r") as my_cert_file:
            cert = my_cert_file.read()

        payload =  {
                   'alg': 'RS256',
                   'iss': self.consumer_key, 
                   'sub': self.username, 
                   'aud': 'https://login.salesforce.com', 
                   'exp': timegm(datetime.utcnow().utctimetuple()) 
                  } 
        pay_string = (str(payload))

        encoded = jwt.encode(payload, cert, algorithm='RS256')
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        grant_type = 'urn:ietf:params:oauth:grant-type:jwt-bearer'
        post_data = { 'grant_type': grant_type, 
                 'assertion': encoded
               }

        result = requests.post(self.access_token_url, data=post_data, headers=headers)
        data = json.loads(result.text)
        access_token = data['access_token']
        instance_url = data['instance_url']
        token = { 'instance_url' : instance_url, 'access_token' : access_token }
        return token


    def webGrantType(self):
        pass

    def decodeToken(self):  
        pass






