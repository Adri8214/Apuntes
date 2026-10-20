class Carta:
    def __init__(self, codigo, nombre, tipo, rareza, valor):
        self.codigo = str(codigo).strip()
        self.nombre = str(nombre).strip()
        self.tipo = str(tipo).strip()
        self.rareza = str(rareza).strip()
        self.valor = float(valor)

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "rareza": self.rareza,
            "valor": self.valor
        }

class Coleccion:
    def __init__(self):
        self.cartas = {}  # Diccionario indexado por código {codigo: Carta}

    def cargar_inicial(self):
        if not self.cartas:
            defecto = [
                Carta("PK01", "Pikachu", "Eléctrico", "Común", 5.0),
                Carta("PK02", "Charizard", "Fuego", "Rara", 30.0),
                Carta("PK03", "Bulbasaur", "Planta", "Común", 4.0)
            ]
            for c in defecto:
                self.cartas[c.codigo] = c

    def alta_carta(self, codigo, nombre, tipo, rareza, valor):
        if not codigo or not nombre:
            return False, "El código y el nombre no pueden estar vacíos[cite: 4]."
        if codigo in self.cartas:
            return False, "El código ya existe en la colección[cite: 4]."
        try:
            val = float(valor)
            if val < 0:
                return False, "El valor de la carta no puede ser negativo[cite: 4]."
        except ValueError:
            return False, "El valor debe ser numérico[cite: 2]."
        
        self.cartas[codigo] = Carta(codigo, nombre, tipo, rareza, val)
        return True, "Carta añadida correctamente."

    def eliminar_carta(self, codigo):
        if codigo not in self.cartas:
            return False, "No existe ninguna carta con ese código en la colección."
        del self.cartas[codigo]
        return True, "Carta eliminada correctamente."

    def buscar_filtrar(self, termino="", rareza_filtro=""):
        resultados = []
        termino = termino.lower()
        rareza_filtro = rareza_filtro.lower()
        for carta in self.cartas.values():
            coincide_termino = (not termino) or (termino in carta.nombre.lower()) or (termino in carta.tipo.lower())
            coincide_rareza = (not rareza_filtro) or (rareza_filtro in carta.rareza.lower())
            if coincide_termino and coincide_rareza:
                resultados.append(carta)
        return resultados

    def intercambiar_carta(self, codigo_antiguo, nuevo_codigo, nuevo_nombre, nuevo_tipo, nueva_rareza, nuevo_valor):
        # Operación atómica: comprueba que la antigua existe y que el código nuevo no está ocupado[cite: 4]
        if codigo_antiguo not in self.cartas:
            return False, "La carta antigua a intercambiar no existe[cite: 4]."
        if nuevo_codigo in self.cartas and nuevo_codigo != codigo_antiguo:
            return False, "El código de la nueva carta ya está ocupado[cite: 4]."
        try:
            val = float(nuevo_valor)
            if val < 0:
                return False, "El valor no puede ser negativo[cite: 4]."
        except ValueError:
            return False, "El valor debe ser numérico[cite: 2]."
        
        # Ejecución atómica segura
        del self.cartas[codigo_antiguo]
        self.cartas[nuevo_codigo] = Carta(nuevo_codigo, nuevo_nombre, nuevo_tipo, nueva_rareza, val)
        return True, "Intercambio realizado con éxito."

    def obtener_estadisticas(self):
        total_cartas = len(self.cartas)
        valor_total = sum(c.valor for c in self.cartas.values())
        conteo_rareza = {}
        for c in self.cartas.values():
            conteo_rareza[c.rareza] = conteo_rareza.get(c.rareza, 0) + 1
        return total_cartas, valor_total, conteo_rareza