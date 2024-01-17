print("Fonctions :")
print("")
def f(x):
    return 2 * x - 4
def saisie_utilisateur():
    while True:
        try:
            # Demander à l'utilisateur d'entrer la valeur de x
            x = float(input("Entrez une valeur pour x : "))
            # Calculer la valeur de la fonction pour x
            resultat = f(x)
            # Afficher le résultat
            print("f({}) = {}".format(x, resultat))
            # Sortir de la boucle si tout se déroule correctement
            break
        except ValueError:
            # Gérer l'exception si l'utilisateur entre une valeur incorrecte
            print("Erreur : Veuillez entrer une valeur numérique valide.")
        except Exception as e:
            # Gérer d'autres exceptions inattendues
            print("Une erreur inattendue s'est produite : {}".format(e))
        finally:
            # Code exécuté à la fin de chaque itération
            print("Fin de l'itération.")
# Appeler la fonction de saisie_utilisateur
saisie_utilisateur()
# Code exécuté à la fin, après la sortie de la boucle
print("Fin du programme.")
