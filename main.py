from datetime import date

from blackjack import blackjack_spel
from roulette import roulette_spel
from fruitmachine import fruitmachine_spel
#from blackjack import blackjack_spel()

REGIS_FEE = 25.00
GAMB_TAX = 18.50
TICKET = 2.50

def welkomst_bericht():
    print("Welkom bij Casino")
    print("1.Profiel aanmaken")
    print("2. Afsluiten")

    keuze = input("Maak je keuze: ")
    if keuze in ("1", "2", "3"):
        return keuze
    print("Maak een juiste keuze")
    return None

welkomst_bericht()

def user_input():
    first_name = input("Wat is uw voornaam? ")
    sur_name = input("Wat is uw achternaam? ")
    birthdate = input("Wat is uw geboortedatum? (dd-mm-yyyy) ")
    gender = input("Wat is uw geslacht? (m/v/x) ").lower()
    return first_name, sur_name, birthdate, gender

def determine_salutation(sur_name, gender):
    if gender == "m":
        return "meneer " + sur_name
    elif gender == "v":
        return "mevrouw " + sur_name
    else:
        return sur_name

def check_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")
    today = date.today()
    age = today.year - int(birth_year)
    if today.month < int(birth_month) or (today.month == int(birth_month) and today.day < int(birth_day)):
        age = age - 1
    return age

def define_start_budget():
    start_budget = float(input("Wat is uw startbudget in €? "))
    total_budget = start_budget - REGIS_FEE - GAMB_TAX - TICKET
    return start_budget, total_budget

def show_welcome_message(start_budget, total_budget, salutation):
    print("Casino de Gouden Driehoek")
    print("-----------------------------")
    print(f"Beste {salutation},\n")
    print(f"Start budget     €{start_budget:.2f}")
    print(f"Inschrijfkosten -€{REGIS_FEE:.2f}")
    print(f"Gok belasting   -€{GAMB_TAX:.2f}")
    print(f"Dagticket       -€{TICKET:.2f}\n")
    print(f"Totaal saldo     €{total_budget:.2f}")
    print("-----------------------------")
    if total_budget <= 0:
        print("Uw speelsaldo is onvoldoende")
    else:
        print("Uw speelsaldo is voldoende")

def hoofdmenu():
    print("1. Spellen")
    print("2. Saldo")
    print("3. Account")

    keuze = input("Maak je keuze: ")
    if keuze in ("1", "2", "3"):
        return keuze
    print("Maak een juiste keuze")
    return None


def show_games_menu():
    print("\nKies een spel:")
    print("1. Roulette")
    print("2. Fruitmachine")
    print("3. Blackjack")
    print("0. Stoppen")

    while True:
        choice = input("Kies een spel: ")
        if choice in ("0", "1", "2", "3"):
            return choice
        print("Kies een juiste keuze")

def toon_saldo(total_budget):
    print(f"Uw saldo is €{total_budget:.2f}")

def toon_account(salutation):
    print(f"Account: {salutation}")

def main():
    first_name, sur_name, birthdate, gender = user_input()
    salutation = determine_salutation(sur_name, gender)
    age = check_age(birthdate)

    if age < 18:
        print(f"Beste {salutation}, je bent helaas te jong om gebruik te maken van deze applicatie.")
        print("Applicatie wordt gesloten.")
        return

    start_budget, total_budget = define_start_budget()
    show_welcome_message(start_budget, total_budget, salutation)

    while True:
        keuze = hoofdmenu()

        if keuze == "0":
            print("Bedankt voor uw bezoek.")
            break

        elif keuze == "1":  # Spellen
            while total_budget > 0:
                spel_keuze = show_games_menu()

                if spel_keuze == "0":
                    break  # terug naar hoofdmenu
                elif spel_keuze == "1":
                    total_budget, actie = roulette_spel(total_budget)
                elif spel_keuze == "2":
                    total_budget, actie = fruitmachine_spel(total_budget)
                elif spel_keuze == "3":
                    total_budget, actie = blackjack_spel(total_budget)

                if total_budget <= 0:
                    print("Uw saldo is op.")
                    break
                if actie == "stop":
                    break

        elif keuze == "2":  # Saldo
            toon_saldo(total_budget)

        elif keuze == "3":  # Account
            toon_account(salutation)

        if total_budget <= 0:
            break

    print(f"Uw eindsaldo is €{total_budget:.2f}")



main()

#        opnieuw = input("Wil je opnieuw naar de roulette? (j/n) ").lower()
#        if opnieuw != "j":
#            break
