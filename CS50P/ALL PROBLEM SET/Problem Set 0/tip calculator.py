# Get input from the user and print the tip 
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# remove the leading "$" and return thw amount as float
def dollars_to_float(d):
    dollar = d.replace("$", "")
    d_dollars = float(dollar)
    return d_dollars

# remove the trailing "%" and divide the value / 100 and return the value in float
def percent_to_float(p):
    percents = p.replace("%", "")
    p_percentage = float(percents) / 100
    return p_percentage


main()