# Opdracht 1 functies
# Naam student:
# Groep:



def write_to_file(bestandsnaam, tekst):
    try:
        with open(bestandsnaam, "a") as bestand:
            bestand.write(tekst + "\n")
        print(f"Tekst is succesvol toegevoegd aan {bestandsnaam}.")
    except Exception as e:
        print(f"Fout bij schrijven naar bestand: {e}")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
