"""
======================================================================
CHULETARIO MAESTRO SGE - EXAMEN PYTHON (GUÍA DE USO + COMENTARIOS)
======================================================================
ETIQUETAS PARA BUSCAR CON CTRL + F:
- [BUSCAR: BASICO]      -> Bucles (for, while), if/elif, range y enumerate.
- [BUSCAR: TEXTO]       -> Limpiar espacios, mayúsculas/minúsculas, separar cadenas.
- [BUSCAR: FUNCIONES]   -> Parámetros por defecto, return, validación try/except.
- [BUSCAR: CLASE BASICA]-> POO básica, constructores (__init__) y métodos.
- [BUSCAR: CLASE GESTOR]-> ¡NUEVO! Clase que guarda diccionarios de objetos (Ej: Refugio/BiciAlerta).
- [BUSCAR: COMPOSICION] -> Clases que guardan listas de otras clases (Ej: Ventas).
- [BUSCAR: HERENCIA]    -> Clases hijas (super().__init__) y máquinas de estados.
- [BUSCAR: LOGICA]      -> Sets (conjuntos), prioridades (and/or) y diccionarios.
- [BUSCAR: CSV DICT]    -> Leer y escribir diccionarios en CSV (Mini CRM).
- [BUSCAR: CSV OBJETOS] -> Leer y escribir objetos básicos en CSV.
- [BUSCAR: CSV HERENCIA]-> Leer y escribir identificando qué clase hija instanciar.
- [BUSCAR: MENU]        -> El bucle interactivo principal (while opcion != 0).
- [BUCAR: METODO REGISTRAR] -> Evita duplicados al añadir un objeto.
- [BUCAR: METODO LISTAR]    -> Empaqueta el diccionario en una lista plana.
- [BUCAR: METODO ADOPTAR]   -> Cambia estado de un objeto validando su existencia.
- [BUCAR: METODO BUSCAR]    -> Busca coincidencias dobles ignorando mayúsculas.
- [BUCAR: METODO RESUMEN]   -> Recorre el diccionario generando estadísticas.
- [BUCAR: CARGAR CSV]       -> Función cargar_perros_csv.
- [BUCAR: GUARDAR CSV]      -> Función guardar_perros_csv.
======================================================================
"""

import csv  # Módulo obligatorio para leer y escribir archivos .csv[cite: 20]
import os   # Módulo usado para comprobar si un archivo existe con os.path.exists()

# ====================================================================
# [BUSCAR: BASICO] - BUCLES Y CONDICIONALES
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Usa 'elif' en lugar de 'else if' para múltiples condiciones[cite: 16].
- Usa 'enumerate(lista, start=1)' si te piden mostrar un listado numerado (1., 2., 3.)[cite: 16].
- PROHIBIDO usar 'while True' con 'break' para los menús. Usa banderas o condiciones[cite: 14].
"""
def ejemplos_basicos():
    # Condicionales con operadores lógicos (and, or, not)
    stock = 3
    if stock == 0:
        pass
    elif stock < 5:  # Python usa elif, no else if[cite: 16]
        pass
    else:
        pass

    # Bucles For y Enumerate
    productos = ["Teclado", "Ratón", "Monitor"]
    # enumerate saca la posición (i) y el valor (prod) a la vez[cite: 16]
    for i, prod in enumerate(productos, start=1): 
        print(f"{i}. {prod}")

# ====================================================================
# [BUSCAR: TEXTO] - MANIPULACIÓN DE CADENAS (STRINGS)
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- .strip(): Elimina espacios en blanco invisibles al principio y al final[cite: 16]. Úsalo SIEMPRE en los input().
- .lower() / .upper(): Convierte a minúsculas o mayúsculas. Ideal para evitar errores[cite: 16].
- .split(";"): Rompe una frase en una lista usando un separador[cite: 16].
"""
def ejemplos_texto(texto_usuario):
    # Limpieza total para guardar en base de datos o diccionarios[cite: 16]
    limpio = texto_usuario.strip().upper() 
    
    # Comprobar si una palabra está dentro de otra ignorando mayúsculas/minúsculas
    # casefold() es una versión más fuerte y segura que lower()
    if "tecla" in texto_usuario.casefold():
        return True

