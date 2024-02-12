# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

ingevoerde_kazen = input("Voer minimaal 5 kazen in, gescheiden door komma's: ").split(", ")

# Sorteer de lijst in omgekeerde volgorde, rekening houdend met de z
gesorteerde_kazen = sorted(ingevoerde_kazen, key=lambda x: (x.lower()[0] != 'z', x), reverse=True)

# Print de gesorteerde lijst
print(gesorteerde_kazen)