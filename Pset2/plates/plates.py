def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for char in s:
        if not s.isalnum():
            return False

    if not s[:2].isalpha():
        return False

    if not 2 <= len(s) <= 6:
        return False

    if len(s) > 2:
        for char in s[2:]:
            if char.isdigit():
                if not s[s.index(char):].isdigit() or char == "0":
                    return False
                break #check the above condition only for the first number in s

    return True

if __name__ == "__main__":
    main()
