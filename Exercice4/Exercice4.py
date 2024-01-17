def demander_nombre(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("ERREUR: Veuillez entrer un nombre.")

# Entrées des dimensions du terrain en mètres avec gestion d'erreur
L = demander_nombre("Entrez la longueur du terrain (en mètres) : ")
l = demander_nombre("Entrez la largeur du terrain (en mètres) : ")

# Calcul de la superficie en mètres carrés
M = L * l

# Conversion en hectares (1 hectare = 10 000 mètres carrés)
H = M / 10000

# Affichage du résultat
print("La superficie du terrain en hectares est :", H, "hectares")
