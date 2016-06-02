import time

a = 10


def test(x):
    global a
    a = 1000
    print(a)
    return 1, 2, 3


f = lambda x, y: x * y

print(test(1))
print(a)
print(f(1, 2))

print(abs(-1212))
print(max([1, 2, 3, 4, 6]))

print(divmod(3, 2))
# help(pow)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = filter(lambda x: x > 5, l)
print(list(l))


class Test(object):
    def __init__(self):
        self.firstValue = 10


print(Test().firstValue)


class Child(Test):
    def __init__(self):
        super(Child, self).__init__()
        self.child = 100


a = Child()
if isinstance(a, Test):
    print('true')
else:
    print('no')
