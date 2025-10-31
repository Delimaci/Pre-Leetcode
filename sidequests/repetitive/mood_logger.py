from datetime import date

user_mood = input("How are you feeling today? \n")

user_rating = int(input("On a scale of 1 to 10, how would you rate your mood? \n"))

today = date.today()

file = open("mood_log.txt", "a")
file.write(f"{today} - {user_mood} ({user_rating}/10) \n")
file.close()