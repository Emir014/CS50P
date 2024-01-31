def main():
    price = 50

    while price > 0:
        cents = get_valid_input(price)
        price -= cents
    print(f"Change Owed: {-price}")

def get_valid_input(price):
    while True:
        print(f"Amount Due: {price}")
        cents = int(input("Insert Coin: "))
        if cents in [5, 10, 25]:
            return cents

if __name__ == "__main__":
    main()
