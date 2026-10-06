import random
def roulette_spel(total_budget):
    actie = "menu"
    print("\nKies één van de volgende opties:")
    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stoppen")

    while True:
        choice = input("Maak je keuze: ")
        if choice == "0":
            print("Bedankt voor het spelen.")
            break
        elif choice == "1":
            print("Je hebt Rood gekozen")
        elif choice == "2":
            print("Je hebt Zwart gekozen")
        elif choice == "3":
            print("Je hebt Even gekozen")
        elif choice == "4":
            print("Je hebt Oneven gekozen")
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

        spin = random.randint(0, 36)

        if spin % 2 == 0:
            odd_even = "even"
        else:
            odd_even = "oneven"

        if spin <= 18:
            if odd_even == "even":
                color = "zwart"
            else:
                color = "rood"
        else:
            if odd_even == "even":
                color = "rood"
            else:
                color = "zwart"

        print("De roulette draait...")
        print(f"De roulette komt uit op: ({spin}) {color}")

        win = False

        if choice == "1" and color == "rood":
            win = True
        elif choice == "2" and color == "zwart":
            win = True
        elif choice == "3" and odd_even == "even":
            win = True
        elif choice == "4" and odd_even == "oneven":
            win = True

        if win:
            total_budget += bet
            print(f"Gefeliciteerd! Je wint €{bet:.2f}!")
        else:
            total_budget -= bet
            print(f"Helaas, je verliest je inzet van €{bet:.2f}.")

        print(f"Je saldo is nu: €{total_budget:.2f}")

        if total_budget <= 0:
            print("Je saldo is op.")
            actie = "stop"
            break

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