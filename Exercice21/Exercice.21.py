print("Ce programme utilise la fonction nfois pour compter le nombre d'occurrences d'une lettre donnée dans une phrase.")
print('Il prend une phrase et une lettre en entrée,')
print("puis utilise une boucle pour parcourir chaque caractère de la phrase.")
print("")
def freq(phrase, lettre):
    t = len(phrase)
    n = 0
    for i in range(0, t):
        if phrase[i].lower() == lettre.lower():
            n = n + 1
    return n
while True:
    try:
        # Demander à l'utilisateur de saisir une phrase
        p = input("Entrer une phrase : ")
        # Valider la phrase pour s'assurer qu'elle ne contient que des caractères alphabétiques
        if not p or not p.replace(" ", "").isalpha():
            raise ValueError("Veuillez entrer une phrase valide sans chiffres ni caractères spéciaux.")
        # Demander à l'utilisateur de saisir une lettre
        l = input("Entrer une lettre : ")
        # Valider la lettre pour s'assurer qu'elle est unique et alphabétique
        if not l or not l.isalpha() or len(l) != 1:
            raise ValueError("Veuillez entrer une seule lettre valide.")
        # Appeler la fonction freq pour calculer le nombre d'occurrences
        resultat = freq(p, l)
        print(f"La lettre {l} apparaît {resultat} fois dans la phrase.")
        # Sortir de la boucle si tout se déroule correctement
        break
    except ValueError as ve:
        # Gérer l'exception si l'utilisateur entre une valeur incorrecte
        print(f"Erreur : {ve}. Veuillez entrer une valeur valide.")
    except Exception as e:
        # Gérer d'autres exceptions inattendues
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        # Code exécuté à la fin de chaque itération
        print("Fin de l'itération.")
# Code exécuté à la fin, après la sortie de la boucle
print("Fin du programme.")