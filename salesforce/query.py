import os
import json
from connect import SalesForceOAuth
from simple_salesforce import Salesforce

class SalesForceQuery:
    def __init__(self, token):
        self.instance_url = token['instance_url']
        self.access_token = token['access_token']
        self.sf = Salesforce(instance_url=self.instance_url, session_id=self.access_token)

    def getDataById(self, dataType, salesforce_id):
        data = self.sf.Contact.get(salesforce_id)
        ##data = sf.(dataType).get(salesforce_id)
        ##print(data)

    def getDataByCustomField(self, dataType, custom_field):
        contact = self.sf.Contact.get_by_custom_id('My_Custom_ID__c', '22')
        pass

    def getDataByQuery(self, query):
        data = self.sf.query(query)
        return data

    def getDataByDateRange(self, dataType, date_range):
        pass

    def getObjectMetaData(self, obj):
        metadata = self.sf.Contact.metadata()
        ##print(metadata)

    def describeObject(self, salesforce_obj): 
        data = self.sf.Account.describe()
        return data

    def sfObjectToJson(self, data):
        json_data = json.dumps(data)
        return json_data

    def getObjectType(self, salesforce_obj_type):
        return {
            'Contact' : 'self.sf.Contact',
            'Account' : 'self.sf.Account'
        }[salesforce_obj_type]


sf = SalesForceOAuth()
token = sf.getAccessToken('password')
salesforce_id = '0031a00000VG4mK'
dataType = 'Contact'
sfq = SalesForceQuery(token)
sfq.getDataById(dataType, salesforce_id)
##data = sfq.getDataByQuery("SELECT Id, Email FROM Contact WHERE LastName = 'Schweitzer'")
salesforce_obj = 'Contact'
data = sfq.describeObject(salesforce_obj)
for field in data['fields']:
    print(field['name'])



