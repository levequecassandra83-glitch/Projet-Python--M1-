import time  # on importe la bibliothèque time


# --- Le quiz ---
score = 0

print("=== Quiz Histoire ===")

print("Début !")
time.sleep(2)  # on attend 2 secondes
print("2 secondes ont passé !")
print("")

def poser_question(question, bonne_reponse):
    print(question)
    reponse = input("Ta réponse : ")
    
    if reponse == bonne_reponse:
        print("✓ Bravo !")
        return 1
    else:
        print("✗ Raté ! C'était :", bonne_reponse)
        return 0

# Toutes les questions dans une liste
questions = [
    ("Question 1 : En quelle année a eu lieu la Révolution française ?", "1789"),
    ("Question 2 : Qui était la femme de Napoléon ?", "Joséphine"),
    ("Question 3 : Qui a dit 'Veni, vidi, vici' ?", "César"),
    ("Question 4 : En quelle année Christophe Colomb arrive en Amérique ?", "1492"),
    ("Question 5 : Dans quel région de France a eu lieu le débarquement du 6 juin 1944?", "Normandie"),
    ("Question 6 : Quelle couleur était le cheval d'Henri IV ?", "gris"),
]

# On parcourt toutes les questions avec une boucle
score = 0
print("=== Quiz Histoire ===")
print("")

for question, reponse in questions:
    score = score + poser_question(question, reponse)
    print("")

# Résultat
print("=== Résultat ===")
print("Tu as eu", score, "bonne(s) réponse(s) sur", len(questions), "!")

if score == len(questions):
    print("Parfait, t'es une historienne née !")
elif score >= 2:
    print("Très bien, encore un effort !")
else:
    print("Retourne réviser tes cours 😄")