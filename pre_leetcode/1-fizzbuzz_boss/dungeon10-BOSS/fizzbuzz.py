# 🏰 Dungeon 10 — FizzBuzz Boss Fight
# Goal: Create a function that returns a list of strings following the FizzBuzz rules.
# Task:
# Ask the user for a number n.
# Loop from 1 to n.
# For each number:
# If divisible by both 3 and 5, append "FizzBuzz" to the list.
# If divisible by 3 only, append "Fizz".
# If divisible by 5 only, append "Buzz".
# Otherwise, append the number as a string.
# At the end, print or return the full list.
# Hints:
# Use an empty list first: results = []
# Append items: results.append(...)
# Check divisible by 3 and 5 first! (i % 3 == 0 and i % 5 == 0)
# Convert numbers to strings when appending numbers.

n = int(input("Enter a number"))

results = []
for i in range(1, n+1):
  if i % 3 == 0 and i % 5 == 0:
    results.append("FizzBuzz")
  elif i % 3 == 0:
    results.append("Fizz")
  elif i % 5 == 0:
    results.append("Buzz")
  else:
    results.append(str(i))

print(results)
