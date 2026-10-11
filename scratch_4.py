

def voeg_account_toe(account):
    voornaam = input("Wat is je voornaam? ")
    achternaam = input("Wat is je achternaam? ")
    aanspreekvorm = input("Wat is je aanspreekvorm? ")
    geboortedatum = input("Wat is je geboortedatum? ")
    saldo = 0.00

    account['Accounts'].append({
        "naam": voornaam,
        "achternaam": achternaam,
        "aanspreekvorm": aanspreekvorm,
        "geboortedatum": geboortedatum,
    })
    sla_op(data)
    print("\nFiets toegevoegd en opgeslagen!\n")