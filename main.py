# Input user names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_string = combined_names.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t + r + u + e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

love = l + o + v + e

love_scor = str(true) + str(love)
love_score = int(love_scor)
if (love_score < int(10)) or (love_score > int(90)):
  print(f"your score is {love_score}, you together like coke and mentos.")
elif (love_score >= int(40)) or (love_score <= int(50)):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
