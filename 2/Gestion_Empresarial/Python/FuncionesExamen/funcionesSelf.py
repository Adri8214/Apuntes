def cambiar_ciudad(self, nueva_ciudad):
        if self.ciudad != nueva_ciudad:
            self.ciudad = nueva_ciudad
            return f"La ciudad se ha cambiado a {self.ciudad}"
        return f"La ciudad ya era {self.ciudad}"

def agregar_linea(self, linea):
    self.lineas.append(linea)

def registrar(self, bicicleta):
        """Devuelve True si la bicicleta se incorpora; False si ya existía."""
        codigo = bicicleta.codigo
        if codigo in self.bicicletas:
            return False
        self.bicicletas[codigo] = bicicleta
        return True

def listar(self):
        """Devuelve todos los objetos Bicicleta del registro."""
        return list(self.bicicletas.values())

def recuperar(self, codigo):
        """Cambia ROBADA a RECUPERADA; False si no puede hacerse."""
        codigo = codigo.strip().upper()
        bicicleta = self.bicicletas.get(codigo)
        if bicicleta is None or bicicleta.estado != "ROBADA":
            return False
        bicicleta.estado = "RECUPERADA"
        return True

def buscar(self, texto):
        """Busca texto en el propietario o el modelo, sin distinguir mayúsculas."""
        texto = texto.strip().casefold()
        if not texto:
            return []
        resultados = []
        for bicicleta in self.bicicletas.values():
            if (texto in bicicleta.propietario.casefold()
                    or texto in bicicleta.modelo.casefold()):
                resultados.append(bicicleta)
        return resultados

def resumen(self):
    """Devuelve las cantidades y el valor pendiente de las robadas."""
    robadas = 0
    recuperadas = 0
    valor_pendiente = 0.0

    for bicicleta in self.bicicletas.values():
        if bicicleta.estado == "ROBADA":
            robadas += 1
            valor_pendiente += bicicleta.valor
        elif bicicleta.estado == "RECUPERADA":
            recuperadas += 1

    return {
        "total": len(self.bicicletas),
        "robadas": robadas,
        "recuperadas": recuperadas,
        "valor_pendiente": valor_pendiente,
    }

def anadir(self, carta):
        """Devuelve "OK" o "DUPLICADO"."""
        if carta.codigo in self.cartas:
            return "DUPLICADO"
        self.cartas[carta.codigo] = carta
        return "OK"
 
def eliminar(self, codigo):
    """True si la carta existía y se ha eliminado."""
    return self.cartas.pop(str(codigo).strip().upper(), None) is not None

def alta_participante(self, participante):
        """Devuelve "OK" o "DUPLICADO" (email repetido)."""
        if participante.email in self.participantes:
            return "DUPLICADO"
        self.participantes[participante.email] = participante
        return "OK"

def buscar_inscripcion(self, email, codigo):
        for inscripcion in self.inscripciones:
            if inscripcion.email_participante == email and inscripcion.codigo_taller == codigo:
                return inscripcion
        return None

def porcentaje_ocupacion(self, codigo):
        """Porcentaje de plazas ocupadas, o None si el taller no existe."""
        inscritos = self.inscritos_taller(codigo)
        if inscritos is None:
            return None
        taller = self.talleres[str(codigo).strip().upper()]
        return len(inscritos) * 100 / taller.plazas

def plazas_libres(self, codigo):
    """Plazas sin ocupar, o None si el taller no existe."""
    inscritos = self.inscritos_taller(codigo)
    if inscritos is None:
        return None
    return self.talleres[str(codigo).strip().upper()].plazas - len(inscritos)

def eliminar_perro(self, chip):
    """Elimina un perro del registro usando su chip. Devuelve True si existía y se borró, o False si no."""
    chip = chip.strip().upper()
    if chip in self.perros:
        del self.perros[chip]
        return True
    return False

def filtrar_por_edad(self, edad_maxima):
    """Devuelve una lista con los perros cuya edad sea menor o igual a la indicada."""
    resultados = []
    for perro in self.perros.values():
        if perro.edad <= edad_maxima:
            resultados.append(perro)
    return resultados