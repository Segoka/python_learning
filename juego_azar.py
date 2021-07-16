import time
import webbrowser
import random

print("Bienbenido al juego de azar... Vamos a comprobar tu lodopatía jejejeje")
print("Tienes números del 0 al 20 para adivinar, si lo haciertas te llevarás una sorpresa 7w7 ")

n = int(99)
n_ganador = random.randint(0, 20)

while n != n_ganador:
    n = int(input("Dime tu numerito "))
    print("Prueba otra vez! \n")

print("Me has ganado... toma tu recompensa...")

time.sleep(2)
webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
