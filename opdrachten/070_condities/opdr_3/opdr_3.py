# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

leeftijdsgroep = None
for groep, leeftijdsgrenzen in leeftijd.items():
    if leeftijdsgrenzen[0] <= leeftijd_input <= leeftijdsgrenzen[1]:
        leeftijdsgroep = groep
        break

korting_percentage = kortings_percentages.get(leeftijdsgroep, 0)

korting_bedrag = (korting_percentage / 100) * normale_toegangsprijs
te_betalen_bedrag = normale_toegangsprijs - korting_bedrag

print(f"U behoort tot de groep {leeftijdsgroep}")
print(f"U krijgt {korting_percentage}% korting")
print(f"U betaalt daarom {te_betalen_bedrag:.2f}")
