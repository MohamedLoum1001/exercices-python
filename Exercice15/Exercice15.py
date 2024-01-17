# Boucle pour gérer la saisie correcte des valeurs
while True:
    try:
        # Lecture des valeurs d'entrée depuis l'utilisateur
        capital_initial = int(input("Entrez le capital initial : "))
        interets_annuels = int(input("Entrez les intérêts annuels : "))
        objectif_capital = int(input("Entrez le montant voulu : "))
        # Vérification des valeurs d'entrée
        if capital_initial <= 0 or interets_annuels <= 0 or objectif_capital <= 0:
            raise ValueError("Les valeurs de C, I et V doivent être des entiers positifs.")
        # Calcul du temps nécessaire pour doubler le capital
        N = 0
        while capital_initial < objectif_capital:
            capital_initial += interets_annuels
            N += 1
        # Affichage du résultat
        print("Le capital doublera en {} années.".format(N))

        # Sortie de la boucle si tout se déroule correctement
        break

    except ValueError as e:
        print("Erreur : {}".format(e))
    except Exception as e:
        print("Une erreur inattendue s'est produite : {}".format(e))
