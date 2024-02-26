# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypteer(tekst):
    encrypted_text = ""
    for karakter in tekst:
        if karakter.isalpha():  # Alleen letters encrypten, laat overige tekens ongewijzigd
            verschoven_code = ord(karakter) + 5
            if karakter.isupper():
                if verschoven_code > ord('Z'):
                    verschoven_code -= 26
            elif karakter.islower():
                if verschoven_code > ord('z'):
                    verschoven_code -= 26
            encrypted_text += chr(verschoven_code)
        else:
            encrypted_text += karakter

    return encrypted_text

def decrypteer(geencrypteerde_tekst):
    decrypted_text = ""
    for karakter in geencrypteerde_tekst:
        if karakter.isalpha():
            verschoven_code = ord(karakter) - 5
            if karakter.isupper():
                if verschoven_code < ord('A'):
                    verschoven_code += 26
            elif karakter.islower():
                if verschoven_code < ord('a'):
                    verschoven_code += 26
            decrypted_text += chr(verschoven_code)
        else:
            decrypted_text += karakter

    return decrypted_text

# Invoer van de gebruiker
te_encrypten_tekst = input("Geef de tekst die je wilt encrypten: ")

# Encryptie
geencrypteerde_tekst = encrypteer(te_encrypten_tekst)
print(f"{geencrypteerde_tekst}")




