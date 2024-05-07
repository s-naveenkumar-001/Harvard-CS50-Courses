
#  if we run this code on cs50 vscode. it shows one error "outdated 1" is a correct code
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
# Using try and except print the year-month-day
# In try if the input is the integer format. we split the input as month, day, year.
    try:
        month, day, year = date.split("/")
# using condition if we check the month in between one and twelve and we check day in between one and thirty one.
# If both cases are satisfy using break it will get out of the loop and print year-month-day.
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
# Else in the except we use try and except. In tey function we split the input as old_month, old_day, and year.    
    except:
        try:
            old_month, old_day, year = date.split(" ")
# In for loop using len function we store the "list" index values in the "i".
            for i in range(len(months)):
# Using condition if old_month in the "month[i]" list. we print the idex value of the month and we add plus one to the index value. because index start from zero.
                if old_month == months[i]:
                    month = i + 1 
# Using replace we replace the comma in the old_day and store the value in the day variable. 
            day = old_day.replace(",","")
# using condition if we check the month in between one and twelve and we check day in between one and thirty one. 
# If both cases are satisfy using break it will get out of the loop and print year-month-day
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
#If any error accours we print empty line and pass to the next line.
        except:
            print()
            pass

# If user enter month or date like "1/1/2023" using format string we zero before month and day "01/01/2023"
print(f"{int(year)}-{int(month):02}-{int(day):02}")

