numeros = -1
contador = -1
subtotal = 0

while numeros != 0:
    numeros = int(input("Introduce un número: "))
    contador+=1
    subtotal+= numeros
print(f"Contador: {contador}\nTotal: {subtotal:.2f}")
