from salesforce.connect import SalesForceOAuth
from salesforce.query import SalesForceQuery

## Authenticate to Salesforce using JWT Grant Type
sf = SalesForceOAuth()
token = sf.getAccessToken('jwt')
sfq = SalesForceQuery(token)

salesforce_objects = ['Account','Contact']

## iterate over sf objects and write fields to files
for salesforce_object in salesforce_objects:
    data = sfq.describeObject(salesforce_object)
    filename = "fields/" + salesforce_object + '.txt'
    filename_descriptive = "fields/" + salesforce_object + '_details.txt'

    ## empties the file of all current fields
    open(filename, 'w').close()

    ## writes new fields to files
    with open(filename, 'a') as out:
        for field in data['fields']:
            print(field['name'])
            out.write(field['name'] + ',')

    ## more detailed version of the fields  
    with open(filename_descriptive, 'a') as out:
        for field in data['fields']:
            out.write(field['name'] + ',' + field['type'] + '\n')
