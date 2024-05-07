# ask the student their score for grading
score = int(input("Score: "))
# print the grade based on their score.
# this type is special in pyton programming.If score greater than or equal to 90 and less than or equal to 100.
# if both condition true only it will print the grade.
if 90 <= score <= 100:
      print("Grade: A")
elif 80 <= score < 90:
      print("Grade: B")
elif 70 <= score < 80:
      print("Grade: C")
elif 60 <= score < 70:
      print("Grade: D")
else:
      print("Grade: F")