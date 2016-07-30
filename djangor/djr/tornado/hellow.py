# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import os
import tornado.auth


class MainHandle(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie('my', 'asda', expires=15 * 60 * 60)
        self.write('hello world')


class CreateSecure(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.write(bytes(os.urandom(24)))
        self.finish()


class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(tornado.escape.json_encode({'name': 'chen', 'age': 11}))


# class GoogleHandler(tornado.web.RequestHandler, tornado.auth.GoogleMixin):
#     @tornado.web.asynchronous
#     def get(self):
#         if self.get_argument("openid.mode", None):
#             self.get_authenticated_user(self._on_auth)
#             return
#         self.authenticate_redirect()
#
#     def _on_auth(self, user):
#         if not user:
#             self.authenticate_redirect()
#             return
#             # Save the user with, e.g., set_secure_cookie()


application = tornado.web.Application([
    (r'/', MainHandle),
    (r'/secure', CreateSecure),
    (r'/j', JsonHandler),
    # (r'/g', GoogleHandler)
], debug=True)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
