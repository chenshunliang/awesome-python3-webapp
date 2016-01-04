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

import orm


async def init(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='chensl', password='123456', db='web_blog')
    app = web.Application(loop=loop)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
