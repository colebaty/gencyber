#!/bin/bash
# automated installation of DVWA
# 
# target is a LAMP stack running DVWA
#
# script helps automate process
# must be run as root

if [ ${EUID} -ne 0 ]; then
    echo "must be run as root; quitting"
    exit
fi

WORKING_DIR=/var/www
DVWA_GH=https://github.com/digininja/DVWA.git

source /root/secrets.sh
rm -f /root/secrets.sh

#REQUIREMENTS=("apache2" "libapache2-mod-php" "mariadb-server" "mariadb-client" "php7.4" "php7.4-mysqli" "php7.4-gd")

#apk --no-cache --update add ${REQUIREMENTS}

echo "[+] installing required packages"
apt-get update -y -q && apt-get install -y -q \
	git \
	apache2 libapache2-mod-php \
	mariadb-server mariadb-client \
	php7.4 php7.4-mysqli php7.4-gd  

echo "[+] setting up DVWA"
echo "[+] cloning DVWA"
cd ${WORKING_DIR}
git clone ${DVWA_GH}
rm -rf ${WORKING_DIR}/html/*
mv ${WORKING_DIR}/DVWA/* ${WORKING_DIR}/html/
chown -R www-data:www-data ${WORKING_DIR}/html/*
rm -rf ${WORKING_DIR}/DVWA

DVWA_DIR=${WORKING_DIR}/html

cp ${DVWA_DIR}/config/config.inc.php.dist ${DVWA_DIR}/config/config.inc.php


echo "[+] setting up database"
mysql < /root/mysql_commands

echo "[+] finished setup"
echo "########### ADDITIONAL STEPS ############"
echo "DATABASE:"
echo -e "\t1) navigate in a browser to <server ip>/index.php\n" \
	"\t2) choose \"Setup/Reset DB\" from the left\n" \
	"\t3) choose the \"Create/Reset DB\" button at the bottom of the page\n" \
	"\n" \
echo "SECURITY"
echo -e "\t1) navigate in a browser to <server ip>/index.php\n" \
	"\t2) choose \"DVWA Securit\" from the left (toward bottom)\n" \
	"\t3) selecte desired security level\n" \
	"\n" \
	"if there are errors, Google is your friend\n" \
