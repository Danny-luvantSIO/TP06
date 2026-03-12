def calculateur(nombre1, nombre2, operateur):
    if operateur == "addition":
        resultat = nombre1 + nombre2
    elif operateur == "soustraction":
        resultat = nombre1 - nombre2
    elif operateur == "multiplication":
        resultat = nombre1 * nombre2
    elif operateur == "division":
        if nombre2 != 0:
            resultat = nombre1 / nombre2
        else:
            print("Erreur : division par zéro")
            return
    else:
        print("Opération inconnue")
        return
    
    print("Résultat :", resultat)
calculateur(10, 5, "addition")       
calculateur(10, 5, "soustraction")    
calculateur(10, 5, "multiplication")  
calculateur(10, 5, "division") 