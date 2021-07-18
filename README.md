## **About**

Script for automatically get "Let's Encrypt" wildcard domain certificate at CentOS, using delegated NS server at NIC.RU

## **Requirements**

* Domain for which we want get wildcard letsencrypt certificate **(Domain's name servers (NS) should be delegated to DNS server at NIC.RU)**
* At NIC.RU DNS service there must be A record containing domain, for which we need to get certificate
* CentOS 7
* Python >= 3.6
* certbot >= 1.11.0

## **Installation**

* At https://www.nic.ru
  * Login to your account
  * go to "Услуги/DNS-хостинг" - Управление DNS-зонами - "Добавить домен"
  * add your domain "example.com" to list
  * delegate NS servers of domain "example.com" to nic.ru
  * add any A-record for your domain (for example: "@ 	A 	1.1.1.1")
  * go to "Услуги/DNS-хостинг". Column "Услуга" contains alphabetical name: **<SERVICE_ID>**. Remember it
  * go to: https://www.nic.ru/manager/oauth.cgi?step=oauth.app_register
  * create APP named "**letsencrypt_nicru**"
  * get and remember: **APP-LOGIN**, **APP-PASSWORD**

* At CentOS 7
  ```
  yum install -y epel-release
  ```
  ```
  yum install -y git certbot python36
  ```
  ```
  pip3.6 install requests nic-api
  ```
  ```
  cd /opt/
  ```
  ```
  git clone https://github.com/clesssalvein/letsencrypt-nicru.git
  ```

## **Usage**
* Edit variables in "start.sh"
* Run ```./start.sh```

## **How it works**
* "start.sh" contains variables and starts certbot with auth script "nicru-auth.sh" and postscript "nicru-cleanup.sh"
* "nicru-auth.sh" starts "nicru-add-entry.py", which put to NIC.RU dns server TXT entry with certbot validation string
* certbot validates text string
* after successfull validation certbot generates a certificate and downloads it to the local directory /etc/letsencrypt
* "nicru-cleanup.sh" starts "nicru-del-entry.py", which delete TXT entry with certbot validation string at NIC.RU dns server

## Thanks
Big Thanks to Sergey "andr1an" (https://github.com/andr1an/nic-api) for NIC-API
