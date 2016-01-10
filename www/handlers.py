#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenshunliang'

'''
async web handles.
'''

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__templates__': 'test.html',
        'users': users
    }
