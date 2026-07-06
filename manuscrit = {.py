import random

anecdotes = {
    "Moyen Age": [
        "Les Vikings n'avaient pas de cornes sur leurs casques, c'est un mythe !",
        "Au Moyen Age, on se mariait souvent dès 12 ans.",
        "Les cathédrales gothiques mettaient parfois 200 ans à être construites.",
    ],
    "Antiquité": [
        "Cléopâtre vivait plus près de nous que de la construction des pyramides.",
        "Les Romains utilisaient du garum, une sauce de poisson fermenté, sur tout !",
        "Alexandre le Grand avait les yeux de deux couleurs différentes.",
    ],
    "Epoque moderne": [
        "Louis XIV se lavait environ 3 fois par an seulement.",
        "Napoléon mesurait 1m69, dans la moyenne de l'époque.",
        "Marie Curie a reçu deux Prix Nobel dans deux sciences différentes.",
    ],
    "Epoque contemporaine": [
        "La première guerre mondiale a duré 4 ans, de 1914 à 1918.",
        "Le mur de Berlin est tombé en 1989.",
        "La Seconde Guerre mondiale a fait plus de 60 millions de morts.",
    ],
}

print("=== Anecdotes historiques ===")
print("")
continuer = "oui"
while continuer == "oui":

    print("")
choix = input("Quelle catégorie tu veux ? : ")

if choix in anecdotes:
    anecdote = random.choice(anecdotes[choix])
    print("")
    print("Le saviez-vous ?")
    print(anecdote)
else:
    print("Cette catégorie n'existe pas !")