# ====================================================================
# [BUSCAR: FUNCIONES] - VALIDACIONES Y PARÁMETROS
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Pon parámetros por defecto (ej: porcentaje=0) si el profesor te pide funciones flexibles[cite: 16].
- Usa try/except ValueError en un bucle 'while not' para pedir números de forma segura[cite: 16].
"""
def aplicar_descuento(importe: float, porcentaje: float = 0) -> float:
    # Función con anotaciones de tipo (-> float) y parámetro opcional[cite: 16]
    descuento = importe * porcentaje / 100
    return importe - descuento

def leer_entero(mensaje):
    # Uso de bandera (dato_valido = False) para evitar el while True + break prohibido[cite: 14, 16].
    valido = False
    valor = 0
    while not valido:
        try:
            valor = int(input(mensaje)) # Intenta convertir a entero
            if valor >= 0:
                valido = True           # Si es positivo, cambiamos la bandera y salimos del bucle
            else:
                print("Error: El número no puede ser negativo.")
        except ValueError:              # Captura el error si el usuario escribe letras[cite: 16]
            print("Error: Formato numérico incorrecto.")
    return valor

def leer_flotante(mensaje):
    valido = False
    valor = 0.0
    while not valido:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                valido = True
            else:
                print("Error: El precio no puede ser negativo.")
        except ValueError:
            print("Error: Formato incorrecto. Escribe un valor decimal.")
    return valor

# ====================================================================
# [BUSCAR: CLASE BASICA] - MODELOS DE DATOS (Va en modelos.py)
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- REGLA DE ORO: Ni print() ni input() dentro de las clases. Devuelven True/False o cálculos[cite: 13, 14].
"""
class Producto:
    # __init__ inicializa el objeto. 'self' hace referencia al objeto actual[cite: 16].
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio) # Forzamos que el precio tenga decimales
        self.stock = int(stock)     # Forzamos que el stock sea un número entero

    def reducir_stock(self, cantidad):
        """Resta stock comprobando que sea positivo y haya suficiente."""
        # Operador 'and': ambas condiciones deben cumplirse estrictamente[cite: 14].
        if cantidad > 0 and self.stock >= cantidad:
            self.stock -= cantidad  # Equivalente a: self.stock = self.stock - cantidad
            return True             # Avisamos al main() de que la operación fue un éxito
        return False                # Avisamos al main() de que falló (sin usar print)[cite: 14]

# ====================================================================
# [BUSCAR: COMPOSICION] - CLASES QUE CONTIENEN OTRAS CLASES
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Se usa cuando te piden que un Pedido tenga Líneas, o un Taller tenga Participantes[cite: 13, 14].
- IMPORTANTE: La lista debe inicializarse vacía DENTRO del __init__.
"""
class LineaPedido:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto  # Guardamos el OBJETO ENTERO (con su código, nombre, etc.)
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)

    def subtotal(self):
        # Responsabilidad única: la línea calcula su propio coste multiplicando sus atributos[cite: 13]
        return self.cantidad * self.precio_unitario

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        # IMPORTANTE: Lista vacía inicializada dentro del constructor para que 
        # cada pedido nuevo tenga su propia lista independiente y no se mezclen[cite: 13].
        self.lineas = []  

    def agregar_linea(self, producto, cantidad):
        # 1. Llamamos al método del producto. Si devuelve True, es que había stock y ya se ha restado.
        if producto.reducir_stock(cantidad):
            # 2. Como hay stock, creamos la línea de pedido
            nueva_linea = LineaPedido(producto, cantidad, producto.precio)
            # 3. Guardamos la línea en la lista de este pedido
            self.lineas.append(nueva_linea) 
            return True
        return False # Falló porque reducir_stock devolvió False

    def calcular_total(self):
        # Recorremos la lista de líneas y sumamos lo que devuelva el método subtotal() de cada una[cite: 13]
        return sum(linea.subtotal() for linea in self.lineas)

# ====================================================================
# [BUSCAR: HERENCIA] Y ESTADOS - POO AVANZADA (Proyecto 04)
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- La clase hija hereda poniendo el nombre del padre entre paréntesis: Comercial(Empleado)[cite: 13].
- Llama a super().__init__(...) para inicializar los datos compartidos[cite: 13].
"""
class Trabajo:
    # Parámetro con valor por defecto: si no le pasamos estado, será "pendiente"
    def __init__(self, codigo, cliente, horas, estado="pendiente"):
        self.codigo = codigo
        self.cliente = cliente
        self.horas = float(horas)
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        """Lógica estricta: Impide retroceder o saltarse estados."""
        # Mapeamos los estados a números para saber el orden lógico
        orden = {"pendiente": 1, "en curso": 2, "finalizado": 3}
        # .get() busca la clave, si no existe devuelve 0
        actual = orden.get(self.estado, 0)
        nuevo = orden.get(nuevo_estado, 0)
        
        # Solo cambiamos el estado si el nuevo número es exactamente el siguiente (+1)
        if nuevo == actual + 1:
            self.estado = nuevo_estado
            return True
        return False

