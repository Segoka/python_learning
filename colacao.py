print("*****Preparación de Colacao******")

leche = input("Primero de todo.... tienes leche? [s/n] ")
colacao = input("Y... tienes colacao? [s/n] ")

if leche == "s" and colacao == "s":
    print("Perfecto!! Pon la leche en un vaso luego el colacao y a disfrutar :)")

elif leche != "s" and colacao == "s":
    print("Te falta la leche para poder hacerlo :(")
    print("Te lo apunto en la lista de la compra ")

elif leche == "s" and colacao != "s":
    print("Te falta colacao :(")
    print("Te lo apunto en la lista de la compra ")

else:
    print("¡¡¡¡¡¡No tienes nada!!!!!")
    print("No puedes hacer el colacao")

