import requests
from termcolor import cprint

def get_random_quote():
    url = "https://api.quotable.io/quotes/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        cprint("[ INFO ] Error bij het ophalen van de quote, API is mogelijk offline.", response.status_code, 'white')
        return None

def print_quote(quote_data):
    if quote_data:
        for q in quote_data:
            cprint(f'"{q["content"]}"\n', 'white')
            cprint(f"- {q['author']}\n", 'white')

def quote():
    quote_data = get_random_quote()
    print_quote(quote_data)

# If quotes_api.py is executed directly, call the quote function
if __name__ == "__main__":
    quote()
