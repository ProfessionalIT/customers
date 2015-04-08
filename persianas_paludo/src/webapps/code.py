# -*- coding: utf-8 -*-
import web

import website
import admin
from configuration import MODE

web.config.debug = True

urls = (
  '/admin', admin.app,
  '', website.app
)

class Main():
    def GET(self):
        raise web.seeother("/index")

webapp = web.application(urls, globals())
session = web.session.Session(webapp, web.session.DiskStore('sessions'), initializer={'captcha': 0, 'isAdmin':0, 'admin_user': ''})

def session_hook():
    web.ctx.session = session

webapp.add_processor(web.loadhook(session_hook))

if MODE=='production':
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr) 


#web.config.debug = False
if __name__=="__main__":
    webapp.run()
