class Participante:
    def __init__(self, email, nombre):
        self.email = str(email).strip().lower()
        self.nombre = str(nombre).strip()

    def to_dict(self):
        return {
            "email": self.email,
            "nombre": self.nombre
        }

class Taller:
    def __init__(self, codigo, titulo, plazas):
        self.codigo = str(codigo).strip()
        self.titulo = str(titulo).strip()
        self.plazas = int(plazas)

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "plazas": self.plazas
        }

class Inscripcion:
    def __init__(self, email_participante, codigo_taller):
        self.email_participante = str(email_participante).strip().lower()
        self.codigo_taller = str(codigo_taller).strip()

    def to_dict(self):
        return {
            "email_participante": self.email_participante,
            "codigo_taller": self.codigo_taller
        }

class CentroTalleres:
    def __init__(self):
        self.participantes = {}  # {email: Participante}
        self.talleres = {}       # {codigo: Taller}
        self.inscripciones = []  # Lista de Inscripcion

    def cargar_datos_iniciales(self):
        if not self.talleres:
            talleres_defecto = [
                Taller("TAL01", "Cerámica", 2),
                Taller("TAL02", "Fotografía", 3),
                Taller("TAL03", "Cocina", 4)
            ]
            for t in talleres_defecto:
                self.talleres[t.codigo] = t

    def alta_participante(self, email, nombre):
        email_limpio = email.strip().lower()
        if not email_limpio or not nombre:
            return False, "El email y el nombre no pueden estar vacíos."
        if email_limpio in self.participantes:
            return False, "Ya existe un participante registrado con este correo electrónico[cite: 5]."
        
        self.participantes[email_limpio] = Participante(email_limpio, nombre)
        return True, "Participante dado de alta con éxito."

    def inscribir_participante(self, email, codigo_taller):
        email = email.strip().lower()
        codigo_taller = codigo_taller.strip()

        if email not in self.participantes:
            return False, "El participante no existe[cite: 5]."
        if codigo_taller not in self.talleres:
            return False, "El taller especificado no existe[cite: 5]."

        # Comprobar si ya está inscrito
        for ins in self.inscripciones:
            if ins.email_participante == email and ins.codigo_taller == codigo_taller:
                return False, "El participante ya está inscrito en este taller (inscripción duplicada)[cite: 5]."

        # Comprobar aforo disponible
        taller = self.talleres[codigo_taller]
        inscritos_actuales = sum(1 for ins in self.inscripciones if ins.codigo_taller == codigo_taller)
        
        if inscritos_actuales >= taller.plazas:
            return False, "El taller ya está completo, no quedan plazas disponibles[cite: 5]."

        self.inscripciones.append(Inscripcion(email, codigo_taller))
        return True, "Inscripción realizada con éxito."

    def cancelar_inscripcion(self, email, codigo_taller):
        email = email.strip().lower()
        codigo_taller = codigo_taller.strip()

        encontrada = False
        nuevas_inscripciones = []
        for ins in self.inscripciones:
            if ins.email_participante == email and ins.codigo_taller == codigo_taller:
                encontrada = True
            else:
                nuevas_inscripciones.append(ins)

        if not encontrada:
            return False, "La inscripción especificada no existe (no afecta a otras)[cite: 5]."

        self.inscripciones = nuevas_inscripciones
        return True, "Inscripción cancelada correctamente."

    def consultar_taller(self, codigo_taller):
        if codigo_taller not in self.talleres:
            return None, "El taller no existe."
        
        taller = self.talleres[codigo_taller]
        inscritos_lista = [
            self.participantes[ins.email_participante] 
            for ins in self.inscripciones 
            if ins.codigo_taller == codigo_taller and ins.email_participante in self.participantes
        ]

        total_plazas = taller.plazas
        ocupados = len(inscritos_lista)
        libres = max(0, total_plazas - ocupados)
        porcentaje = (ocupados / total_plazas) * 100 if total_plazas > 0 else 0.0

        return {
            "taller": taller,
            "inscritos": inscritos_lista,
            "plazas_libres": libres,
            "porcentaje_ocupacion": porcentaje
        }, "Consulta correcta."

    def buscar_participante(self, fragmento):
        fragmento = fragmento.lower()
        resultados = []
        for p in self.participantes.values():
            if fragmento in p.nombre.lower() or fragmento in p.email:
                # Buscar talleres a los que está inscrito
                talleres_asistidos = [
                    self.talleres[ins.codigo_taller] 
                    for ins in self.inscripciones 
                    if ins.email_participante == p.email and ins.codigo_taller in self.talleres
                ]
                resultados.append({"participante": p, "talleres": talleres_asistidos})
        return resultados