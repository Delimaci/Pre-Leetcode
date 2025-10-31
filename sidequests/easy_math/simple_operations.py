firstnum = int(input("What's the first number?"))

secondnum = int(input("What's the second number?"))

operation = input("What operation? \n")

if operation == "+":
  answer = firstnum + secondnum
elif operation == "-":
  answer = firstnum - secondnum
elif operation == "*":
  answer = firstnum * secondnum
elif operation == "/":
  answer = firstnum / secondnum

print(answer)