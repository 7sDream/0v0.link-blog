#!/bin/bash
#
# Useage:
#   Auto deploy site to apache.
#
# Arguments:
#   $1: Website domain
#   $2: Python env dir, Optional

if [ -z "$1" ]; then
    echo "No argument!"
    exit 1
fi

cd "$(dirname $0)"

SCRIPT=`realpath $0`
BASE_DIR=`dirname ${SCRIPT}`
PYTHON_SITE_PACKAGE=`python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`

# git pull

python3 manage.py makemigrations

python3 manage.py migrate

sed -e "s#%BASE_DIR%#${BASE_DIR}#" -e "s#%domain%#$1#" deploy/apache.conf.template -e "s#%PY_LIB%#$PYTHON_SITE_PACKAGE#" > "$1.conf"

sudo mv -f "$1.conf" "/etc/apache2/sites-available/$1.conf"

sudo a2ensite "$1"

sudo service apache2 reload

