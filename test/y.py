def countNum(length):
		while length > 1:
				length -= 1
				a = (yield length)
				print(a)


def repeater(value):
		while True:
				new = (yield value)
				if new is not None:value = new


