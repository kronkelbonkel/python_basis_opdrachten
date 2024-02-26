# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]
 
# Vraag de feestgangers om antwoorden
feestganger = {}
for i, vraag in enumerate(vragen, 1):
    antwoord = input(f"{i}. {vraag}\n")
    feestganger[vraag] = antwoord
 
# Schrijf alleen de relevante informatie naar een tekstbestand
with open("feestgangers.txt", "w") as bestand:
    bestand.write(f"Voornaam: {feestganger['Wat is je voornaam?']}\n")
    bestand.write(f"Achternaam: {feestganger['Wat is je achternaam?']}\n")
    bestand.write(f"Drank: {feestganger['Wat neem je mee aan drank?']}\n")
    bestand.write(f'Eten: {feestganger["Wat neem je mee om te eten?"]}\n')
 
print("Bedankt voor het invullen!\nSee you at the party.")