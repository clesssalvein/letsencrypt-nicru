#!/usr/bin/python3.6

# modules
import sys
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
CERTBOT_VALIDATION = sys.argv[8]

# auth
oauth_config = {
    'APP_LOGIN': nicruAppLogin,
    'APP_PASSWORD': nicruAppPass
}
api = DnsApi(oauth_config)

api.authorize(username=nicruUser,
              password=nicruPass,
              token_filename='nic_token.json')

#api.services()
#api.zones('MKDUBKI')

# define service and domain
api.records(nicruServiceName, TXT_DOMAIN)

# write TXT record "_acme..."
record_www = TXTRecord(name=TXT_SUBDOMAIN, txt=CERTBOT_VALIDATION, ttl=60)
api.add_record(record_www, nicruServiceName, TXT_DOMAIN)

# commit changes
api.commit(nicruServiceName, TXT_DOMAIN)
