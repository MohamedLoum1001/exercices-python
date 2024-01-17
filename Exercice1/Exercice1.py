print("Exécution de la première séquence")
# État de mémoire initial
x = 2
y = -2
z = -4
s = 1
t = 3

# Exécution de la première séquence
z = x + y
t = z * t
x = -t
s = 3 * x
y = 8

# Nouvel état de mémoire
nouvel_etat = {'x': x, 'y': y, 'z': z, 's': s, 't': t}
print(nouvel_etat)
print('')

#---------2em Programme---------
print("Exécution de la deuxième séquence")
# État de mémoire initial
x = 2
y = -2
z = -4
s = 1
t = 3

# Exécution de la deuxième séquence
t = -y
z = t ** 2
x = z - x
t = x

# Nouvel état de mémoire
nouvel_etat = {'x': x, 'y': y, 'z': z, 's': s, 't': t}
print(nouvel_etat)
