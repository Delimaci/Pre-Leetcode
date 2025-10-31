storenumbers = input("Enter numbers separated by spaces \n")

items = storenumbers.split()


print("Here are your items converted to integers:")
for i in range(len(items)):
  items[i] = int(items[i])
  print(items[i])