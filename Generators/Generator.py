#
# def simpleGeneratorFun(book):
#     yield 1
#     print(book)
#
#     yield 2
#
#     print(books)
#     yield 3
#
# book ="Hi How Are You".split(" ")
# books="Fine"
# x = simpleGeneratorFun(book)
# print(next(x))
# print(next(x))
# print(next(x))


def fun(line):
    for i in line:
        yield i

line="hello world"
x=fun(line)
print(next(x),end='')
print(next(x),end='')

print(next(x),end='')

print(next(x),end='')

