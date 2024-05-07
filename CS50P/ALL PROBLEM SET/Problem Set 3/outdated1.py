# create a list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# we prompt the user using while loop and get input from user.
while True:
    date = input("Date: ")
# In try if the input is the integer format. we split the input as month, day, year.
    try:
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            new_month, year = date.split(", ")
            month, day = new_month.split(" ")
            # No need to check if mm in months. KeyError is handled separately.
            month = (months.index(month)) + 1
        if int(month) > 12 or int(day) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
# If user enter month or date like "1/1/2023" using format string we zero before month and day "01/01/2023"
    else:
        print(f"{int(year)}-{int(month):02}-{int(day):02}")
        break