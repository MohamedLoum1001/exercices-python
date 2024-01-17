print("Afficher le cube des (n) premiers entiers naturels non nuls ")
def cube(x):
    return x ** 3
while True:
    try:
        n = int(input("Entrer n : "))
        if n <= 0:
            raise ValueError("Veuillez entrer un entier naturel non nul.")
        print("Le cube des (n) premiers entiers naturels non nuls :")
        for i in range(1, n + 1):
            print(cube(i))
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