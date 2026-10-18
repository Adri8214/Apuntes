importe = float(input("Introduce el importe: "))
total = 0
contador = 0
while importe != 0:

    contador +=1
    total += importe
    importe = float(input("Introduce el importe: "))

print(f"Se han introducido una cantidad de {contador} importes\nTotal: {total:.2f}")