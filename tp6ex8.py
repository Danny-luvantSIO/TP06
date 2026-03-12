def tarif(age):
    if age < 12:
        print("enfant")
    elif age >= 12 and age <= 17:
        print("adolescent")
    elif age >= 18 and age <= 64:
        print("adulte")
    else:
        print("senior")
tarif(6)
tarif(15)
tarif(30)
tarif(70)