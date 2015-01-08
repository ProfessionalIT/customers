# -*- coding: utf-8 -*-
import web

import website
import admin
from configuration import MODE

urls = (
  '/admin', admin.app,
  '', website.app
)


class Main():
    """
    pass
    """

    dl = 'Leandro'

    def __init__(self):
        """
        pass
        """

        super(Main, self).__init__()

    def GET(self):
        """
        sdas
        """
        raise web.seeother("/index")

webapp = web.application(urls, globals())
init_params = {'captcha': 0, 'isAdmin': 0, 'admin_user': ''}
session = web.session.Session(webapp, web.session.DiskStore('sessions'),
                              initializer=init_params)


def session_hook():
    """
    sdasd
    asdasd
    """
    web.ctx.session = session

webapp.add_processor(web.loadhook(session_hook))

if MODE == 'production':
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

#web.config.debug = False
if __name__ == "__main__":
    webapp.run()
