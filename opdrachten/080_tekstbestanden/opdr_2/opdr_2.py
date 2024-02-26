# Opdracht 2 tekstbestanden
# Naam student:
# Groep:


import random

def raad_een_nummertje():
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0

    print("Raad mijn geheime getal tussen 1 en 100")

    while True:
        gebruikers_gok = int(input())

        aantal_pogingen += 1

        if gebruikers_gok < geheim_getal:
            print("hoger")
        elif gebruikers_gok > geheim_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden, het is {geheim_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer gedaan")
            break

# Uitvoeren van het spel
raad_een_nummertje()

