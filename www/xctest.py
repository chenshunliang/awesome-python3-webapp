# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#
#         # print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         # print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         # print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)

# import asyncio
#
#
# async def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = await asyncio.sleep(5)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
from objrelationmap import Model, StringField, IntegerField
import asyncio
import mysqlhelper


class User(Model):
    __table__ = 'user'

    id = IntegerField(primary_key=True)
    name = StringField()

# user = User(id=3, name='test')
# f = user.findAll()
# f.send(None)

# loop = asyncio.get_event_loop()
# mysqlhelper.create_pool(loop, user='chensl', password='123456', db='test')
# loop.run_until_complete()
# loop.close()
