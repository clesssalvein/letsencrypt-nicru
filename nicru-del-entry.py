#!/usr/bin/python3.6

# modules
import sys
import json
from nic_api import DnsApi
from nic_api.models import ARecord
from nic_api.models import TXTRecord

# vars
nicruUser = sys.argv[1]
nicruPass = sys.argv[2]
nicruAppLogin = sys.argv[3]
nicruAppPass = sys.argv[4]
nicruServiceName = sys.argv[5]
TXT_SUBDOMAIN = sys.argv[6]
TXT_DOMAIN = sys.argv[7]

# auth
oauth_config = {
'APP_LOGIN': nicruAppLogin,
'APP_PASSWORD': nicruAppPass
}
api = DnsApi(oauth_config)

api.authorize(username=nicruUser,
                  password=nicruPass,
                  token_filename='nic_token.json')

api.services()
api.zones(nicruServiceName)

# all dns records list
recordList = api.records(nicruServiceName, TXT_DOMAIN)

# debug
#print(type(recordList).__name__)

# define array of IDs of TXT Records "_acme..."
listRecordTxtIds = []

# for every record
for x in range(len(recordList)):

    # if it's TXT record
    if (type(recordList[x]).__name__) == "TXTRecord":

        # debug
        #print(recordList[x])

        # convert TXT record to str
        recordTxtString = str(recordList[x])

        # debug
        #print(type(recordTxtString).__name__)

        # replace ' to " for correctly parse of json.loads
        recordTxtString = recordTxtString.replace('\'', '\"')

        # convert str to json
        recordTxtJson = json.loads(recordTxtString)

        # debug
        #print(type(recordTxtJson).__name__)

        # debug
        #print(recordTxtJson['name'])

        # if record contains "_acme...", put ID of record to array
        if recordTxtJson['name'] == TXT_SUBDOMAIN:
            listRecordTxtIds.append(recordTxtJson['id'])

# delete every TXT record with "_acme..." by ID
for x in range(len(listRecordTxtIds)):
    print(listRecordTxtIds[x])
    api.delete_record(listRecordTxtIds[x], nicruServiceName, TXT_DOMAIN)
    api.commit(nicruServiceName, TXT_DOMAIN)
