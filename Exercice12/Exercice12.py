while True:
    try:
        # Demander à l'utilisateur d'entrer le capital initial, les intérêts annuels et le nombre d'années
        C = int(input("Entrez le capital initial : "))
        I = int(input("Entrez les intérêts annuels : "))
        N = int(input("Entrez le nombre d'années : "))
        # Vérifier si les valeurs saisies sont négatives, si oui, lever une exception ValueError
        if C < 0 or I < 0 or N < 0:
            raise ValueError("Les valeurs ne peuvent pas être négatives.")
        # Calculer le capital après N années en ajoutant les intérêts chaque année
        for k in range(1, N + 1):
            C += I  # Le capital augmente de I chaque année
        # Afficher le capital après N années
        print("Le capital après", N, "années est de", C)
        # Sortir de la boucle si tout se déroule correctement
        break
    except ValueError as ve:
        # Gérer l'exception ValueError (valeurs négatives)
        print(f"Erreur : {ve}. Assurez-vous d'entrer des valeurs valides.")
    except Exception as e:
        # Gérer d'autres exceptions inattendues
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        # Code exécuté à la fin de chaque itération
        print("Fin de l'itération.")
# Code exécuté à la fin, après la sortie de la boucle
print("Fin du programme.")