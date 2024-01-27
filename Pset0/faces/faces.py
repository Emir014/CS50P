def main():
    text = input("Enter your message: ")
    print(convert(text))

def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

if __name__ == "__main__":
    main()
