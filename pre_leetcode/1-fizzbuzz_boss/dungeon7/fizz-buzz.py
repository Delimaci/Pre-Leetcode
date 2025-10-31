# 🏰 Dungeon 7 — Fizz + Buzz Combo ⚔️
# Your Task:
# Ask the user for a number n.
# Loop from 1 to n (inclusive).
# For each number:
# If the number is divisible by 3, print "Fizz".
# If the number is divisible by 5, print "Buzz".
# If the number is divisible by both 3 and 5, print "FizzBuzz".
# Otherwise, print the number itself.
# Hints (without giving full solution):
# You already know how to check divisibility with %.
# Think about the order of your if/elif statements so that numbers divisible by both 3 and 5 are handled correctly.
# You can print directly inside the loop — no lists needed yet.
# Example Input/Output:
# Input: n = 15
# Output:


n = int(input("Enter a number"))

for i in range(1, n+1):
  if i % 5 == 0 and i % 3 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)