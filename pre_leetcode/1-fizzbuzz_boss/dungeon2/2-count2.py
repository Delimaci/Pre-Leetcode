# Dungeon 2 — The Fruit Baskets 🍎
# You are sorting fruit baskets numbered from 1 to n.
# Your Task:
# Ask the user for a number n.
# For each number, print:
# "Basket number: X"
# Where X is the current number in the loop.
# That’s it.

#Expected Style of Output:
# Basket number: 1
# Basket number: 2
# Basket number: 3
# ...


n = int(input("Enter your number"))

for f in range(1, n+1):
  print(f"Basket number: {f}")