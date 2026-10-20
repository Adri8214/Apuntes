class Trabajo:
    def __init__(self, codigo, cliente, horas, estado="pendiente"):
        self.codigo = str(codigo).strip()
        self.cliente = str(cliente).strip()
        self.horas = float(horas)
        self.estado = str(estado).strip().lower()

    def calcular_importe(self):
        raise NotImplementedError

    def cambiar_estado(self, nuevo_estado):
        nuevo_estado = nuevo_estado.strip().lower()
        estados_validos = ["pendiente", "en curso", "finalizado"]
        if nuevo_estado not in estados_validos:
            return False, "Estado desconocido."
        
        # Validar reglas de transición de estados[cite: 6]
        if self.estado == "pendiente" and nuevo_estado == "finalizado":
            return False, "No se puede pasar directamente de pendiente a finalizado[cite: 6]."
        if self.estado == "en curso" and nuevo_estado == "pendiente":
            return False, "No se puede retroceder de estado[cite: 6]."
        if self.estado == "finalizado":
            return False, "Un trabajo finalizado no puede cambiar de estado."
        if self.estado == nuevo_estado:
            return False, "El trabajo ya se encuentra en ese estado."
            
        self.estado = nuevo_estado
        return True, f"Estado actualizado a '{nuevo_estado}' con éxito."

class Reparacion(Trabajo):
    def __init__(self, codigo, cliente, horas, precio_pieza=0.0, estado="pendiente"):
        super().__init__(codigo, cliente, horas, estado)
        self.precio_pieza = float(precio_pieza)

    def calcular_importe(self):
        # Reparación: horas x 25 € + precio_pieza[cite: 6]
        return (self.horas * 25.0) + self.precio_pieza

class AsistenciaRemota(Trabajo):
    def __init__(self, codigo, cliente, horas, estado="pendiente"):
        super().__init__(codigo, cliente, horas, estado)
        self.precio_pieza = 0.0  # Atributo auxiliar para compatibilidad con CSV

    def calcular_importe(self):
        # Asistencia remota: horas x 20 €[cite: 6]
        return self.horas * 20.0

class ServicioTecnicoGestor:
    def __init__(self):
        self.trabajos = {}  # Diccionario {codigo: Trabajo}

    def alta_trabajo(self, tipo, codigo, cliente, horas, precio_pieza=0.0):
        codigo = codigo.strip()
        cliente = cliente.strip()
        tipo = tipo.strip().lower()

        if not codigo or not cliente:
            return False, "El código y el cliente no pueden estar vacíos[cite: 6]."
        if codigo in self.trabajos:
            return False, "Ya existe un trabajo con ese código[cite: 6]."
        
        try:
            h = float(horas)
            if h <= 0:
                return False, "Las horas deben ser mayores que cero[cite: 6]."
        except ValueError:
            return False, "Las horas deben ser un número válido[cite: 2]."

        if tipo == "reparacion":
            try:
                pp = float(precio_pieza)
                if pp < 0:
                    return False, "El precio de la pieza no puede ser negativo[cite: 6]."
            except ValueError:
                return False, "El precio de la pieza debe ser numérico[cite: 2]."
            
            self.trabajos[codigo] = Reparacion(codigo, cliente, h, pp)
            return True, "Reparación dada de alta con éxito."

        elif tipo == "remota":
            self.trabajos[codigo] = AsistenciaRemota(codigo, cliente, h)
            return True, "Asistencia remota dada de alta con éxito."
        else:
            return False, "Tipo de trabajo desconocido[cite: 6]."

    def cambiar_estado_trabajo(self, codigo, nuevo_estado):
        if codigo not in self.trabajos:
            return False, "El trabajo no existe."
        return self.trabajos[codigo].cambiar_estado(nuevo_estado)

    def buscar_filtrar(self, cliente_filtro="", tipo_filtro="", estado_filtro=""):
        cliente_filtro = cliente_filtro.strip().lower()
        tipo_filtro = tipo_filtro.strip().lower()
        estado_filtro = estado_filtro.strip().lower()

        resultados = []
        for t in self.trabajos.values():
            coincide_cliente = (not cliente_filtro) or (cliente_filtro in t.cliente.lower())
            
            es_reparacion = isinstance(t, Reparacion)
            tipo_str = "reparacion" if es_reparacion else "remota"
            coincide_tipo = (not tipo_filtro) or (tipo_filtro == tipo_str)
            
            coincide_estado = (not estado_filtro) or (estado_filtro == t.estado)

            if coincide_cliente and coincide_tipo and coincide_estado:
                resultados.append((tipo_str, t))
        return resultados

    def obtener_resumen(self):
        conteo_estados = {"pendiente": 0, "en curso": 0, "finalizado": 0}
        importe_total_finalizados = 0.0

        for t in self.trabajos.values():
            if t.estado in conteo_estados:
                conteo_estados[t.estado] += 1
            if t.estado == "finalizado":
                importe_total_finalizados += t.calcular_importe()

        return conteo_estados, importe_total_finalizados