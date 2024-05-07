# we use *args unpack list of items
# we use **kwargs to unpack dictionary
def f(*args, **kwargs):
    print("Named:", kwargs)


f(galleons=100, sickles=50, knuts=25)