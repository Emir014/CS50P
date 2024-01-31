camelCase = input("camelCase: ")
snake_case = ""

for char in camelCase:
    if char.isupper():
        char = "_" + char.lower()
    snake_case += char

print(snake_case)
