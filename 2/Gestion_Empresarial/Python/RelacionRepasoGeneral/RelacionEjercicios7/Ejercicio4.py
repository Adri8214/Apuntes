lista = [
    {"nombre": "jabon", "categoria": "aseo", "precio": 2.5, "stock": 50},
    {"nombre": "ordenador", "categoria": "tecnologia", "precio": 250, "stock": 10},
    {"nombre": "botella", "categoria": "hogar", "precio": 4.75, "stock": 100},
    {"nombre": "libreta", "categoria": "papeleria", "precio": 1.4, "stock": 20}
]

disponibles = 0

for producto in lista:
    if producto["stock"] > 0:
        disponibles +=1
        print(f"- {producto['nombre']} (Precio: {producto['precio']}€) - Stock: {producto['stock']}")
print(f"Disponibles: {disponibles}")