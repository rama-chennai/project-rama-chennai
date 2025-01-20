import requests

def fetch_books(search_query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={search_query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("items", [])
    else:
        print("Error fetching data:", response.status_code)
        return []
