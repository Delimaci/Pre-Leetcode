# Dungeon 5 — “Fizz Only” 🍹
# Goal:
# Check numbers from 1 to n and print "Fizz" if a number is divisible by 3.
# Otherwise, just print the number itself.
# Your Task:
# Ask the user for a number n.
# Loop from 1 to n using range(1, n+1).
# For each number:
# If divisible by 3 → print "Fizz"
# Else → print the number itself
# Hints:
# Use % to check divisibility.
# Use if/else.
# No lists needed yet.


n = int(input("Enter your number"))

for c in range(1, n+1):
  if c % 3 == 0:
    print("Fizz")
  else:
    print(c)