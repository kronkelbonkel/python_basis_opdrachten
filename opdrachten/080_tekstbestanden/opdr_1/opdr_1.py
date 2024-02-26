# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

def vul_enquete_in():
    antwoorden = []


    antwoord1 = input("Wat vind je van de huidige regering? ")
    antwoorden.append(f"Vraag 1: {antwoord1}\n")

    antwoord2 = input("Wat vind je van de Python-lessen tot nu toe? ")
    antwoorden.append(f"Vraag 2: {antwoord2}\n")

    antwoord3 = input("Wat vind jij de mooiste stad van Nederland? ")
    antwoorden.append(f"Vraag 3: {antwoord3}\n")

    with open("enquete_resultaten.txt", "w") as bestand:
        bestand.writelines(antwoorden)

    print("Bedankt voor het invullen van de enquête. De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")

vul_enquete_in()