print("BIENVENIDO AL ZOO DE NARNIA \n")

edad = int(input("Cuantos años tienes? "))
print("Aceptamos varios tipos de carnet: \n Pulsa [E] para ESTUDIANTE \n Pulsa [P] para PENSIONISTA \n Pulsa [F] para "
      "FAMILIA NUMEROSA \n Pulsa [N] para NO CARNET")

t_carnet = input("Que carnet tiene [*] ")

# Comprobación ESTUDIANTE

if edad >= 25 and edad <= 35:

    if t_carnet == "E" or t_carnet == "F":
        print("Se le aplica el descuento")
    elif t_carnet != "E":
        print("Te falta el carnet de estudiate :(")
    if t_carnet == "P":
        print("Espera... de donde has sacado ese caret? ")

# Comprobación PENSIONISTA

if edad >= 65:

    if t_carnet == "P" or t_carnet == "F":
        print("Se le aplica el descuento")
    elif t_carnet != "P":
        print("Te falta el carnet de pensionista :(")
    if t_carnet == "E":
        print("Espera... de donde has sacado ese caret? ")

# Comprobación INFANTIL

if edad <= 10:
    print("Se te aplica el descuento infantil")

# Comprobación FAMILIA NUMEROSA + 35 - 65 años

if 35 < edad < 65 and t_carnet == "F":
    print("Se te aplica el descuento Familia numerosa")
