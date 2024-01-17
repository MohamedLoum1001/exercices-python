print("Cet algorithme en Python prend en compte le tarif groupe si le nombre de personnes")
print("est supérieur ou égal à 5 et affiche le prix par personne en conséquence.")
print("")
# Étape 1 : Lire N (N est un entier)
N = int(input("Entrez le nombre de personnes dans le groupe : "))

# Étape 2 : Instruction conditionnelle
if N >= 5:
    P = 170  # Tarif groupe par personne
else:
    P = (700 + 210 * N) / N  # Prix total / Nombre de personnes

# Étape 3 : Afficher P
print("Le prix par personne est de", P, "euros.")
