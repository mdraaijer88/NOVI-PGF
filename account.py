# bekijken
# toevoegen
# wisselen
# verwijderen

def account_menu():
    print("1. Bekijk account")
    print("2. Voeg account toe")
    print("3. Wissel account")
    print("4. Verwijder account")
    print("5. Terug naar hoofdmenu")
    return input("Maak uw keuze: ")


def toon_account(account):
    print("")
    print(f"Naam:           {account['voornaam']} {account['achternaam']}")
    print(f"Aanspreekvorm:  {account['aanspreekvorm']}")
    print(f"Geboortedatum:  {account['geboortedatum']}")
    print(f"Saldo:          €{account['saldo']:.2f}")

def maak_account():
    voornaam = input("Wat is je voornaam? ")
    achternaam = input("Wat is je achternaam? ")
    aanspreekvorm = input("Wat is je aanspreekvorm? ")
    geboortedatum = input("Wat is je geboortedatum? ")
    saldo = 0.00

    account = {
        "voornaam": voornaam,
        "achternaam": achternaam,
        "aanspreekvorm": aanspreekvorm,
        "geboortedatum": geboortedatum,
        "saldo": saldo
    }

    return account

def start_account_menu(account):
    while True:
        keuze = account_menu()
        if keuze == "1":
            toon_account(account)
        elif keuze == "2":
            maak_account(account)
        elif keuze == "3":
            print("Account wisselen...")
        elif keuze == "4":
            print("Account verwijderen...")
        elif keuze == "5":
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")



start_account_menu({
    "voornaam": "Test", "achternaam": "Speler",
    "aanspreekvorm": "meneer Speler",
    "geboortedatum": "01-01-1990", "saldo": 100.0,
})

account = {
        "voornaam": "Jan",
        "achternaam": "Jansen",
        "aanspreekvorm": "Dhr.",
        "geboortedatum": "15-05-1990",
        "saldo": 125.5
    }