import orm
from models import User, Blog, Comment
import asyncio
import inspect
from urllib import parse
import time


# async def test(loop):
#     await orm.create_pool(loop, user='chensl', password='123456', db='web_blog')
#
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#
#     await u.save()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.run_forever()

def fun(name, chen=1, *args, a, **kw):
    pass


sig = inspect.signature(fun)
t = (1,)
print(type(sig))
print(type(t))
print(sig is tuple)
for k, v in sig.parameters.items():
    print(v.kind)
print('....')
# print(**'a')

qsdata = "test=test&test2=test2&test3=test3"
qs = parse.parse_qs(qsdata, keep_blank_values=True, strict_parsing=True)
print(qs)

print(type(('12,qw')))
print(time.time())
