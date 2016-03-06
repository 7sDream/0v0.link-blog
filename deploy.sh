#!/bin/bash
#
# Useage:
#   Auto deploy site to apache.
#
# Arguments:
#   $1: Website domain

if [ -z "$1" ]; then
    echo "No argument!"
    exit 1
fi

cd "$(dirname $0)"

SCRIPT=`realpath $0`
BASE_DIR=`dirname $SCRIPT`

sed -e "s#%BASE_DIR%#${BASE_DIR}#" -e "s#%domain%#$1#" deploy/apache.conf.template > "$1.conf"

sudo mv -f "$1.conf" "/etc/apache2/sites-available/$1.conf"

sudo a2ensite "$1"

sudo service apache2 reload

