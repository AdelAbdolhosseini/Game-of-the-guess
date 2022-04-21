num1 = input("Please insert the first number: ")
num2 = input("please insert the second number: ")
operation = input("Please insert desired operation amon: + , - , * , / , **: ")
if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    result = float(num1) * float(num2)
elif operation == "**":
    result = float(num1) ** float(num2)
else:
    result = "Unfortunately your operation not exists"

print(result)
