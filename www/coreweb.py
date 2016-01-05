#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenshunliang'

'''
async web core.
'''
import asyncio, os, inspect, logging, functools

from urllib import parse

from aiohttp import web


def get(path):
    '''
    define decorator @get('/path')
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'get'
        wrapper.__route__ = path
        return wrapper

    return decorator


def post(path):
    '''
    define decorator @get('/path')
    '''

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)

        wrapper.__method__ = 'post'
        wrapper.__route__ = path
        return wrapper

    return decorator


def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.defaut == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)


class RequestHandler(object):
    pass
