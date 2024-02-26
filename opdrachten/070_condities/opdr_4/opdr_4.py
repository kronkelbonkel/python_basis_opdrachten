# Opdracht 4 condities
# Naam student:
# Groep:


# Hier de rest van jouw code...
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

def kies_topping():
    while True:
        print(f"Maak een keuze uit onze toppings: {beschikbare_toppings}")
        gekozen_topping = input()

        for topping, prijs in toppings:
            if gekozen_topping.lower() == topping.lower():
                print(f"U heeft {topping} besteld. Dat kost {prijs}")
                return prijs

        print("Uw keuze zit niet in ons assortiment. Probeer opnieuw.")

gekozen_prijs = kies_topping()



