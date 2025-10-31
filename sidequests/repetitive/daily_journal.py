from datetime import datetime

grateful_entry = input("What are you grateful for today?")

today = datetime.now()

date_today = today.date()
time_today = today.strftime("%H:%M")

with open("grateful_entries.txt", "a") as file:
  file.write(f"{date_today} - {time_today} - I am grateful for: {grateful_entry}\n")
with open("grateful_entries.txt", "r") as file:
  lines = file.readlines()
  lines.sort()