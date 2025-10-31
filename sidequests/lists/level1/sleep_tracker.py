hours_slept = input("How many hours did you sleep for a week?")

hours = hours_slept.split()
total =0
for h in range(len(hours)):
  hours[h] = int(hours[h])
  total = hours[h] + total
  print(hours[h])
  print(f"total amount of hours slept this week: {total}")