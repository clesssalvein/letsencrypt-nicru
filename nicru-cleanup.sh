#!/bin/bash

# vars
nicruUser=$1
nicruPass=$2
nicruAppLogin=$3
nicruAppPass=$4
nicruServiceName=$5
TXT_SUBDOMAIN=$6
TXT_DOMAIN=$7

# add dns entry at dns server
./nicru-del-entry.py "$nicruUser" "$nicruPass" "$nicruAppLogin" "$nicruAppPass" "$nicruServiceName" "$TXT_SUBDOMAIN" "$TXT_DOMAIN"

# delete token file
rm -f ./nic_token.json
