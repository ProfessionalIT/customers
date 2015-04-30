# -*- coding: utf-8 -*-
# Database Connection variables
DBN = 'sqlite'
HOST='localhost'
DB = 'database'  # sqlite database
USER='bambino'
MODE='mod_wsgi'    # mod_python, fastcgi, mod_wsgi
ENV='production' # production or development
PWD='Master12131415'
# Generic configuration website variables
WEBSITE_URL='http://www.bambinocamppones.com.br'
WEBSITE_NAME='Escola de Educação Infantil Bambino Camponês - Creche, Maternal e Educação Pré em Canoas/RS.'
ADMIN_VERSION='001b'

CONTROL_CONCURRENT_ACCESS = False
AUTO_MODERATE = True
# Get the Active Modules for the perfis
from model import get_active_admin_modules, get_active_oper_modules, get_active_moderate_modules
admin_modules = get_active_admin_modules()
oper_modules = get_active_oper_modules()
moderate_modules = get_active_moderate_modules()


ACTIVE_MODULES_ADMIN = [(str(row.class_name), row.titulo.encode('utf8')) for row in admin_modules]
ACTIVE_MODULES_OPER =  [(str(row.class_name), row.titulo.encode('utf8')) for row in oper_modules]
ACTIVE_MODULES_MODER = [(str(row.class_name), row.titulo.encode('utf8')) for row in moderate_modules]
