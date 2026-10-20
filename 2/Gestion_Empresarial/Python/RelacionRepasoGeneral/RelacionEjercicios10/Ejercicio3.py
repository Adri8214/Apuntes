class Cliente:
    def __init__(self, nombre, email, ciudad):
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad

    def cambiar_ciudad(self, nueva_ciudad):
        self.ciudad = nueva_ciudad

    def ficha(self):
        return f"Nombre: {self.nombre} | Email: {self.email} | Ciudad: {self.ciudad}"

cliente1 = Cliente("Antonio", "antoniojg@gmail.com", "Granada")
cliente2 = Cliente("Manueh", "mannu23@gmail.com", "Cordoba")

cliente1.cambiar_ciudad("Málaga")

print(cliente1.ficha())
print(cliente2.ficha())