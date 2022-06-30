from statistics import mean, median

#
# def appender(lst = []):
#     lst.append("You")
#     return lst
#
# print(appender())
#
# print(appender())
#
# print(appender([1,2,3]))
#
# print(appender())
#
# print(appender([1,2,3]))
#
#
# def add(x: int, y: int) -> int:
#     return x + y
#
# print(add.__annotations__)
#
# print(add.__annotations__['y'])

def avg(*args):
    return mean(args)

print(avg(*[2, 4, 6, 8, 10, 12], *[1, 2, 3, 4, 5, 6]))

def letters(*word):
    return word

print(letters(*"typing"))


def mixer(b, *args, c=0, **kwargs):
    print(b)
    print(args)
    print(c)
    print(kwargs)


mixer([2, 3, 4], 3, 4, *[5, 8, 9], 6, c=3, f=3, h=5, t=7, y=8)
