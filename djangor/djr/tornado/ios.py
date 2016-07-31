import os
import webbrowser


# print(os.getcwd())

# os.remove(os.path.join(os.getcwd(), 'sdad.py'))

# webbrowser.open('http://www.baidu.com', new=1)

# print(1 == 1 and -1 or 4)
#
# print(eval('1+1'))
from south.utils.py3 import raw_input


def create_class(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo
    else:
        class NoFoo(object):
            pass

        return NoFoo


# my = create_class('foo')
# print(my)
# print(my())
#
# Maaa = type('Maaa', (), {})
# print(Maaa)


def decorator_a(func):
    print("decorator_a")
    return func


def decorator_b(func):
    print("decorator_b")
    return func


@decorator_a
@decorator_b
def foo():
    print("foo")


foo()

exec('a=9')
# print(a)

input('1+2')
raw_input('1+2')
