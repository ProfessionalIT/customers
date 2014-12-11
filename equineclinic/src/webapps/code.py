# -*- coding: utf-8 -*-
import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
#os.chdir(abspath)
import web

import website
import admin
from configuration import ENV, MODE

from model import setDB, unsetDB

urls = (
  '/admin', admin.app,
  '', website.app
)

class Main():
    def GET(self):
        raise web.seeother("/index")
    

#web.config.session_parameters['timeout'] = 360 
#web.config.session_parameters['ignore_expiry'] = False
#web.config.session_parameters['expired_message'] = 'Session Expired !, Acesse Novamente !'

webapp = web.application(urls, globals())
session = web.session.Session(webapp, web.session.DiskStore('sessions'), initializer={'captcha': 0, 'isAdmin':0, 'admin_user': ''})

def db_handler(handler):
    setDB()
    result=handler()
    unsetDB()
    return result

def session_hook():
    web.ctx.session = session

webapp.add_processor(web.loadhook(session_hook))
webapp.add_processor(db_handler)

if ENV=='production':
    if MODE=='fastcgi':
        web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr) 
        web.config.debug = False
    elif MODE=='mod_python':
        pass
    elif MODE=='mod_wsgi':
        application = webapp.wsgifunc()
    else:
        pass

if __name__=="__main__":
    webapp.run()
