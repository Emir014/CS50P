#One liner
#print(round(float(eval(input("Expression: "))), 1))

expression = input("Expression: ")
x, y, z = expression.split()
x, z = float(x), float(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z
    case _:
        print("Invalid operator")
        exit(1)

print(round(result, 1))
