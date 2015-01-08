import web


def requires_admin(method):
    def wrapper(self, *args, **kwargs):
        if web.ctx.session.isAdmin == 0:
            raise web.seeother('/login/')
        else:
            return method(self, *args, **kwargs)
    return wrapper


def get_logged_user():
    try:
        return web.ctx.session.logged
    except:
        return None


def get_logoff_url():
    return '/admin/logout/'
