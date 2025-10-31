# Dungeon 4 — Count the Multiples ⚡
# Task:
# Ask the user for a number n.
# Loop from 1 to n.
# Count how many numbers are divisible by 3 in that range.
# At the end, print:
# There are X numbers divisible by 3.
# Rules:
# Do not print each number as you go.
# You must use a counter variable (like total or count) that increases when you find a divisible number.


n = int(input("Enter your number: \n"))
multiples = 0
for c in range(1, n+1):
  if c % 3 == 0:
    multiples += 1

print(f"There are {multiples} numbers divisible by 3.")