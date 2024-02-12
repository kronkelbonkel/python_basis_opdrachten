# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "de rijn": ["nederland", "duitsland", "Frankrijk"],
    "de maas": ["nederland", "belgië", "duitsland"],
    "de nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

eerste_rivier = rivieren[0]
tweede_land = rivier_info[eerste_rivier][1]

print(f"De rivier {eerste_rivier.capitalize()} stroomt onder andere door {tweede_land.capitalize()}.")

tweede_rivier = rivieren[1]
eerste_land = rivier_info[tweede_rivier][0]

print(f"De rivier {tweede_rivier.capitalize()} stroomt onder andere door {eerste_land.capitalize()}.")

derde_rivier = rivieren[2]
derde_land = rivier_info[derde_rivier][2]

print(f"De rivier {derde_rivier.capitalize()} stroomt onder andere door {derde_land.capitalize()}.")