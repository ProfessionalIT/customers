# -*- coding: utf-8 -*-
# Database Connection variables
DBN='postgres'
HOST='localhost'
DB='equine_website'
USER='equine_website'
MODE='fastcgi'    # mod_python, fastcgi, mod_wsgi
ENV='development' # production or development
PWD='Master12131415'
# Generic configuration website variables
WEBSITE_URL='http://localhost:8080'
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
