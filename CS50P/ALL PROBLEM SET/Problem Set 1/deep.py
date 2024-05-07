# Get input from user and  if it is deep thought print "yes" otherwise "no"
deep_thought =input("what is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
if deep_thought == "42":
    print("Yes")
elif deep_thought == "forty two":
    print("Yes")
elif deep_thought == "forty-two":
    print("Yes")
else:
    print("No")