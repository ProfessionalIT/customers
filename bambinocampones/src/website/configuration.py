# -*- coding: utf-8 -*-
"""
    Configuration File of projects and apps.
"""
# Database Connection variables
DBN = 'sqlite'
#DBN = 'postgres'
HOST = 'localhost'
#DB = 'fenix_db'
DB = 'database'  # sqlite database
USER = 'fenix_fenix'
MODE = 'fastcgi'    # mod_python, fastcgi, mod_wsgi
ENV = 'development'  # production or development
PWD = 'Master12131415'
# Generic configuration website variables
WEBSITE_URL = 'http://localhost:8080'
STATIC_URL = '/static/'
WEBSITE_NAME = 'Empresa de Teste - Porto Alegre - RS'
ADMIN_VERSION = '001b'

# If True auto approve (status = 'A') a record.
AUTO_MODERATE = True
# If True implements a record lock / concurrent control access in a record.
CONTROL_CONCURRENT_ACCESS = False

# Get the Active Modules for the perfis
from model import (get_active_admin_modules,
                   get_active_oper_modules,
                   get_active_moderate_modules)

admin_modules = get_active_admin_modules()
oper_modules = get_active_oper_modules()
moderate_modules = get_active_moderate_modules()

ACTIVE_MODULES_ADMIN = [(str(row.class_name),
                        row.titulo.encode('utf8')) for row in admin_modules]
if oper_modules:
    ACTIVE_MODULES_OPER = [(str(row.class_name),
                            row.titulo.encode('utf8')) for row in oper_modules]
else:
    ACTIVE_MODULES_OPER = []
if moderate_modules:
    ACTIVE_MODULES_MODER = [(str(row.class_name),
                            row.titulo.encode('utf8'))
                            for row in moderate_modules]
else:
    ACTIVE_MODULES_MODER = []
if ENV == 'development':
    STATIC_URL = WEBSITE_URL + STATIC_URL
