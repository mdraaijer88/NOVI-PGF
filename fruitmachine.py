import random

def fruitmachine_spel(total_budget):
    actie = "menu"
    symbolen = ["kers", "citroen", "ster"]

    print("\nKies één van de volgende opties:")
    print("1. Draai")
    print("0. Stoppen")

    while True:
        choice = input("Maak je keuze: ")
        if choice == "0":
            print("Bedankt voor het spelen.")
            break
        elif choice == "1":
            print("Je hebt draaien gekozen")
        else:
            print("Kies een juiste keuze")
            continue

        bet = float(input("Wat is je inzet? "))
        if bet <= 0:
            print("Kies een geldig bedrag...")
            continue
        elif bet > total_budget:
            print(f"U heeft niet genoeg saldo, saldo is €{total_budget:.2f}")
            continue
        print(f"€{bet:.2f} is je inzet!")

        spin = random.choice(symbolen)

        rol1 = random.choice(symbolen)
        rol2 = random.choice(symbolen)
        rol3 = random.choice(symbolen)

        print("De fruitmachine draait...")
        print(f"Uitkomst: {rol1} | {rol2} | {rol3}")

        if rol1 == rol2 == rol3 == "ster":
            winst = bet * 10
            total_budget += winst
            print(f"JACKPOT! Drie sterren! Je wint €{winst:.2f}!")

        elif rol1 == rol2 == rol3:
            winst = bet * 5
            total_budget += winst
            print(f"Drie gelijke symbolen! Je wint €{winst:.2f}!")

        elif rol1 == rol2 or rol2 == rol3 or rol1 == rol3:
            winst = bet * 2
            total_budget += winst
            print(f"Twee gelijke symbolen! Je wint €{winst:.2f}!")
        else:
            total_budget -= bet
            print(f"Helaas, geen match. Je verliest je inzet van €{bet:.2f}.")

        print(f"Je saldo is nu: €{total_budget:.2f}")

        again = input("Wil je nog een keer spelen? (j/n) ").lower()
        if again == "n":
            while True:
                vervolg = input("1. Terug naar hoofdmenu\n2. Stoppen\nUw keuze: ")
                if vervolg == "1":
                    actie = "menu"
                    break
                elif vervolg == "2":
                    print("Bedankt voor het spelen.")
                    actie = "stop"
                    break
                else:
                    print("Kies een juiste keuze")
            break

    return total_budget, actie
#TODO keuze draaien nog veranderen.
