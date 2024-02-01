while True:
    try:
        x, y = input("Fraction: ").split("/")
        if float(x) == int(x) and float(y) == int(y):
            x, y = int(x), int(y)
        if x <= y and x >= 0 and y > 0:
            break
    except ValueError:
        pass

percentage = x / y * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{round(percentage)}%")
