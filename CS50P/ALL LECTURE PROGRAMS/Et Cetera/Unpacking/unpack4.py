# we use *args unpack list of items
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins =[100, 50, 25]

print(total(*coins), "knuts")