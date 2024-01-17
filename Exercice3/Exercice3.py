# L'algorithme lit la chaîne "algorithme" et effectue les opérations suivantes :

# D prend la valeur du neuvième caractère de C (ici, 'e')
# E prend la valeur du premier caractère de C (ici, 'a')
# F prend la valeur du septième caractère de C (ici, 'i')
# G prend la valeur du huitième caractère de C (ici, 'm')
# S prend la somme de D, E, F et G (ici, 'e' + 'a' + 'i' + 'm')

# Entrée de la chaîne de caractères C
C = input("Entrez une chaîne de caractères : ")

# Récupération des caractères spécifiés
D = C[8] if len(C) >= 9 else ''  # Valeur du neuvième caractère
E = C[0]  # Valeur du premier caractère
F = C[6] if len(C) >= 7 else ''  # Valeur du septième caractère
G = C[7] if len(C) >= 8 else ''  # Valeur du huitième caractère

# Calcul de la somme
S = D + E + F + G

# Affichage du résultat
print("La somme des caractéres (D), (E), (F) et (G) est : ", S)
