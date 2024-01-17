print(" Et/ou :")
reponse = input("répondre oui ou non: ")
if reponse == "oui" or reponse == "non":
    print("La réponse est", reponse)
    if len(reponse) == 3:
        print("La réponse a trois caractères, mais n'est pas correcte.")
else:
    print("C'est une mauvaise réponse")
