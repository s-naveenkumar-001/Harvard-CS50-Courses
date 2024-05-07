# import inflect library and read the inflect " p.join() " in the documentation .

import inflect
p = inflect.engine()
# create a empty list to store the values.
names = []
# Using while loop prompt the user and in try get input from user and using append() function add the elements into the list.
# In except catch the Eoferror. when user enter control + d using except break get out of loop. 
while True:
    try:
        name=input("Name: ")
        names.append(name)
# when user enter control + d using except catch the EOFError and print one line and using break get out of the loop.
    except EOFError:
        
        print()
        break
    
# create a variable and using p.join() print the stored list values in the series comma order.
# print " Adieu, adieu, to " and using concatenation " + " add the stored value.
output = p.join(names)
print("Adieu, adieu, to " + output)
