calories_count = input("How many calories have you ate each day for a week?")

calories = calories_count.split()
total = 0
for c in range(len(calories)):
  calories[c] = int(calories[c])
  total = calories[c] + total
  print(calories[c])
print(f"Your total calorie count this week: {total}")