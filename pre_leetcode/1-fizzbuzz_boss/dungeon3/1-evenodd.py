# Dungeon 3 — Even or Odd Checker ⚔️
# You will loop from 1 to n again, but this time:
# Your Task:
# Ask the user for a number n.
# Loop using for c in range(1, n+1):
# For each number:
# If the number is even, print:
# c is even
# Otherwise, print:
# c is odd
# Do NOT use lists. Only the loop and if/else.

n = int(input("What's your number?"))

for c in range(1, n+1):
  if c % 2 == 0:
    print(f"{c} is even")
  else:
    print(f"{c} is odd")
