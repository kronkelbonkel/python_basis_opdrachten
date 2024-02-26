# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(kilometers):
    miles = kilometers / 1.609344
    return miles

def miles_naar_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers

# Voorbeeldgebruik:
kilometers = 1223
miles = 867

miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")
