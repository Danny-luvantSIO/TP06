def connexion():
    identifiant_attendu = "root"
    mot_de_passe_attendu = "!!_Ca_C_pYthon_**"
    
    login = input("Entrez l'identifiant : ")
    mdp = input("Entrez le mot de passe : ")
    
    if login != identifiant_attendu:
        print("Identifiant incorrect")
    elif mdp != mot_de_passe_attendu:
        print("Mot de passe incorrect")
    else:
        print("Connexion réussie")
connexion()