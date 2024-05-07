# we use **kwargs to unpack dictionary
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons" : 100, "sickles" : 50, "knuts" : 25}

print(total(**coins), "knuts")