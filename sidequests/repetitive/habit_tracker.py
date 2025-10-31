from datetime import datetime
habit = input("What's your habit?")

habit_completed = input("Have you completed your habit?")

now = datetime.now()
date_today = now.date()
time_today = now.time()
with open("habit_tracking.txt", "a") as file:
  file.write(f"{date_today} - {time_today}- {habit} - {habit_completed}\n")
with open("habit_tracking.txt", "r") as file:
  lines = file.readlines()
  lines.sort()
with open ("habit_tracking.txt", "w") as file:
  file.writelines(lines)
