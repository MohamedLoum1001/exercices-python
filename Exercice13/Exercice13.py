while True:
    try:
        # Demander à l'utilisateur d'entrer la valeur de n
        n = int(input("Entrez un entier positif n : "))
        # Vérifier si la valeur de n est positive
        if n < 0:
            raise ValueError("Veuillez entrer un entier positif.")

        # Calculer la somme des n premiers entiers naturels
        S = (n * (n + 1)) // 2

        # Afficher la somme
        print(f"La somme des {n} premiers entiers naturels est : {S}")

        # Sortir de la boucle si tout se déroule correctement
        break
    except ValueError as ve:
        # Gérer l'exception si l'utilisateur entre une valeur incorrecte
        print(f"Erreur : {ve}")
    except Exception as e:
        # Gérer d'autres exceptions inattendues
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        # Code exécuté à la fin de chaque itération
        print("Fin de l'itération.")
# Code exécuté à la fin, après la sortie de la boucle
print("Fin du programme.")
