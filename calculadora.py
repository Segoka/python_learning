option = int(input("1 para Calculadora de Farenheit a Celsius [*] 2 para calculadora Libras a Euros "))

if option == 1 or option == 2:
    print("Ejecutando calculadora: ")

    if option == 1:
        tfarenheit = float(input("Dime la temperatura en grados Farenheit: "))
        tcelsius = ((tfarenheit - 32) * 5 / 9)
        print("La temperatura en celsius es de " + str(tcelsius) + "grados")
    if option == 2:
        libras = float(input("Cuantas libras tienes: "))
        euros = libras * 1.2
        print("Tienes " + str(euros) + "euros")

else:
    print("Introduce una opción valida")
