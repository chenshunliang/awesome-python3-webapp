import pdb
def countNum(length):
    while length > 1:
	length -= 1
	a = (yield length)
	print(a)


def repeater(value):
    while True:
	new = (yield value)
	if new is not None:value = new

def pr(value):
    return value

def readfile(path):
    f = open(path,'r+')
    t = f.read()
    print(t)

if __name__ == '__main__':
    import sys
    from timeit import Timer
    import doctest
    from string import Template
    # print(sys.argv[1])
    # print(pr('aaaaa'))
    # print('123'.zfill(6))
    # readfile(sys.argv[2])
   ppdb.set_trace() ############################## Breakpoint ##############################
    print(Timer('a,b = 1,2').timeit())
    print(doctest.testmod())
   tpdb.set_trace() ############################## Breakpoint ##############################
    t = Template('im $name , age is $age')
    print(t.substitute(name = 'chen',age = 19))
    import aaaaaa 
