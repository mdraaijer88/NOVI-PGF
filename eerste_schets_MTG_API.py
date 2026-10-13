import requests
from rich.console import Console
from rich.table import Table
from datetime import date

console = Console()

url = "https://api.scryfall.com/cards/search"

parameters = {
    "q": "m:1WR t:creature kw:flying"
}

#TODO in menu functie maken waar je een kaart kan zoeken op naam...
#zoek exact "exact" : "Black Lotus"
#zoek op woord in titel :    "q": "o:black"
# m:2WW
# aantal = Aantal wat je wil laten zoeken
# for card in result['naam'][:aantal]:

headers = {
    "User-Agent": "MTG_app/1.0",
    "Accept": "application/json"
}

response = requests.get(
    url,
    params=parameters,
    headers=headers
)

result = response.json()
aantal = 10
if response.status_code == 200:
    for card in result["data"][:aantal]:
        print("Naam:", card["name"])
        print("Mana cost:", card.get("mana_cost", "Geen mana cost"))
        print("Type:", card["type_line"])
        print("Kaarttekst:", card.get("oracle_text", "Geen kaarttekst"))
        print("------------------------------")
else:
    print("Er is een fout opgetreden:")
    print(result.get("details", "Onbekende fout"))