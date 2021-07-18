#!/bin/bash

# vars
nicruUser="xxx/NIC-D" # NIC.RU COMMON ACCOUNT LOGIN
nicruPass="xxx" # NIC.RU COMMON ACCOUNT PASSWORD
nicruAppLogin="xxx" # app "letsencrypt_nicru" APP-LOGIN
nicruAppPass="xxx" # app "letsencrypt_nicru" APP-PASSWORD
nicruServiceName="<SERVICE_ID>" # go to "Услуги/DNS-хостинг", column "Услуга" contains alphabetical name <SERVICE_ID>
domain="example.com" # domain for cert create
subdomain="_acme-challenge" # subdomain "_acme-challenge", don't change it
letsencryptServer="https://acme-v02.api.letsencrypt.org/directory" # letsencrypt server url
email="clesssalvein@gmail.com" # email for notifies

# certbot run
certbot certonly --manual --preferred-challenges=dns \
    --manual-auth-hook "./nicru-auth.sh $nicruUser $nicruPass $nicruAppLogin $nicruAppPass $nicruServiceName $subdomain $domain" \
    --manual-cleanup-hook "./nicru-cleanup.sh $nicruUser $nicruPass $nicruAppLogin $nicruAppPass $nicruServiceName $subdomain $domain" \
    -d *.$domain -d $domain --email=$email \
    --server $letsencryptServer --agree-tos --non-interactive --manual-public-ip-logging-ok --force-renewal #--dry-run

# nginx reload
/usr/sbin/nginx -s reload
