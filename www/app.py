#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenshunliang'

'''
async web application.
'''

import logging

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

import orm
from coreweb import add_routes, add_static


def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
            autoescape=kw.get('autoescape', True),
            block_start_string=kw.get('block_start_string', '{%'),
            block_end_string=kw.get('block_end_string', '%}'),
            variable_start_string=kw.get('variable_start_string', '{{'),
            variable_end_string=kw.get('variable_end_string', '}}'),
            auto_reload=kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env


async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        return await handler(request)

    return logger


async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        return await handler(request)

    return parse_data


async def response_factory(app,handle):
    async def response(request):
        logging.info('Response handler....')
        r=await handle(request)
        if isinstance(r,web.StreamResponse):
            return r
        if isinstance(r,bytes):
            resp=web.Request(body=r)
            resp.content_type='application/octet-tream'
            return resp
        if isinstance(r,str):


async def init(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='chensl', password='123456', db='web_blog')
    app = web.Application(loop=loop)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
