from datetime import date
glasses_count = int(input("How many glasses of water have you drank today? \n"))

did_meet_goal = input("Did you meet your daily goal? \n")


date_today = date.today()

file = open("water_log.txt", "a")
file.write(f"{date_today} - {glasses_count} glasses - {did_meet_goal}")
file.close()