from rich.console import Console
from rich.table import Table
from datetime import date
console = Console()

from blackjack import blackjack_spel
from roulette import roulette_spel
from fruitmachine import fruitmachine_spel
from account import start_account_menu

REGIS_FEE = 25.00
GAMB_TAX = 18.50
TICKET = 2.50


def welkomst_bericht():
    table = Table(title="Welkom bij Casino")
    table.add_column("Keuze", justify="center")
    table.add_column("Actie")
    table.add_row("1", "Starten")
    table.add_row("2", "Afsluiten")
    console.print(table)

    keuze = input("Maak je keuze: ")
    if keuze in ("1", "2"):
        return keuze
    console.print("Maak een juiste keuze!")
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
    table = Table(title="Casino de Gouden Driehoek")
    table.add_column("Omschrijving")
    table.add_column("Bedrag", justify="right")
    table.add_row(f"Beste {salutation}", "")
    table.add_row("Startbudget", f"€ {start_budget:.2f}")
    table.add_row("Inschrijfkosten", f"- € {REGIS_FEE:.2f}")
    table.add_row("Gokbelasting", f"- € {GAMB_TAX:.2f}")
    table.add_row("Dagticket", f"- € {TICKET:.2f}")
    table.add_section()
    table.add_row("Totaal saldo", f"€ {total_budget:.2f}")
    if total_budget <= 0:
        table.add_row("Status", "[bold red]Speelsaldo onvoldoende[/bold red]")
    else:
        table.add_row("Status", "[bold green]Speelsaldo voldoende[/bold green]")
    console.print(table)

def hoofdmenu():
    table = Table()
    table.add_column("Hoofdmenu ")
    table.add_row("1. Spellen")
    table.add_row("2. Saldo")
    table.add_row("3. Account")
    console.print(table)

    keuze = input("Maak je keuze: ")
    if keuze in ("1", "2", "3"):
        return keuze
    print("Maak een juiste keuze")
    return None


def show_games_menu():
    table = Table()
    table.add_column("Kies een spel:")
    table.add_row("1. Roulette")
    table.add_row("2. Fruitmachine")
    table.add_row("3. Blackjack")
    table.add_row("0. Stoppen")
    console.print(table)

    while True:
        choice = input("Kies een spel: ")
        if choice in ("0", "1", "2", "3"):
            return choice
        print("Kies een juiste keuze")

def toon_saldo(total_budget):
    print(f"Uw saldo is €{total_budget:.2f}")


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

    account = {
        "voornaam": first_name,
        "achternaam": sur_name,
        "aanspreekvorm": salutation,
        "geboortedatum": birthdate,
        "saldo": total_budget,
    }

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
            account["saldo"] = total_budget
            start_account_menu(account)

        if total_budget <= 0:
            break

    print(f"Uw eindsaldo is €{total_budget:.2f}")



main()

#        opnieuw = input("Wil je opnieuw naar de roulette? (j/n) ").lower()
#        if opnieuw != "j":
#            break
