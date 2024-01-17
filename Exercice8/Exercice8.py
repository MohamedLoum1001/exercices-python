print("Instruction conditionnelle :")
# Étape 1 : Lire X (X est un entier)
X = int(input("Entrez un entier X : "))

# Étape 2 : Instruction conditionnelle
if X % 9 == 0:
    Y = X / 9
else:
    Y = X - 9

# Étape 3 : Afficher Y
print("La valeur de (Y) est :", Y)
