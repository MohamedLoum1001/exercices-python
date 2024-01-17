def calculer_annees_depassement(prix_moyen, objectif):
    annees = 0

    while prix_moyen <= objectif:
        prix_moyen *= 1.08  # Augmentation de 8%
        annees += 1

    return annees

while True:
    try:
        # Lecture des données
        prix_moyen_initial = 7.0
        objectif_prix = float(input("Entrez le montant objectif de location en euros : "))

        # Appel de la fonction
        resultat = calculer_annees_depassement(prix_moyen_initial, objectif_prix)

        # Affichage du résultat
        print(f"Le prix moyen de location dépassera {objectif_prix} euros au bout de {resultat} années.")
        break  # Sortir de la boucle si tout se passe bien
    except ValueError:
        print("Veuillez entrer un montant valide en euros.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
