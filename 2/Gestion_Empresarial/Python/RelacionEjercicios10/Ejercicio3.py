class Cliente:
    def __init__(self, nombre, email, ciudad):
        self.nombre = nombre
        self.email = email
        self.ciudad = ciudad

    def cambiar_ciudad(self, nueva_ciudad):
        if self.ciudad != nueva_ciudad:
            self.ciudad = nueva_ciudad
            return f"La ciudad se ha cambiado a {self.ciudad}"
    
    def ficha(self):
        return f"Nombre: {self.nombre} | Email: {self.ciudad} | Ciudad: {self.ciudad}"

cliente = Cliente("Alberto", "alberto@gmail.com", "Granada")
print("Antes:", cliente.ficha())
resultado = cliente.cambiar_ciudad("Malaga")
print("Despues:", cliente.ficha())

