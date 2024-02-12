# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Lisanne", "Paul", "Kees", "Marie", "Hilda" ]
mooier_opgemaakt = f"De gasten {', '.join(gasten[:-1])} en {gasten[-1]} gaan samen uit eten."
print(mooier_opgemaakt)

gasten.remove("Marie")
mooier_opgemaakt = f"De gasten {', '.join(gasten[:-1])} en {gasten[-1]} gaan samen uit eten."

print(mooier_opgemaakt)

index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, ("George"))
mooier_opgemaakt = f"De gasten {', '.join(gasten[:-1])} en {gasten[-1]} gaan samen uit eten."

print(mooier_opgemaakt)