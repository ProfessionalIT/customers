# -*- coding: utf-8 -*-
# Database Connection variables
DBN='mysql'
HOST='localhost'
DB='cavalgad_bd'
USER='cavalgad_user'
MODE='fastcgi'    # mod_python, fastcgi, mod_wsgi
ENV='production' # production or development
PWD='Master11235813'
# Generic configuration website variables
WEBSITE_URL='http://www.cavalgadadomar.art.br'
WEBSITE_NAME='Empresa de Teste - Porto Alegre - RS'
ADMIN_VERSION='001b'

AUTO_MODERATE=True # If True auto approve (status = 'A') a record.
CONTROL_CONCURRENT_ACCESS=False # If True implements a record lock / concurrent control access in a record.

# Get the Active Modules for the perfis
from model import get_active_admin_modules, get_active_oper_modules, get_active_moderate_modules
admin_modules = get_active_admin_modules()
oper_modules = get_active_oper_modules()
moderate_modules = get_active_moderate_modules()

ACTIVE_MODULES_ADMIN = [(str(row.class_name), row.titulo.encode('utf8')) for row in admin_modules]
ACTIVE_MODULES_OPER =  [(str(row.class_name), row.titulo.encode('utf8')) for row in oper_modules]
ACTIVE_MODULES_MODER = [(str(row.class_name), row.titulo.encode('utf8')) for row in moderate_modules]
