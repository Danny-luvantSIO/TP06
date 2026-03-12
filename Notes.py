Note_input = input("Entrez Une note ")
Note = int(Note_input)
if Note < 10:
    print("Ajourné")
elif 10 <= Note < 12:
    print("Passable")
elif 12 <= Note < 14:
    print("Assez Bien")
elif 14 <= Note < 16:
    print("Bien")
else:
    print("Très bien")
