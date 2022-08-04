print("Welcome to the Calculator")

while True:
    print("Please enter the first number: ")
    first = input()

    print("Would you like to Add, Subtract, Multiply or Divide? ")
    symbol = input()

    print("What is the second number? ")
    second = input()

    if symbol == "Add":
        solution = int(first) + int(second)
        symbol = "+"
    elif symbol == "Subtract":
        solution = int(first) - int(second)
        symbol = "-"
    elif symbol == "Multiply":
        solution = int(first) * int(second)
        symbol = "*"
    elif symbol == "Divide":
        solution = int(first) / int(second)
        symbol = "/"

    print(f"The solution to {first} {symbol} {second} = {solution}")

    print("Would you like to calculate something else? y/n")
    again = input()

    if again == "n":
        break
