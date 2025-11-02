#DUNGEON 1

char = input("Enter a single character: ")
print(ord(char))


#DUNGEON 2
string = input("Enter a short string: \n")

for c in range(len(string)):
  print(ord(string[c]))

  
# DUNGEON 3

string = input("Enter a string at least 2 characters long: \n")

for i in range(len(string) -1):
  value = ord(string[i])
  difference =  abs(ord(string[i]) - ord(string[i + 1]))
  print(f"{string[i]} and {string[i+1]} difference: {difference}") 

  #OR

  string = input("Enter a string at least 2 characters long: ")

for i in range(len(string)- 1):
  difference = abs(ord(string[i]) - ord(string[i +1]))
  print(f"difference between {string[i]} and {string[i +1]}: {difference}")


# DUNGEON 4


string = input("Enter a string at least 2 characters long: ")

total_score = 0

for i in range(len(string) -1 ):
  total_score += abs(ord(string[i]) - ord(string[i + 1]) )
print(f"total score: {total_score}")

