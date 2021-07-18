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
./nicru-add-entry.py "$nicruUser" "$nicruPass" "$nicruAppLogin" "$nicruAppPass" "$nicruServiceName" "$TXT_SUBDOMAIN" "$TXT_DOMAIN" "$CERTBOT_VALIDATION"

# wait for dns entry create
sleep 120
