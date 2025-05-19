import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def fetch_data(name):
    try:
        response = requests.get(BASE_URL + name.lower())
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return None
