items = []
while True:
    try:
        item = input().upper()
        items.append(item)
    except EOFError:
        for item in sorted(set(items)):
            print(f"{items.count(item)} {item}")
        break
