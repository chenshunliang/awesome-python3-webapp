import fileinput


def readtext(url):
    lines = fileinput.input(url)
    print
    len(lines)
    for l in lines:
        print(l)
