# -*- coding:utf-8 -*-


import logging, mysqlhelper, xctest
import asyncio, json, os
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>awesome</h1>')


async def init(loop):
    await mysqlhelper.create_pool(loop, user='chensl', password='123456', db='test')
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    user = xctest.User(id=3, name='test')
    f = user.findAll()
    f.send(None)
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
