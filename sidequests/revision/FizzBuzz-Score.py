# 🏰 Dungeon 10: The String Fizz Score Trial

# You are given a string `s`.

# 1. First, calculate a score for the string:
#    - The score is the sum of the absolute differences between each pair of adjacent characters.
#    - Use: abs(ord(s[i]) - ord(s[i+1])) for each i.

#    Example:
#    s = "abc"
#    score = |a-b| + |b-c| = 1 + 1 = 2

# 2. Then, based on the score:
#    - If the score is divisible by 3 → print "Fizz"
#    - If the score is divisible by 5 → print "Buzz"
#    - If the score is divisible by both 3 and 5 → print "FizzBuzz"
#    - Otherwise → print the actual score.

# Input:
# A single string s.

# Output:
# A single string or number depending on the rules above.


s = input("Enter a string: ")
difference = 0

for i in range(len(s) - 1):
  difference += abs(ord(s[i]) - ord(s[i + 1]))
if difference % 3 == 0 and difference % 5 == 0:
  print("FizzBuzz")
elif difference % 3 == 0:
  print("Fizz")
elif difference % 5 == 0:
  print("Buzz")
else:
  print(difference)
