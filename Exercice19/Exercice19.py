def aryt(a, b, n):
    for i in range(1, n):
        a = a + b
        print(a)

def saisie_entier(message):
    while True:
        try:
            valeur = int(input(message))
            return valeur
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")

# Obtenir la suite des 100 premiers nombres pairs
nombres_pairs = saisie_entier("Entrez le nombre d'éléments pour la suite des nombres pairs : ")
aryt(2, 2, nombres_pairs + 1)

# Obtenir la suite des 100 premiers nombres impairs supérieurs à 10
nombres_impairs = saisie_entier("Entrez le nombre d'éléments pour la suite des nombres impairs (>10) : ")
aryt(11, 2, nombres_impairs + 1)

# Obtenir la suite des 50 premiers multiples de 3 supérieurs à 5678
multiples_de_3 = saisie_entier("Entrez le nombre d'éléments pour la suite des multiples de 3 (>5678) : ")
aryt(5682, 3, multiples_de_3 + 1)