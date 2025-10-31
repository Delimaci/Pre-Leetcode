step_count = input("How many steps have you walked each day?")

steps = step_count.split()
total = 0
for s in range(len(steps)):
  steps[s] = int(steps[s])
  total = steps[s] + total
  print(steps[s])
  print(f"Total steps: {total}")

