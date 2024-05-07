# ask the student their score for grading
score = int(input("Score: "))
# print the grade based on their score 
# In tis program we use logical operater "and". it return true if both condition are true.
if score >= 90 and score <= 100:
      print("Grade: A")
elif score >= 80 and score < 90:
      print("Grade: B")
elif score >= 70 and score < 80:
      print("Grade: C")
elif score >= 60 and  score < 70:
      print("Grade: D")
else:
      print("Grade: F")