while True:
    try:
        # Demander à l'utilisateur d'entrer les valeurs de X et Y
        X = int(input("Entrez la valeur de X : "))
        Y = int(input("Entrez la valeur de Y (Y < X) : "))

        # Vérifier que Y < X
        if Y >= X:
            raise ValueError("Assurez-vous que Y est strictement inférieur à X.")

        # Initialiser le reste à X
        reste = X
        # Utiliser une boucle while pour soustraire Y de reste jusqu'à ce que reste soit inférieur à Y
        while reste >= Y:
            reste -= Y
        # Afficher le résultat
        print(f"Le reste de la division de {X} par {Y} est : {reste}")
        # Sortir de la boucle si tout se déroule correctement
        break

    except ValueError as e:
        print(f"Erreur : {e}. Assurez-vous d'entrer des entiers valides.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
