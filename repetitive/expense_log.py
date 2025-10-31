from datetime import date
item_name = input("What item did you buy?")

item_cost = float(input("How much did the item cost?"))

today_date = date.today()

file = open("expense_tracker.txt", "a")
file.write(f"{today_date} - {item_name} - {item_cost:.2f}\n") 