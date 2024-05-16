import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()
    quote = data[0]['q'] + " - " + data[0]['a']
    return quote

def main():
    print("Welcome to Inspirational Quotes Generator!")
    while True:
        input("Press Enter to get an inspirational quote or type 'exit' to quit: ")
        quote = get_quote()
        print(quote)
        choice = input("Do you want another quote? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
