# Track daily temperatures 🌡️
# Goal: Ask the user for daily temperatures for a week, convert them to integers, then:
# Print each day’s temperature individually.
# Print the first, middle, and last day’s temperature using direct indices.
# Print the total temperature for the week.


daily_temps = input("Enter daily temperatures for a week, separated by spaces: \n")

temps = daily_temps.split()
total = 0
for t in range(len(temps)):
  temps[t] = int(temps[t])
  total = temps[t] + total
  print(temps[t])

print(f"first: {temps[0]}, middle: {temps[3]}, last: {temps[6]}")
print(f"Total temperature for the week: {total}")
