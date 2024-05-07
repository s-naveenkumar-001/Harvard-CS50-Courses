# Wouldn’t it be nice if you had a program that could tell you what to eat when
def main():
    answer = input("what time it is: ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")
# we split hours and time and we change hours and time into float  value and return the value
def convert(time):
    hours, minutes = time.split(":")
    new_minutes =float(minutes) / 60
    return float(hours) + new_minutes

if __name__ == "__main__":
    main()