# we use *args unpack list of items
# we use **kwargs to unpack dictionary
def f(*args, **kwargs):
    print("positional:", args)


f(100, 50, 25)