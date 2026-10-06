import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def maak_deck():
    deck = [(r, s) for r in RANKS for s in SUITS]
    random.shuffle(deck)
    return deck


def kaart_waarde(rank):
    if rank == "A":
        return 11
    if rank in ("J", "Q", "K"):
        return 10
    return int(rank)


def hand_waarde(hand):
    """Telt de hand op; azen tellen als 11, of als 1 als je anders over 21 gaat."""
    totaal = sum(kaart_waarde(r) for r, _ in hand)
    azen = sum(1 for r, _ in hand if r == "A")
    while totaal > 21 and azen:
        totaal -= 10
        azen -= 1
    return totaal


def toon_hand(naam, hand, verberg_tweede=False):
    if verberg_tweede:
        tekst = f"{hand[0][0]}{hand[0][1]}  [?]"
        print(f"{naam}: {tekst}")
    else:
        tekst = "  ".join(f"{r}{s}" for r, s in hand)
        print(f"{naam}: {tekst}  (totaal: {hand_waarde(hand)})")


def trek_kaart(deck):
    if len(deck) < 15:  # opnieuw schudden als het deck bijna op is
        deck.clear()
        deck.extend(maak_deck())
    return deck.pop()


def speel_ronde(deck):
    """Speelt één ronde. Geeft 'blackjack', 'win', 'verlies' of 'gelijk' terug."""
    speler = [trek_kaart(deck), trek_kaart(deck)]
    dealer = [trek_kaart(deck), trek_kaart(deck)]

    print()
    toon_hand("Dealer", dealer, verberg_tweede=True)
    toon_hand("Jij   ", speler)

    # Blackjack direct na het delen
    speler_bj = hand_waarde(speler) == 21
    dealer_bj = hand_waarde(dealer) == 21
    if speler_bj or dealer_bj:
        print()
        toon_hand("Dealer", dealer)
        if speler_bj and dealer_bj:
            print("Beiden blackjack: gelijkspel.")
            return "gelijk"
        if speler_bj:
            print("Blackjack! Je wint.")
            return "blackjack"
        print("Dealer heeft blackjack. Je verliest.")
        return "verlies"

    # Beurt van de speler
    while True:
        keuze = input("\n(h)it of (s)tand? ").strip().lower()
        if keuze == "h":
            speler.append(trek_kaart(deck))
            toon_hand("Jij   ", speler)
            if hand_waarde(speler) > 21:
                print("Bust! Je gaat over 21 en verliest.")
                return "verlies"
            if hand_waarde(speler) == 21:
                print("21! Je blijft automatisch staan.")
                break
        elif keuze == "s":
            break
        else:
            print("Typ 'h' om een kaart te nemen of 's' om te blijven staan.")

    # Beurt van de dealer: trekt tot minimaal 17
    print()
    toon_hand("Dealer", dealer)
    while hand_waarde(dealer) < 17:
        print("Dealer pakt een kaart...")
        dealer.append(trek_kaart(deck))
        toon_hand("Dealer", dealer)

    # Uitslag
    s, d = hand_waarde(speler), hand_waarde(dealer)
    print()
    if d > 21:
        print("Dealer gaat bust. Jij wint!")
        return "win"
    if s > d:
        print(f"Jij wint met {s} tegen {d}!")
        return "win"
    if s < d:
        print(f"Dealer wint met {d} tegen {s}.")
        return "verlies"
    print(f"Gelijkspel: allebei {s}.")
    return "gelijk"


def vraag_inzet(budget):
    while True:
        tekst = input(f"\nBudget: €{budget:.2f}. Hoeveel wil je inzetten? €").replace(",", ".")
        try:
            inzet = float(tekst)
        except ValueError:
            print("Voer een bedrag in, bijvoorbeeld 10 of 12.50.")
            continue
        if inzet <= 0:
            print("De inzet moet groter zijn dan 0.")
        elif inzet > budget:
            print("Je kunt niet meer inzetten dan je budget.")
        else:
            return inzet


def blackjack_spel(total_budget):
    """Speelt blackjack-rondes met inzet tot de speler stopt of het budget op is.
    Geeft (nieuw_budget, actie) terug; actie is 'stop' zodra de speler klaar is."""
    while True:
        if total_budget <= 0:
            return total_budget, "stop"

        deck = maak_deck()
        inzet = vraag_inzet(total_budget)
        uitslag = speel_ronde(deck)

        if uitslag == "blackjack":
            winst = inzet * 1.5
            total_budget += winst
            print(f"Je wint €{winst:.2f}.")
        elif uitslag == "win":
            total_budget += inzet
            print(f"Je wint €{inzet:.2f}.")
        elif uitslag == "verlies":
            total_budget -= inzet
            print(f"Je verliest €{inzet:.2f}.")
        else:
            print("Je krijgt je inzet terug.")

        print(f"Nieuw budget: €{total_budget:.2f}")
        if total_budget <= 0:
            return total_budget, "stop"

        opnieuw = input("\nNog een ronde blackjack? (j/n) ").strip().lower()
        if opnieuw != "j":
            return total_budget, "stop"


def main():
    budget, _ = blackjack_spel(100.0)
    print(f"Eindbudget: €{budget:.2f}")
