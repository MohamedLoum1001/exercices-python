def g(a, b, x):
    return a * x + b
def inverse_f(y):
    if a == 0:
        raise ValueError("La fonction inverse n'est pas définie pour a égal à zéro.")
    return (y - 7) / -2
while True:
    try:
        # Demander à l'utilisateur d'entrer les valeurs de a, b, et x
        a = float(input("Entrez la valeur de a : "))
        b = float(input("Entrez la valeur de b : "))
        x = float(input("Entrez la valeur de x : "))
        # Vérifier si les valeurs saisies sont valides
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(x, (int, float)):
            raise ValueError("Veuillez entrer des valeurs numériques valides.")
        # Calculer et afficher le résultat de la fonction g
        resultat_g = g(a, b, x)
        print(f"Le résultat de la fonction g({a}, {b}, {x}) est : {resultat_g}")
        # Utiliser la fonction inverse_f pour trouver x lorsque g(x) = 5
        x_associated_with_5 = inverse_f(5)
        print("La valeur de x associée à g(x) = 5 est :", x_associated_with_5)
        # Sortir de la boucle si tout se déroule correctement
        break
    except ValueError as ve:
        # Gérer l'exception si l'utilisateur entre une valeur incorrecte
        print(f"Erreur : {ve}. Veuillez entrer des valeurs valides.")
    except Exception as e:
        # Gérer d'autres exceptions inattendues
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        # Code exécuté à la fin de chaque itération
        print("Fin de l'itération.")
# Code exécuté à la fin, après la sortie de la boucle
print("Fin du programme.")
