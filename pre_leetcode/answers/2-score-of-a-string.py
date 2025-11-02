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

# DUNGEON 5

string = input("Enter a string: ")

ascii_sum = 0

for i in range(len(string)):
  ascii_sum += ord(string[i])
print(ascii_sum)


# DUNGEON 6

string = input("Enter a string: ")

ascii_sum = 0
for i in range(len(string)):
  ascii_sum += ord(string[i])
average = ascii_sum / len(string)
print(average)

# DUNGEON 7

string = input("Enter a string at least 2 chars long: ")

differences = []

for i in range(len(string) - 1):
  adif = abs(ord(string[i]) - ord(string[i + 1]))
  differences.append(adif)
print(differences)

#DUNGEON 8


string = input("Enter a string")

vowel_count = 0

for i in range(len(string)):
  if string[i] in "aeiou":
    vowel_count = vowel_count + 1
print(vowel_count)

# DUNGEON 9

string = input("Enter a string: ")

halfway_point = len(string) // 2
partial_score = 0

for i in range( halfway_point - 1):
  partial_score += abs(ord(string[i]) - ord(string[i + 1]))

print(partial_score)

# DUNGEON 10

score = 0
for i in range(len(s) - 1):
      score += abs(ord(s[i]) - ord(s[i + 1]))
print(score)
