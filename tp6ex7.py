input_age = int(input("Entrez votre âge : "))   
def verifier_majorite(age):
    if age >= 18:
        print("majeur")
    else:
        print("mineur")
verifier_majorite(input_age)