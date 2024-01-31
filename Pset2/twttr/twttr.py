text = input("Input: ")
vowels = "aAeEiIoOuU"

for char in text:
    if char in vowels:
        text = text.replace(char, "")

print(text)
