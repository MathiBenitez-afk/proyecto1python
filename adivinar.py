# numeros = [1, 2, 3, 4]
# total = 0
# for n in numeros:
#     total += n
# print(total)

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a & b)

# numero = int(input("ingresa un numero: "))
# if numero % 2 == 0:
#     print("es par")
# else:
#     print("es impar")

# colores = ["rojo", "azul", "rojo", "verde"]
# colores_unicos = set(colores)
# print(f"hay {len(colores_unicos)} colores unicos")

# for numero in range(1, 6):
#     print(numero)

import tkinter as tk
import random

secreto = random.randint(1, 100)
intentos = 0
def adivinar():
    global intentos
    intento = int(entrada.get())
    intentos += 1

    if intento < secreto:
        resultado["text"] = "Muy bajo. Mas alto"
    elif intento > secreto:
        resultado["text"] = "Muy alto. Mas bajo"
    else:
        resultado["text"] = f"Correcto en {intentos}"
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("adivina el numero")

tk.Label(ventana, text="adivina (1-100):").pack()

entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="probar", command=adivinar).pack()

resultado = tk.Label(ventana, text="escribe y pulsa probar")
resultado.pack()
ventana.mainloop()