class Reparacion(Trabajo):
    # La clase hija (Reparacion) hereda de la clase base (Trabajo)[cite: 13].
    def __init__(self, codigo, cliente, horas, estado, precio_pieza):
        # super() permite reutilizar el constructor de la clase padre[cite: 13].
        super().__init__(codigo, cliente, horas, estado)
        # Inicializamos el atributo exclusivo de esta clase hija
        self.precio_pieza = float(precio_pieza)

    def calcular_importe(self):
        # Regla de negocio matemática exclusiva para Reparaciones
        return (self.horas * 25.0) + self.precio_pieza

class AsistenciaRemota(Trabajo):
    def __init__(self, codigo, cliente, horas, estado):
        # Reutilizamos el constructor padre sin añadir atributos extra[cite: 13]
        super().__init__(codigo, cliente, horas, estado)

    def calcular_importe(self):
        # Regla matemática distinta a Reparacion (Polimorfismo)
        return self.horas * 20.0

# ====================================================================
# [BUSCAR: LOGICA] - COLECCIONES, BÚSQUEDAS Y PRIORIDADES
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Usa set() si te piden sacar categorías o elementos ÚNICOS (sin duplicados)[cite: 15].
- Usa diccionarios {} si necesitas búsquedas ultrarrápidas por código[cite: 15].
"""
def obtener_categorias_unicas(lista_productos):
    """Extrae valores únicos ignorando duplicados usando set()."""
    # Un set evita duplicados automáticamente. Ideal para sacar una lista de categorías[cite: 15].
    return set(prod.categoria for prod in lista_productos)

def es_prioritario(total, es_premium):
    """Operadores and/or para reglas de negocio múltiples."""
    # O se gasta más de 500€, o es premium Y se gasta más de 250€
    return total > 500 or (es_premium and total > 250)

def buscar_por_texto(diccionario_objetos, texto_busqueda):
    """Busca coincidencias exactas o parciales ignorando mayúsculas."""
    encontrados = []
    # .casefold() convierte el texto a minúsculas absolutas para que "hola" coincida con "HOLA"
    busqueda = texto_busqueda.casefold()
    for obj in diccionario_objetos.values():
        if busqueda in obj.nombre.casefold():
            encontrados.append(obj)
    return encontrados

# ====================================================================
# [BUSCAR: CSV DICT] - PERSISTENCIA PARA DICCIONARIOS SIMPLES (Mini CRM)
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Cópialo si el ejercicio NO te pide crear clases, sino guardar una lista de diccionarios[cite: 16].
- Usa newline="" y encoding="utf-8" siempre[cite: 16, 20].
"""
def guardar_crm_csv(lista_clientes):
    # 'w' sobrescribe el archivo. with open() cierra el fichero automáticamente[cite: 16, 20].
    with open("clientes.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "email", "ciudad", "activo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()          # Escribe la primera fila con los nombres de las columnas
        escritor.writerows(lista_clientes) # Vuelca toda la lista de diccionarios de golpe

def cargar_crm_csv():
    clientes = []
    if os.path.exists("clientes.csv"): # Solo leemos si el archivo ya fue creado antes
        with open("clientes.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # El CSV guarda texto plano. Convertimos el texto "True"/"False" a booleano real
                fila["activo"] = fila["activo"].lower() == "true"
                clientes.append(fila)
    return clientes

# ====================================================================
# [BUSCAR: CSV OBJETOS] - PERSISTENCIA PARA CLASES BÁSICAS
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Cópialo cuando tengas que guardar objetos de una clase (ej: Producto, Coche, Cliente).
- Usa try/except ValueError para saltarte las filas que alguien haya roto en el Excel[cite: 16].
"""
def guardar_productos_csv(diccionario_productos):
    with open("productos.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["codigo", "nombre", "precio", "stock"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        
        # Como son Objetos de una Clase, leemos sus atributos uno a uno (prod.codigo, prod.nombre...)
        for prod in diccionario_productos.values():
            escritor.writerow({
                "codigo": prod.codigo, 
                "nombre": prod.nombre, 
                "precio": prod.precio, 
                "stock": prod.stock
            })

def cargar_productos_csv():
    productos = {}
    if os.path.exists("productos.csv"):
        with open("productos.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convertimos forzosamente los tipos. Si falla (ValueError), salta al except[cite: 16].
                    codigo = fila["codigo"]
                    nombre = fila["nombre"]
                    precio = float(fila["precio"])
                    stock = int(fila["stock"])
                    # Instanciamos el objeto y lo guardamos en el diccionario con su código como clave
                    productos[codigo] = Producto(codigo, nombre, precio, stock)
                except ValueError:
                    # Ignoramos esa fila corrupta y seguimos con la siguiente
                    pass
    return productos

# ====================================================================
# [BUSCAR: CSV HERENCIA] - PERSISTENCIA PARA CLASES HIJAS MULTIPLES
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Cópialo si te piden herencia y tienes que guardar TODO en el mismo CSV (ej: Reparaciones y Remotas).
- Consiste en guardar una columna "chivata" ("tipo") para saber qué clase construir al cargar.
"""
def guardar_trabajos_csv(diccionario_trabajos):
    with open("trabajos.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["tipo", "codigo", "cliente", "horas", "estado", "precio_pieza"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for trabajo in diccionario_trabajos.values():
            # isinstance() averigua si el objeto es de la clase hija Reparacion
            if isinstance(trabajo, Reparacion):
                escritor.writerow({
                    "tipo": "Reparacion", # Guardamos una chivata para saber qué es al cargar
                    "codigo": trabajo.codigo, 
                    "cliente": trabajo.cliente, 
                    "horas": trabajo.horas, 
                    "estado": trabajo.estado, 
                    "precio_pieza": trabajo.precio_pieza
                })
            elif isinstance(trabajo, AsistenciaRemota):
                escritor.writerow({
                    "tipo": "Remota", 
                    "codigo": trabajo.codigo, 
                    "cliente": trabajo.cliente, 
                    "horas": trabajo.horas, 
                    "estado": trabajo.estado, 
                    "precio_pieza": 0.0 # Remota no tiene pieza, guardamos 0 por defecto
                })

def cargar_trabajos_csv():
    trabajos = {}
    if os.path.exists("trabajos.csv"):
        with open("trabajos.csv", mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    codigo = fila["codigo"]
                    cliente = fila["cliente"]
                    horas = float(fila["horas"])
                    estado = fila["estado"]
                    
                    # Leemos la "chivata" (columna tipo) para instanciar la clase correcta
                    if fila["tipo"] == "Reparacion":
                        precio_pieza = float(fila["precio_pieza"])
                        trabajos[codigo] = Reparacion(codigo, cliente, horas, estado, precio_pieza)
                    elif fila["tipo"] == "Remota":
                        trabajos[codigo] = AsistenciaRemota(codigo, cliente, horas, estado)
                except ValueError:
                    pass
    return trabajos

# ====================================================================
# [BUSCAR: MENU] - CONTROLADOR PRINCIPAL E INTERFAZ (main.py)
# ====================================================================
"""
CÓMO USAR EN EL EXAMEN:
- Aquí SÍ puedes poner print() e input(). Es el único lugar permitido.
- Usa el while opcion != 0 como pide el profesor[cite: 14].
- Pega el if __name__ == "__main__": al final del todo[cite: 16].
"""
def main():
    # 1. Cargar datos desde los CSV correspondientes al inicio
    catalogo = cargar_productos_csv()
    
    opcion = -1 # Condición inicial para que el while arranque[cite: 16]
    
    # 2. Bucle principal con condición explícita (prohibido while True y break)[cite: 14, 16].
    while opcion != 0:
        print("\n--- MENÚ DEL SISTEMA ---")
        print("1) Listar registros")
        print("2) Añadir nuevo registro")
        print("3) Buscar coincidencia")
        print("4) Guardar datos en CSV")
        print("0) Salir")
        
        # Delegamos el input y la validación a la función leer_entero()
        opcion = leer_entero("Seleccione una opción: ")
        
        # En Python, el "else if" de otros lenguajes se escribe "elif"[cite: 16].
        if opcion == 1:
            if not catalogo:
                print("El sistema está vacío.")
            else:
                # enumerate() genera un contador automático (idx) para mostrar listas numeradas[cite: 16]
                for idx, item in enumerate(catalogo.values(), start=1):
                    # Uso de f-strings {variable} y formateo a 2 decimales {:.2f}
                    print(f"{idx}. [{item.codigo}] {item.nombre} | {item.precio:.2f} EUR")
                    
        elif opcion == 2:
            # .strip() elimina espacios al principio y al final. .upper() lo pone en mayúsculas[cite: 16].
            codigo = input("Código: ").strip().upper()
            if codigo in catalogo:
                print("Error: El código ya existe.")
            else:
                nombre = input("Nombre: ").strip()
                precio = leer_flotante("Precio: ")
                stock = leer_entero("Stock inicial: ")
                # Instanciamos el objeto y lo metemos al diccionario en memoria
                catalogo[codigo] = Producto(codigo, nombre, precio, stock)
                print("Registro guardado en memoria.")
                
        elif opcion == 3:
            texto = input("Introduzca nombre a buscar: ").strip()
            # Llamamos a nuestra función de búsqueda sin case-sensitivity
            resultados = buscar_por_texto(catalogo, texto)
            if not resultados:
                print("No hay coincidencias.")
            else:
                for r in resultados:
                    print(f"Encontrado: {r.nombre} (Stock: {r.stock})")
                    
        elif opcion == 4:
            guardar_productos_csv(catalogo)
            print("Ficheros CSV actualizados.")
            
        elif opcion == 0:
            print("Cerrando el programa...")
        else:
            print("Opción inválida. Intente de nuevo.")
# ====================================================================
# METODO REGISTRAR
# Verifica si el chip ya existe. Si no, guarda el objeto en el diccionario
# y devuelve True. Si ya existe, devuelve False y bloquea la operación.
# ====================================================================
    def registrar(self, perro):
        """Devuelve True si el perro se incorpora; False si ya existía."""
        chip = perro.chip
        # Comprueba si la clave ya existe en el diccionario
        if chip in self.perros:
            return False
        # Si no existe, lo añade
        self.perros[chip] = perro
        return True

# ====================================================================
# METODO LISTAR
# Extrae todos los valores (los objetos Perro) del diccionario y los
# devuelve empaquetados en una lista plana para que el main los imprima.
# ====================================================================
    def listar(self):
        """Devuelve todos los objetos Perro del refugio."""
        return list(self.perros.values())

# ====================================================================
# METODO ADOPTAR
# Busca un perro por su chip usando .get() de forma segura. Si lo encuentra
# y su estado es "REFUGIO", lo cambia a "ADOPTADO" y devuelve True.
# ====================================================================
    def adoptar(self, chip):
        """Cambia REFUGIO a ADOPTADO; False si no puede hacerse."""
        chip = chip.strip().upper()
        # .get() evita que el programa colapse si la clave no existe
        perro = self.perros.get(chip)
        
        # Bloquea si no existe o si ya estaba adoptado
        if perro is None or perro.estado != "REFUGIO":
            return False
            
        perro.estado = "ADOPTADO"
        return True

# ====================================================================
# METODO BUSCAR
# Recorre el diccionario y devuelve una lista con los perros cuyo nombre
# o raza coincida parcialmente con el texto, ignorando mayúsculas.
# ====================================================================
    def buscar(self, texto):
        """Busca texto en el nombre o raza, sin distinguir mayúsculas."""
        texto = texto.strip().casefold()
        if not texto:
            return []
            
        resultados = []
        for perro in self.perros.values():
            if (texto in perro.nombre.casefold() 
                    or texto in perro.raza.casefold()):
                resultados.append(perro)
        return resultados

# ====================================================================
# METODO RESUMEN
# Agrupa los perros por estado para contarlos y suma el peso total
# de los que siguen en el refugio. Devuelve un diccionario con los datos.
# ====================================================================
    def resumen(self):
        """Devuelve las cantidades y el peso total en refugio."""
        en_refugio = 0
        adoptados = 0
        peso_total = 0.0

        for perro in self.perros.values():
            if perro.estado == "REFUGIO":
                en_refugio += 1
                peso_total += perro.peso
            elif perro.estado == "ADOPTADO":
                adoptados += 1

        return {
            "total": len(self.perros),
            "en_refugio": en_refugio,
            "adoptados": adoptados,
            "peso_total_refugio": peso_total,
        }
    # ====================================================================
# NUEVO: PERSISTENCIA CSV PARA PERROS
# ====================================================================
CAMPOS_PERROS = ["chip", "nombre", "raza", "peso", "estado"]

# ====================================================================
# FUNCION CARGAR_PERROS_CSV
# Abre el fichero en modo lectura ("r"). Usa DictReader y valida que 
# las columnas coinciden. Si es correcto, reconstruye cada Perro y lo 
# mete en una lista. Si el archivo no existe, devuelve una lista vacía.
# ====================================================================
def cargar_perros_csv(ruta):
    """Lee perros del CSV, con su peso numérico y su estado."""
    perros_cargados = []
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            
            # Validación de seguridad: Comprueba que el CSV tiene las columnas correctas
            if lector.fieldnames != CAMPOS_PERROS:
                raise ValueError("Las columnas del CSV no tienen el formato esperado")

            for fila in lector:
                # Reconstruimos el objeto fila a fila convirtiendo el peso a número
                p = Perro(
                    fila["chip"],
                    fila["nombre"],
                    fila["raza"],
                    float(fila["peso"]), 
                    fila["estado"]
                )
                perros_cargados.append(p)
    except FileNotFoundError:
        pass # Si el archivo no existe aún, devolvemos la lista vacía
    
    return perros_cargados

# ====================================================================
# FUNCION GUARDAR_PERROS_CSV
# Abre el fichero en modo escritura ("w"). Escribe la fila de cabeceras 
# y luego recorre la lista de perros guardando los datos de cada uno 
# en su columna correspondiente. Devuelve True si acaba con éxito.
# ====================================================================
def guardar_perros_csv(ruta, lista_perros):
    """Escribe cabeceras y perros en el CSV; devuelve True al terminar."""
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PERROS)
            escritor.writeheader()
            
            for perro in lista_perros:
                escritor.writerow({
                    "chip": perro.chip,
                    "nombre": perro.nombre,
                    "raza": perro.raza,
                    "peso": perro.peso,
                    "estado": perro.estado,
                })
        return True
    except Exception:
        return False
    # ====================================================================
# NUEVO: PERSISTENCIA CSV PARA PERROS
# ====================================================================
CAMPOS_PERROS = ["chip", "nombre", "raza", "peso", "estado"]

# ====================================================================
# FUNCION CARGAR CSV
# Abre el fichero en modo lectura ("r"). Usa DictReader y valida que 
# las columnas coinciden. Si es correcto, reconstruye cada Perro y lo 
# mete en una lista. Si el archivo no existe, devuelve una lista vacía.
# ====================================================================
def cargar_perros_csv(ruta):
    """Lee perros del CSV, con su peso numérico y su estado."""
    perros_cargados = []
    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            
            # Validación de seguridad: Comprueba que el CSV tiene las columnas correctas
            if lector.fieldnames != CAMPOS_PERROS:
                raise ValueError("Las columnas del CSV no tienen el formato esperado")

            for fila in lector:
                # Reconstruimos el objeto fila a fila convirtiendo el peso a número
                p = Perro(
                    fila["chip"],
                    fila["nombre"],
                    fila["raza"],
                    float(fila["peso"]), 
                    fila["estado"]
                )
                perros_cargados.append(p)
    except FileNotFoundError:
        pass # Si el archivo no existe aún, devolvemos la lista vacía
    
    return perros_cargados

# ====================================================================
# FUNCION GUARDAR CSV
# Abre el fichero en modo escritura ("w"). Escribe la fila de cabeceras 
# y luego recorre la lista de perros guardando los datos de cada uno 
# en su columna correspondiente. Devuelve True si acaba con éxito.
# ====================================================================
def guardar_perros_csv(ruta, lista_perros):
    """Escribe cabeceras y perros en el CSV; devuelve True al terminar."""
    try:
        with open(ruta, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS_PERROS)
            escritor.writeheader()
            
            for perro in lista_perros:
                escritor.writerow({
                    "chip": perro.chip,
                    "nombre": perro.nombre,
                    "raza": perro.raza,
                    "peso": perro.peso,
                    "estado": perro.estado,
                })
        return True
    except Exception:
        return False
# ====================================================================
# PUNTO DE ENTRADA OBLIGATORIO
# Impide que el código se ejecute accidentalmente al importar el módulo
# ====================================================================
if __name__ == "__main__":
    main()