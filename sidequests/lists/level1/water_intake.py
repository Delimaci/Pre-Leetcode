glasses_of_water = input("How many glasses of water you drank each day, separated by spaces: \n")

glasses = glasses_of_water.split()
total = 0
for i in range(len(glasses)):
  glasses[i] = int(glasses[i])
  total = glasses[i] + total
  print(glasses[i])


print(f"The total amount of water is: {total}")