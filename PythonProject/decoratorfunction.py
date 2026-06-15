# def smart_sub(fun):
#     def wrapper(x, y):
#         if x < y:
#             x, y = y, x
#         return fun(x, y)
#     return wrapper
#
# @smart_sub
# def sub(x, y):
#     s = x - y
#     print(s)
#     return
# sub(3, 2)
# sub(2, 3)

def smart_div(fun):
    def wrapper(x, y):
        if y < x:
            x, y = y, x
        return fun(x, y)
    return wrapper

@smart_div
def div(x, y):
    res = x / y
    print(res)
    return
div(1, 5)
div(5, 1)
div(2, 0)