"""BIBLIOTECA DE MÉTODOS CON SELF · TEMÁTICA CANINA
====================================================================
Recopilación de TODOS los métodos válidos de los exámenes y proyectos
trabajados (BiciAlerta, CanAlerta, PatitasAdopta, Tienda canina y los
proyectos 02, 03 y 04 del repaso final) adaptados a perros, más métodos
EXTRA que pueden servir en otros ejercicios.

Etiquetas en cada docstring:
    [EXAMEN] -> el método (o su idea) apareció en un examen/ejercicio.
    [EXTRA]  -> añadido como ampliación.

REGLAS que cumple todo el archivo (las del enunciado):
    * Ningún método imprime ni pide datos: devuelven valores, booleanos,
      listas, diccionarios o códigos de estado ("OK", "DUPLICADO"...).
    * Primero se VALIDA y después se MODIFICA: una operación inválida
      nunca deja cambios parciales.
    * Solo biblioteca estándar. print()/input() únicamente en main().

ÍNDICE
    0. Helpers privados de validación
    1. PerroPerdido / RegistroPerdidos      (BiciAlerta y CanAlerta)
    2. Perro / Protectora                   (PatitasAdopta)
    3. Producto / LineaVenta / Venta / Tienda (Tienda canina, proyecto 01)
    4. CartaRaza / ColeccionRazas           (proyecto 02: cartas e intercambios)
    5. Participante / Taller / Inscripcion / EscuelaCanina (proyecto 03)
    6. ServicioCanino / Peluqueria / Teleconsulta / GestorServicios
                                            (proyecto 04: herencia)

Ejecuta `python metodos_con_self.py` para lanzar las comprobaciones.
"""
import math


# =====================================================================
# 0. HELPERS PRIVADOS DE VALIDACIÓN (lanzan ValueError si algo es inválido)
# =====================================================================
def _texto(valor, nombre):
    """Texto no vacío (sin espacios sobrantes)."""
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{nombre} no puede estar vacío")
    return valor.strip()


def _entero(valor, nombre, minimo=None, maximo=None):
    """Entero real: rechaza bool, 3.5, 'abc'. Acepta '4', 4 y 4.0."""
    if isinstance(valor, bool):
        raise ValueError(f"{nombre} debe ser un número entero")
    if isinstance(valor, float):
        if not valor.is_integer():
            raise ValueError(f"{nombre} debe ser un número entero")
        valor = int(valor)
    else:
        try:
            valor = int(valor)
        except (TypeError, ValueError):
            raise ValueError(f"{nombre} debe ser un número entero") from None
    if minimo is not None and valor < minimo:
        raise ValueError(f"{nombre} debe ser como mínimo {minimo}")
    if maximo is not None and valor > maximo:
        raise ValueError(f"{nombre} debe ser como máximo {maximo}")
    return valor


def _decimal(valor, nombre, minimo=None, estricto=False):
    """Número finito. Acepta coma decimal ('3,5'). Rechaza nan e inf.

    minimo + estricto=True  -> valor > minimo
    minimo + estricto=False -> valor >= minimo
    """
    if isinstance(valor, bool):
        raise ValueError(f"{nombre} debe ser numérico")
    if isinstance(valor, str):
        valor = valor.strip().replace(",", ".")
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{nombre} debe ser numérico") from None
    if not math.isfinite(numero):
        raise ValueError(f"{nombre} debe ser un número finito")
    if minimo is not None:
        if estricto and numero <= minimo:
            raise ValueError(f"{nombre} debe ser mayor que {minimo:g}")
        if not estricto and numero < minimo:
            raise ValueError(f"{nombre} debe ser como mínimo {minimo:g}")
    return numero


def _estado(valor, permitidos, nombre="El estado"):
    """Estado normalizado en mayúsculas que debe estar en `permitidos`."""
    if not isinstance(valor, str) or valor.strip().upper() not in permitidos:
        raise ValueError(f"{nombre} no es válido")
    return valor.strip().upper()


def _clave(valor):
    """Normaliza un código para usarlo como clave de diccionario."""
    return str(valor).strip().upper()


def _email(valor):
    """Email sencillo normalizado en minúsculas."""
    if not isinstance(valor, str):
        raise ValueError("El email no es válido")
    valor = valor.strip().lower()
    usuario, arroba, dominio = valor.partition("@")
    if (not usuario or arroba != "@" or "@" in dominio or " " in valor
            or "." not in dominio.strip(".")):
        raise ValueError("El email no es válido")
    return valor


# =====================================================================
# 1. PERRO PERDIDO / REGISTRO  (BiciAlerta -> CanAlerta)
# =====================================================================
class PerroPerdido:
    """Aviso de un perro perdido. Estados: PERDIDO / ENCONTRADO."""

    ESTADOS = ("PERDIDO", "ENCONTRADO")

    def __init__(self, codigo, propietario, raza, recompensa, estado="PERDIDO"):
        self.codigo = _texto(codigo, "El código").upper()
        self.propietario = _texto(propietario, "El propietario")
        self.raza = _texto(raza, "La raza")
        self.recompensa = _decimal(recompensa, "La recompensa", minimo=0, estricto=True)
        self.estado = _estado(estado, self.ESTADOS)

    def esta_perdido(self):
        """[EXTRA] True si sigue perdido."""
        return self.estado == "PERDIDO"

    def marcar_encontrado(self):
        """[EXAMEN] PERDIDO -> ENCONTRADO. False si ya estaba encontrado."""
        if self.estado != "PERDIDO":
            return False
        self.estado = "ENCONTRADO"
        return True

    def cambiar_recompensa(self, nueva):
        """[EXTRA] Cambia la recompensa solo si sigue perdido y el valor es válido."""
        if not self.esta_perdido():
            return False
        try:
            self.recompensa = _decimal(nueva, "La recompensa", minimo=0, estricto=True)
        except ValueError:
            return False
        return True

    def a_fila(self):
        """[EXTRA] Diccionario listo para csv.DictWriter."""
        return {"codigo": self.codigo, "propietario": self.propietario,
                "raza": self.raza, "recompensa": self.recompensa, "estado": self.estado}

    def __str__(self):
        return (f"{self.codigo} | {self.propietario} | {self.raza} | "
                f"{self.recompensa:.2f} € | {self.estado}")


class RegistroPerdidos:
    """Diccionario codigo -> PerroPerdido."""

    def __init__(self):
        self.perros = {}

    def registrar(self, perro):
        """[EXAMEN] True si se incorpora; False si el código ya existía."""
        if perro.codigo in self.perros:
            return False
        self.perros[perro.codigo] = perro
        return True

    def listar(self):
        """[EXAMEN] Copia de la lista de perros (no expone el diccionario)."""
        return list(self.perros.values())

    def obtener(self, codigo):
        """[EXTRA] El perro con ese código, o None."""
        return self.perros.get(_clave(codigo))

    def encontrar(self, codigo):
        """[EXAMEN] Marca como ENCONTRADO. False si no existe o ya lo estaba."""
        perro = self.obtener(codigo)
        if perro is None:
            return False
        return perro.marcar_encontrado()

    def eliminar(self, codigo):
        """[EXAMEN] True si existía y se ha eliminado."""
        return self.perros.pop(_clave(codigo), None) is not None

    def buscar(self, texto):
        """[EXAMEN] Fragmento en propietario o raza, sin distinguir mayúsculas."""
        texto = str(texto).strip().casefold()
        if not texto:
            return []
        return [p for p in self.perros.values()
                if texto in p.propietario.casefold() or texto in p.raza.casefold()]

    def filtrar_por_estado(self, estado):
        """[EXTRA] Perros con el estado indicado (PERDIDO / ENCONTRADO)."""
        estado = str(estado).strip().upper()
        return [p for p in self.perros.values() if p.estado == estado]

    def resumen(self):
        """[EXAMEN] Totales y recompensa pendiente (suma de los todavía perdidos)."""
        perdidos = 0
        encontrados = 0
        pendiente = 0.0
        for perro in self.perros.values():
            if perro.estado == "PERDIDO":
                perdidos += 1
                pendiente += perro.recompensa
            elif perro.estado == "ENCONTRADO":
                encontrados += 1
        return {"total": len(self.perros), "perdidos": perdidos,
                "encontrados": encontrados, "recompensa_pendiente": pendiente}

    def top_recompensas(self, n=3):
        """[EXTRA] Los n perros perdidos con mayor recompensa."""
        if n <= 0:
            return []
        perdidos = self.filtrar_por_estado("PERDIDO")
        return sorted(perdidos, key=lambda p: (-p.recompensa, p.codigo))[:n]

    def recompensa_media_pendiente(self):
        """[EXTRA] Media de recompensa de los perdidos (0.0 si no hay ninguno)."""
        perdidos = self.filtrar_por_estado("PERDIDO")
        if not perdidos:
            return 0.0
        return sum(p.recompensa for p in perdidos) / len(perdidos)


# =====================================================================
# 2. PERRO / PROTECTORA  (PatitasAdopta)
# =====================================================================
class Perro:
    """Perro de una protectora. Estados: DISPONIBLE / ADOPTADO."""

    ESTADOS = ("DISPONIBLE", "ADOPTADO")

    def __init__(self, codigo, nombre, raza, edad, peso, estado="DISPONIBLE"):
        self.codigo = _texto(codigo, "El código").upper()
        self.nombre = _texto(nombre, "El nombre")
        self.raza = _texto(raza, "La raza")
        self.edad = _entero(edad, "La edad", minimo=0, maximo=30)
        self.peso = _decimal(peso, "El peso", minimo=0, estricto=True)
        self.estado = _estado(estado, self.ESTADOS)

    def esta_disponible(self):
        """[EXTRA]"""
        return self.estado == "DISPONIBLE"

    def adoptar(self):
        """[EXAMEN] DISPONIBLE -> ADOPTADO. False si no estaba disponible."""
        if self.estado != "DISPONIBLE":
            return False
        self.estado = "ADOPTADO"
        return True

    def devolver(self):
        """[EXTRA] ADOPTADO -> DISPONIBLE (devolución a la protectora)."""
        if self.estado != "ADOPTADO":
            return False
        self.estado = "DISPONIBLE"
        return True

    def etapa_vida(self):
        """[EXTRA] CACHORRO (<1 año), ADULTO (<8) o SENIOR."""
        if self.edad < 1:
            return "CACHORRO"
        if self.edad < 8:
            return "ADULTO"
        return "SENIOR"

    def categoria_peso(self):
        """[EXTRA] PEQUEÑO (<10 kg), MEDIANO (<25), GRANDE (<45) o GIGANTE."""
        if self.peso < 10:
            return "PEQUEÑO"
        if self.peso < 25:
            return "MEDIANO"
        if self.peso < 45:
            return "GRANDE"
        return "GIGANTE"

    def a_fila(self):
        """[EXTRA] Diccionario listo para csv.DictWriter."""
        return {"codigo": self.codigo, "nombre": self.nombre, "raza": self.raza,
                "edad": self.edad, "peso": self.peso, "estado": self.estado}

    def __str__(self):
        return (f"{self.codigo} | {self.nombre} | {self.raza} | "
                f"{self.edad} años | {self.peso:.1f} kg | {self.estado}")


class Protectora:
    """Diccionario codigo -> Perro."""

    def __init__(self):
        self.perros = {}

    def registrar(self, perro):
        """[EXAMEN] True si ingresa; False si el código ya existía."""
        if perro.codigo in self.perros:
            return False
        self.perros[perro.codigo] = perro
        return True

    def listar(self):
        """[EXAMEN]"""
        return list(self.perros.values())

    def obtener(self, codigo):
        """[EXTRA]"""
        return self.perros.get(_clave(codigo))

    def adoptar(self, codigo):
        """[EXAMEN] DISPONIBLE -> ADOPTADO. False si no existe o ya adoptado."""
        perro = self.obtener(codigo)
        if perro is None:
            return False
        return perro.adoptar()

    def devolver(self, codigo):
        """[EXTRA] ADOPTADO -> DISPONIBLE."""
        perro = self.obtener(codigo)
        if perro is None:
            return False
        return perro.devolver()

    def dar_de_baja(self, codigo):
        """[EXAMEN] True si existía y se ha eliminado (dict.pop con valor por defecto)."""
        return self.perros.pop(_clave(codigo), None) is not None

    def disponibles_por_edad(self):
        """[EXAMEN] DISPONIBLES de menor a mayor edad (a igual edad, por nombre)."""
        disponibles = [p for p in self.perros.values() if p.estado == "DISPONIBLE"]
        return sorted(disponibles, key=lambda p: (p.edad, p.nombre.casefold()))

    def buscar(self, texto):
        """[EXTRA] Fragmento en nombre o raza, sin distinguir mayúsculas."""
        texto = str(texto).strip().casefold()
        if not texto:
            return []
        return [p for p in self.perros.values()
                if texto in p.nombre.casefold() or texto in p.raza.casefold()]

    def filtrar_por_raza(self, raza):
        """[EXTRA] Perros de esa raza exacta (sin distinguir mayúsculas)."""
        raza = str(raza).strip().casefold()
        return [p for p in self.perros.values() if p.raza.casefold() == raza]

    def filtrar_por_peso(self, minimo, maximo):
        """[EXTRA] Perros con minimo <= peso <= maximo."""
        return [p for p in self.perros.values() if minimo <= p.peso <= maximo]

    def agrupar_por_raza(self):
        """[EXTRA] Diccionario raza (en minúsculas) -> lista de perros."""
        grupos = {}
        for perro in self.perros.values():
            grupos.setdefault(perro.raza.casefold(), []).append(perro)
        return grupos

    def contar_por_raza(self):
        """[EXTRA] Diccionario raza (en minúsculas) -> cantidad."""
        return {raza: len(lista) for raza, lista in self.agrupar_por_raza().items()}

    def edad_media(self):
        """[EXTRA] Edad media de todos los perros (0.0 si no hay ninguno)."""
        if not self.perros:
            return 0.0
        return sum(p.edad for p in self.perros.values()) / len(self.perros)

    def estadisticas(self):
        """[EXAMEN] Cantidades, peso medio de los disponibles y perro más pesado."""
        disponibles = 0
        adoptados = 0
        suma_peso = 0.0
        mas_pesado = None
        for perro in self.perros.values():
            if perro.estado == "DISPONIBLE":
                disponibles += 1
                suma_peso += perro.peso
            elif perro.estado == "ADOPTADO":
                adoptados += 1
            if mas_pesado is None or perro.peso > mas_pesado.peso:
                mas_pesado = perro
        peso_medio = suma_peso / disponibles if disponibles else 0.0  # evita /0
        return {"total": len(self.perros), "disponibles": disponibles,
                "adoptados": adoptados, "peso_medio_disponibles": peso_medio,
                "mas_pesado": mas_pesado}


# =====================================================================
# 3. TIENDA CANINA  (proyecto 01: inventario y ventas)
# =====================================================================
class Producto:
    """Producto de la tienda canina."""

    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = _texto(codigo, "El código").upper()
        self.nombre = _texto(nombre, "El nombre")
        self.categoria = _texto(categoria, "La categoría")
        self.precio = _decimal(precio, "El precio", minimo=0, estricto=True)
        self.stock = _entero(stock, "El stock", minimo=0)

    def reponer(self, cantidad):
        """[EXAMEN] Suma unidades. False (sin cambios) si la cantidad no es válida."""
        try:
            cantidad = _entero(cantidad, "La cantidad", minimo=1)
        except ValueError:
            return False
        self.stock += cantidad
        return True

    def descontar(self, cantidad):
        """[EXAMEN] Resta unidades. False (sin cambios) si no es válida o no hay stock."""
        try:
            cantidad = _entero(cantidad, "La cantidad", minimo=1)
        except ValueError:
            return False
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True

    def esta_agotado(self):
        """[EXTRA]"""
        return self.stock == 0

    def valor_en_stock(self):
        """[EXTRA] precio x unidades en almacén."""
        return round(self.precio * self.stock, 2)

    def a_fila(self):
        """[EXTRA]"""
        return {"codigo": self.codigo, "nombre": self.nombre, "categoria": self.categoria,
                "precio": self.precio, "stock": self.stock}


class LineaVenta:
    """Línea de una venta; conserva el precio en el momento de la operación."""

    def __init__(self, producto, cantidad, precio_unitario):
        if not isinstance(producto, Producto):
            raise ValueError("La línea necesita un producto válido")
        self.producto = producto
        self.cantidad = _entero(cantidad, "La cantidad", minimo=1)
        self.precio_unitario = _decimal(precio_unitario, "El precio unitario",
                                        minimo=0, estricto=True)

    def importe(self):
        """[EXAMEN] cantidad x precio_unitario."""
        return round(self.cantidad * self.precio_unitario, 2)


class Venta:
    """Venta con varias líneas. El descuento se aplica al TOTAL, nunca por línea."""

    UMBRAL_DESCUENTO = 50.0
    PORCENTAJE_DESCUENTO = 0.10

    def __init__(self, numero, cliente):
        self.numero = _entero(numero, "El número de venta", minimo=1)
        self.cliente = _texto(cliente, "El cliente")
        self.lineas = []

    def agregar_linea(self, producto, cantidad, precio_unitario=None):
        """[EXAMEN] Añade una línea; si ya hay una del mismo producto y precio, suma."""
        if not isinstance(producto, Producto):
            raise ValueError("La línea necesita un producto válido")
        if precio_unitario is None:
            precio_unitario = producto.precio
        nueva = LineaVenta(producto, cantidad, precio_unitario)
        for linea in self.lineas:
            if (linea.producto.codigo == nueva.producto.codigo
                    and linea.precio_unitario == nueva.precio_unitario):
                linea.cantidad += nueva.cantidad
                return linea
        self.lineas.append(nueva)
        return nueva

    def quitar_linea(self, codigo):
        """[EXTRA] Elimina la línea de ese producto y la devuelve (None si no hay)."""
        codigo = _clave(codigo)
        for posicion, linea in enumerate(self.lineas):
            if linea.producto.codigo == codigo:
                return self.lineas.pop(posicion)
        return None

    def unidades(self):
        """[EXTRA] Total de unidades de la venta."""
        return sum(linea.cantidad for linea in self.lineas)

    def subtotal(self):
        """[EXAMEN] Suma de los importes de las líneas."""
        return round(sum(linea.importe() for linea in self.lineas), 2)

    def descuento(self):
        """[EXAMEN] 10 % del subtotal si es >= 50 €; 0 en caso contrario."""
        subtotal = self.subtotal()
        if subtotal >= self.UMBRAL_DESCUENTO:
            return round(subtotal * self.PORCENTAJE_DESCUENTO, 2)
        return 0.0

    def total(self):
        """[EXAMEN] subtotal - descuento."""
        return round(self.subtotal() - self.descuento(), 2)


class Tienda:
    """Gestor: catálogo, venta en curso e historial de ventas cerradas."""

    def __init__(self):
        self.productos = {}
        self.ventas_cerradas = []
        self.venta_actual = None

    # --- catálogo ---
    def alta_producto(self, producto):
        """[EXAMEN] True si se da de alta; False si el código ya existía."""
        if producto.codigo in self.productos:
            return False
        self.productos[producto.codigo] = producto
        return True

    def buscar_producto(self, codigo):
        """[EXAMEN] Producto por código, o None."""
        return self.productos.get(_clave(codigo))

    def listar_productos(self):
        """[EXAMEN]"""
        return list(self.productos.values())

    def reponer(self, codigo, cantidad):
        """[EXAMEN] "OK", "NO_EXISTE" o "CANTIDAD_INVALIDA"."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return "NO_EXISTE"
        if not producto.reponer(cantidad):
            return "CANTIDAD_INVALIDA"
        return "OK"

    def buscar_productos(self, texto):
        """[EXTRA] Fragmento en nombre o categoría, sin distinguir mayúsculas."""
        texto = str(texto).strip().casefold()
        if not texto:
            return []
        return [p for p in self.productos.values()
                if texto in p.nombre.casefold() or texto in p.categoria.casefold()]

    def productos_bajo_stock(self, umbral=5):
        """[EXTRA] Productos con stock <= umbral (para reponer)."""
        return [p for p in self.productos.values() if p.stock <= umbral]

    def valor_inventario(self):
        """[EXTRA] Valor total del almacén."""
        return round(sum(p.valor_en_stock() for p in self.productos.values()), 2)

    # --- ventas ---
    def _numero_siguiente(self):
        return max((v.numero for v in self.ventas_cerradas), default=0) + 1

    def abrir_venta(self, cliente):
        """[EXAMEN] "OK", "VENTA_ABIERTA" o "CLIENTE_VACIO"."""
        if self.venta_actual is not None:
            return "VENTA_ABIERTA"
        try:
            venta = Venta(self._numero_siguiente(), cliente)
        except ValueError:
            return "CLIENTE_VACIO"
        self.venta_actual = venta
        return "OK"

    def anadir_linea(self, codigo, cantidad):
        """[EXAMEN] Añade línea y descuenta stock UNA sola vez.

        "OK", "SIN_VENTA", "NO_EXISTE", "CANTIDAD_INVALIDA" o "STOCK_INSUFICIENTE".
        Si no devuelve "OK", no se modifica nada.
        """
        if self.venta_actual is None:
            return "SIN_VENTA"
        producto = self.buscar_producto(codigo)
        if producto is None:
            return "NO_EXISTE"
        try:
            cantidad = _entero(cantidad, "La cantidad", minimo=1)
        except ValueError:
            return "CANTIDAD_INVALIDA"
        if cantidad > producto.stock:
            return "STOCK_INSUFICIENTE"
        self.venta_actual.agregar_linea(producto, cantidad)
        producto.descontar(cantidad)
        return "OK"

    def quitar_linea(self, codigo):
        """[EXTRA] Quita un producto de la venta actual devolviendo su stock."""
        if self.venta_actual is None:
            return "SIN_VENTA"
        linea = self.venta_actual.quitar_linea(codigo)
        if linea is None:
            return "NO_EXISTE"
        linea.producto.reponer(linea.cantidad)
        return "OK"

    def cerrar_venta(self):
        """[EXAMEN] "OK", "SIN_VENTA" o "VENTA_VACIA" (sigue abierta)."""
        if self.venta_actual is None:
            return "SIN_VENTA"
        if not self.venta_actual.lineas:
            return "VENTA_VACIA"
        self.ventas_cerradas.append(self.venta_actual)
        self.venta_actual = None
        return "OK"

    def cancelar_venta(self):
        """[EXAMEN-ampliación] Cancela la venta actual devolviendo todo el stock."""
        if self.venta_actual is None:
            return False
        for linea in self.venta_actual.lineas:
            linea.producto.reponer(linea.cantidad)
        self.venta_actual = None
        return True

    def incorporar_venta(self, venta):
        """[EXAMEN] Añade una venta ya cerrada (carga de CSV). False si el número existe."""
        if any(v.numero == venta.numero for v in self.ventas_cerradas):
            return False
        self.ventas_cerradas.append(venta)
        return True

    def importe_acumulado(self):
        """[EXAMEN] Suma del total de todas las ventas cerradas."""
        return round(sum(v.total() for v in self.ventas_cerradas), 2)

    def ventas_de_cliente(self, cliente):
        """[EXTRA] Ventas cerradas de un cliente (sin distinguir mayúsculas)."""
        cliente = str(cliente).strip().casefold()
        return [v for v in self.ventas_cerradas if v.cliente.casefold() == cliente]

    def unidades_vendidas(self):
        """[EXTRA] Diccionario codigo -> unidades vendidas en ventas cerradas."""
        vendidas = {}
        for venta in self.ventas_cerradas:
            for linea in venta.lineas:
                codigo = linea.producto.codigo
                vendidas[codigo] = vendidas.get(codigo, 0) + linea.cantidad
        return vendidas

    def producto_mas_vendido(self):
        """[EXTRA] Producto con más unidades vendidas (empate: código menor) o None."""
        vendidas = self.unidades_vendidas()
        if not vendidas:
            return None
        codigo = sorted(vendidas, key=lambda c: (-vendidas[c], c))[0]
        return self.productos.get(codigo)

    def ticket_medio(self):
        """[EXTRA] Importe medio por venta cerrada (0.0 si no hay)."""
        if not self.ventas_cerradas:
            return 0.0
        return round(self.importe_acumulado() / len(self.ventas_cerradas), 2)


# =====================================================================
# 4. CARTAS DE RAZAS  (proyecto 02: colección e intercambios atómicos)
# =====================================================================
class CartaRaza:
    """Carta coleccionable de una raza. tipo = tamaño (Pequeño/Mediano/Grande)."""

    def __init__(self, codigo, nombre, tipo, rareza, valor):
        self.codigo = _texto(codigo, "El código").upper()
        self.nombre = _texto(nombre, "El nombre")
        self.tipo = _texto(tipo, "El tipo")
        self.rareza = _texto(rareza, "La rareza")
        self.valor = _decimal(valor, "El valor", minimo=0, estricto=False)  # 0 permitido

    def a_fila(self):
        """[EXTRA]"""
        return {"codigo": self.codigo, "nombre": self.nombre, "tipo": self.tipo,
                "rareza": self.rareza, "valor": self.valor}


class ColeccionRazas:
    """Diccionario codigo -> CartaRaza."""

    def __init__(self):
        self.cartas = {}

    def anadir(self, carta):
        """[EXAMEN] Devuelve "OK" o "DUPLICADO"."""
        if carta.codigo in self.cartas:
            return "DUPLICADO"
        self.cartas[carta.codigo] = carta
        return "OK"

    def eliminar(self, codigo):
        """[EXAMEN] True si la carta existía y se ha eliminado."""
        return self.cartas.pop(_clave(codigo), None) is not None

    def listar(self):
        """[EXAMEN]"""
        return list(self.cartas.values())

    def buscar(self, texto):
        """[EXAMEN] Por nombre o tipo, sin distinguir mayúsculas."""
        texto = str(texto).strip().casefold()
        if not texto:
            return []
        return [c for c in self.cartas.values()
                if texto in c.nombre.casefold() or texto in c.tipo.casefold()]

    def filtrar_por_rareza(self, rareza):
        """[EXAMEN] Cartas de esa rareza exacta (sin distinguir mayúsculas)."""
        rareza = str(rareza).strip().casefold()
        return [c for c in self.cartas.values() if c.rareza.casefold() == rareza]

    def intercambiar(self, codigo_antiguo, carta_nueva):
        """[EXAMEN] Operación ATÓMICA: o se hace completa o no cambia nada.

        "OK", "NO_EXISTE" (la antigua no está) o "CODIGO_OCUPADO" (el nuevo ya existe).
        Primero se comprueba todo; solo entonces se elimina una y se incorpora la otra.
        """
        antiguo = _clave(codigo_antiguo)
        if antiguo not in self.cartas:
            return "NO_EXISTE"
        if carta_nueva.codigo in self.cartas:
            return "CODIGO_OCUPADO"
        del self.cartas[antiguo]
        self.cartas[carta_nueva.codigo] = carta_nueva
        return "OK"

    def valor_total(self):
        """[EXAMEN] Suma del valor de todas las cartas."""
        return round(sum(c.valor for c in self.cartas.values()), 2)

    def contar(self):
        """[EXAMEN] Número de cartas."""
        return len(self.cartas)

    def contar_por_rareza(self):
        """[EXAMEN] Diccionario rareza -> cantidad."""
        cuenta = {}
        for carta in self.cartas.values():
            cuenta[carta.rareza] = cuenta.get(carta.rareza, 0) + 1
        return cuenta

    def estadisticas(self):
        """[EXAMEN] Valor total, número de cartas y cartas por rareza."""
        return {"cartas": self.contar(), "valor_total": self.valor_total(),
                "por_rareza": self.contar_por_rareza()}

    def ordenar_por_valor(self, descendente=True):
        """[EXAMEN-ampliación] Cartas ordenadas por valor (desempate por código)."""
        if descendente:
            return sorted(self.cartas.values(), key=lambda c: (-c.valor, c.codigo))
        return sorted(self.cartas.values(), key=lambda c: (c.valor, c.codigo))

    def top(self, n=3):
        """[EXAMEN-ampliación] Las n cartas de mayor valor."""
        if n <= 0:
            return []
        return self.ordenar_por_valor(True)[:n]


# =====================================================================
# 5. ESCUELA CANINA  (proyecto 03: inscripciones y plazas)
#    Participante = dueño (+ su perro) · Taller = clase de adiestramiento
# =====================================================================
class Participante:
    """Dueño inscrito en la escuela. El email es la clave única."""

    def __init__(self, email, nombre, perro=""):
        self.email = _email(email)
        self.nombre = _texto(nombre, "El nombre")
        self.perro = perro.strip() if isinstance(perro, str) else ""


class Taller:
    """Clase con aforo limitado."""

    def __init__(self, codigo, titulo, plazas):
        self.codigo = _texto(codigo, "El código").upper()
        self.titulo = _texto(titulo, "El título")
        self.plazas = _entero(plazas, "Las plazas", minimo=1)


class Inscripcion:
    """Relaciona un participante y un taller SOLO por email y código."""

    def __init__(self, email_participante, codigo_taller):
        self.email_participante = str(email_participante).strip().lower()
        self.codigo_taller = _clave(codigo_taller)


class EscuelaCanina:
    """Gestiona participantes, talleres e inscripciones."""

    def __init__(self):
        self.participantes = {}   # email -> Participante
        self.talleres = {}        # codigo -> Taller
        self.inscripciones = []   # lista de Inscripcion

    # --- altas ---
    def alta_participante(self, participante):
        """[EXAMEN] Devuelve "OK" o "DUPLICADO" (email repetido)."""
        if participante.email in self.participantes:
            return "DUPLICADO"
        self.participantes[participante.email] = participante
        return "OK"

    def alta_taller(self, taller):
        """[EXTRA] Devuelve "OK" o "DUPLICADO" (código repetido)."""
        if taller.codigo in self.talleres:
            return "DUPLICADO"
        self.talleres[taller.codigo] = taller
        return "OK"

    def baja_participante(self, email):
        """[EXTRA] Elimina al participante y TODAS sus inscripciones (sin huérfanas)."""
        email = str(email).strip().lower()
        if email not in self.participantes:
            return False
        del self.participantes[email]
        self.inscripciones = [i for i in self.inscripciones
                              if i.email_participante != email]
        return True

    # --- inscripciones ---
    def buscar_inscripcion(self, email, codigo):
        """[EXAMEN] La Inscripcion que coincide, o None."""
        email = str(email).strip().lower()
        codigo = _clave(codigo)
        for inscripcion in self.inscripciones:
            if (inscripcion.email_participante == email
                    and inscripcion.codigo_taller == codigo):
                return inscripcion
        return None

    def inscribir(self, email, codigo):
        """[EXAMEN] "OK", "NO_EXISTE_PARTICIPANTE", "NO_EXISTE_TALLER",
        "DUPLICADA" o "COMPLETO". Si no es "OK", no cambia nada."""
        email = str(email).strip().lower()
        codigo = _clave(codigo)
        if email not in self.participantes:
            return "NO_EXISTE_PARTICIPANTE"
        if codigo not in self.talleres:
            return "NO_EXISTE_TALLER"
        if self.buscar_inscripcion(email, codigo) is not None:
            return "DUPLICADA"
        if self.plazas_libres(codigo) <= 0:
            return "COMPLETO"
        self.inscripciones.append(Inscripcion(email, codigo))
        return "OK"

    def cancelar(self, email, codigo):
        """[EXAMEN] True si se cancela. Cancelar una inexistente no afecta a nada."""
        inscripcion = self.buscar_inscripcion(email, codigo)
        if inscripcion is None:
            return False
        self.inscripciones.remove(inscripcion)
        return True

    # --- consultas ---
    def inscritos_taller(self, codigo):
        """[EXAMEN] Lista de Participante inscritos, o None si el taller no existe."""
        codigo = _clave(codigo)
        if codigo not in self.talleres:
            return None
        return [self.participantes[i.email_participante]
                for i in self.inscripciones
                if i.codigo_taller == codigo and i.email_participante in self.participantes]

    def plazas_libres(self, codigo):
        """[EXAMEN] Plazas sin ocupar, o None si el taller no existe."""
        inscritos = self.inscritos_taller(codigo)
        if inscritos is None:
            return None
        return self.talleres[_clave(codigo)].plazas - len(inscritos)

    def porcentaje_ocupacion(self, codigo):
        """[EXAMEN] Porcentaje de plazas ocupadas, o None si el taller no existe."""
        inscritos = self.inscritos_taller(codigo)
        if inscritos is None:
            return None
        return len(inscritos) * 100 / self.talleres[_clave(codigo)].plazas

    def esta_completo(self, codigo):
        """[EXTRA] True/False, o None si el taller no existe."""
        libres = self.plazas_libres(codigo)
        if libres is None:
            return None
        return libres == 0

    def buscar_participante(self, fragmento):
        """[EXAMEN] Por fragmento del nombre del dueño o de su perro."""
        fragmento = str(fragmento).strip().casefold()
        if not fragmento:
            return []
        return [p for p in self.participantes.values()
                if fragmento in p.nombre.casefold() or fragmento in p.perro.casefold()]

    def talleres_de_participante(self, email):
        """[EXAMEN] Talleres en los que está inscrito, o None si no existe."""
        email = str(email).strip().lower()
        if email not in self.participantes:
            return None
        return [self.talleres[i.codigo_taller] for i in self.inscripciones
                if i.email_participante == email and i.codigo_taller in self.talleres]

    def talleres_con_plazas(self):
        """[EXTRA] Talleres que todavía admiten inscripciones."""
        return [t for t in self.talleres.values() if self.plazas_libres(t.codigo) > 0]

    def ranking_ocupacion(self):
        """[EXAMEN-ampliación] Lista de (Taller, porcentaje) de mayor a menor ocupación."""
        ranking = [(t, self.porcentaje_ocupacion(t.codigo)) for t in self.talleres.values()]
        return sorted(ranking, key=lambda par: (-par[1], par[0].titulo.casefold()))


# =====================================================================
# 6. SERVICIOS CANINOS  (proyecto 04: HERENCIA)
#    Trabajo -> ServicioCanino · Reparacion -> Peluqueria · Remota -> Teleconsulta
# =====================================================================
class ServicioCanino:
    """Clase BASE: datos y estados comunes. Estados: PENDIENTE -> EN_CURSO -> FINALIZADO."""

    TIPO = "BASE"
    ESTADOS = ("PENDIENTE", "EN_CURSO", "FINALIZADO")

    def __init__(self, codigo, cliente, horas, estado="PENDIENTE"):
        self.codigo = _texto(codigo, "El código").upper()
        self.cliente = _texto(cliente, "El cliente")
        self.horas = _decimal(horas, "Las horas", minimo=0, estricto=True)
        self.estado = _estado(estado, self.ESTADOS)

    def calcular_importe(self):
        """[EXAMEN] POLIMORFISMO: cada subclase lo redefine."""
        raise NotImplementedError("Las subclases deben implementar calcular_importe()")

    def siguiente_estado(self):
        """[EXTRA] El único estado al que se puede pasar, o None si ya está FINALIZADO."""
        posicion = self.ESTADOS.index(self.estado)
        if posicion + 1 < len(self.ESTADOS):
            return self.ESTADOS[posicion + 1]
        return None

    def cambiar_estado(self, nuevo):
        """[EXAMEN] Solo permite avanzar un paso: no saltar ni retroceder."""
        if not isinstance(nuevo, str) or nuevo.strip().upper() != self.siguiente_estado():
            return False
        self.estado = nuevo.strip().upper()
        return True

    def avanzar(self):
        """[EXTRA] Avanza al siguiente estado. False si ya está FINALIZADO."""
        siguiente = self.siguiente_estado()
        if siguiente is None:
            return False
        self.estado = siguiente
        return True

    def cambiar_horas(self, nuevas):
        """[EXAMEN-ampliación] Cambia las horas si no está FINALIZADO y son válidas."""
        if self.estado == "FINALIZADO":
            return False
        try:
            self.horas = _decimal(nuevas, "Las horas", minimo=0, estricto=True)
        except ValueError:
            return False
        return True

    def a_fila(self):
        """[EXAMEN] Fila CSV con el campo `tipo` para reconstruir el subtipo al cargar."""
        return {"tipo": self.TIPO, "codigo": self.codigo, "cliente": self.cliente,
                "horas": self.horas,
                "precio_producto": getattr(self, "precio_producto", 0.0),
                "estado": self.estado}


class Peluqueria(ServicioCanino):
    """Baño/corte: horas x tarifa + precio del producto utilizado."""

    TIPO = "PELUQUERIA"
    TARIFA_HORA = 25.0

    def __init__(self, codigo, cliente, horas, precio_producto, estado="PENDIENTE"):
        super().__init__(codigo, cliente, horas, estado)
        self.precio_producto = _decimal(precio_producto, "El precio del producto", minimo=0)

    def calcular_importe(self):
        """[EXAMEN] horas x 25 € + precio_producto."""
        return round(self.horas * self.TARIFA_HORA + self.precio_producto, 2)


class Teleconsulta(ServicioCanino):
    """Consulta veterinaria a distancia: horas x tarifa."""

    TIPO = "TELECONSULTA"
    TARIFA_HORA = 20.0

    def calcular_importe(self):
        """[EXAMEN] horas x 20 €."""
        return round(self.horas * self.TARIFA_HORA, 2)


class GestorServicios:
    """Diccionario codigo -> servicio (de cualquier subtipo)."""

    def __init__(self):
        self.servicios = {}

    def alta(self, servicio):
        """[EXAMEN] True si se da de alta; False si el código ya existía."""
        if servicio.codigo in self.servicios:
            return False
        self.servicios[servicio.codigo] = servicio
        return True

    def obtener(self, codigo):
        """[EXTRA]"""
        return self.servicios.get(_clave(codigo))

    def listar(self):
        """[EXAMEN]"""
        return list(self.servicios.values())

    def cambiar_estado(self, codigo, nuevo):
        """[EXAMEN] "OK", "NO_EXISTE" o "TRANSICION_INVALIDA" (sin cambios)."""
        servicio = self.obtener(codigo)
        if servicio is None:
            return "NO_EXISTE"
        if not servicio.cambiar_estado(nuevo):
            return "TRANSICION_INVALIDA"
        return "OK"

    def cambiar_horas(self, codigo, horas):
        """[EXAMEN-ampliación] "OK", "NO_EXISTE", "FINALIZADO" o "HORAS_INVALIDAS"."""
        servicio = self.obtener(codigo)
        if servicio is None:
            return "NO_EXISTE"
        if servicio.estado == "FINALIZADO":
            return "FINALIZADO"
        if not servicio.cambiar_horas(horas):
            return "HORAS_INVALIDAS"
        return "OK"

    def buscar(self, cliente="", tipo=None, estado=None):
        """[EXAMEN] Por fragmento de cliente, filtrando opcionalmente por tipo y estado."""
        fragmento = str(cliente).strip().casefold()
        resultado = []
        for servicio in self.servicios.values():
            if fragmento and fragmento not in servicio.cliente.casefold():
                continue
            if tipo and servicio.TIPO != str(tipo).strip().upper():
                continue
            if estado and servicio.estado != str(estado).strip().upper():
                continue
            resultado.append(servicio)
        return resultado

    def resumen(self):
        """[EXAMEN] Nº de servicios por estado e importe total de los FINALIZADOS."""
        por_estado = {estado: 0 for estado in ServicioCanino.ESTADOS}
        importe_finalizados = 0.0
        for servicio in self.servicios.values():
            por_estado[servicio.estado] += 1
            if servicio.estado == "FINALIZADO":
                importe_finalizados += servicio.calcular_importe()
        return {"total": len(self.servicios), "por_estado": por_estado,
                "importe_finalizados": round(importe_finalizados, 2)}

    def importe_pendiente(self):
        """[EXTRA] Importe de los servicios que todavía no están FINALIZADOS."""
        return round(sum(s.calcular_importe() for s in self.servicios.values()
                         if s.estado != "FINALIZADO"), 2)


# =====================================================================
# COMPROBACIONES (único lugar con print)
# =====================================================================
def main():
    def lanza(funcion, *args):
        try:
            funcion(*args)
        except ValueError:
            return True
        return False

    # ---- 1. RegistroPerdidos (BiciAlerta / CanAlerta) ----
    r = RegistroPerdidos()
    for datos in [("PR01", "Ana García", "Border Collie", 300, "PERDIDO"),
                  ("PR02", "Carlos López", "Beagle", 240, "PERDIDO"),
                  ("PR03", "Lucía Martín", "Labrador", 300, "ENCONTRADO")]:
        assert r.registrar(PerroPerdido(*datos))
    res = r.resumen()
    assert (res["total"], res["perdidos"], res["encontrados"]) == (3, 2, 1)
    assert res["recompensa_pendiente"] == 540
    assert r.registrar(PerroPerdido("pr04", "Marta", "Golden Retriever", "180,00"))
    assert r.resumen()["recompensa_pendiente"] == 720 and r.resumen()["total"] == 4
    assert r.registrar(PerroPerdido("PR01", "X", "Y", 10)) is False       # duplicado
    assert r.resumen()["recompensa_pendiente"] == 720
    assert r.encontrar("pr01") is True and r.resumen()["recompensa_pendiente"] == 420
    assert r.encontrar("PR01") is False and r.encontrar("ZZ") is False
    assert [p.codigo for p in r.buscar("BORDER")] == ["PR01"] and r.buscar("  ") == []
    for malo in (0, -5, "abc", "nan", "inf", None, True):
        assert lanza(PerroPerdido, "X", "Y", "Z", malo), malo
    assert r.top_recompensas(1)[0].codigo == "PR02"
    assert r.recompensa_media_pendiente() == 210
    assert r.obtener("PR02").cambiar_recompensa(500) and not r.obtener("PR01").cambiar_recompensa(9)
    assert r.eliminar("pr04") and not r.eliminar("pr04")
    assert len(r.filtrar_por_estado("encontrado")) == 2

    # ---- 2. Protectora (PatitasAdopta) ----
    p = Protectora()
    for datos in [("DG01", "Toby", "Labrador", 4, 30.0, "DISPONIBLE"),
                  ("DG02", "Luna", "Beagle", 2, 12.0, "DISPONIBLE"),
                  ("DG03", "Rex", "Pastor Alemán", 6, 35.0, "ADOPTADO")]:
        assert p.registrar(Perro(*datos))
    e = p.estadisticas()
    assert e["peso_medio_disponibles"] == 21.0 and e["mas_pesado"].nombre == "Rex"
    assert p.registrar(Perro("DG04", "Nala", "Husky", 3, "24"))
    assert p.estadisticas()["peso_medio_disponibles"] == 22.0
    assert p.registrar(Perro("DG01", "X", "Y", 1, 1)) is False
    for edad, peso in ((-1, 5), (31, 5), ("x", 5), (2.5, 5), (3, 0), (3, -1), (3, "abc")):
        assert lanza(Perro, "D", "N", "R", edad, peso), (edad, peso)
    assert [d.nombre for d in p.disponibles_por_edad()] == ["Luna", "Nala", "Toby"]
    assert p.adoptar("dg01") and not p.adoptar("DG01") and not p.adoptar("ZZ")
    assert p.estadisticas()["peso_medio_disponibles"] == 18.0
    assert p.dar_de_baja("DG03") and not p.dar_de_baja("XX")
    assert p.estadisticas()["total"] == 3 and p.estadisticas()["mas_pesado"].nombre == "Toby"
    assert p.devolver("DG01") and p.obtener("DG01").esta_disponible()
    assert p.obtener("DG04").etapa_vida() == "ADULTO" and p.obtener("DG04").categoria_peso() == "MEDIANO"
    assert [d.nombre for d in p.buscar("lab")] == ["Toby"]
    assert p.contar_por_raza() == {"labrador": 1, "beagle": 1, "husky": 1}
    assert len(p.filtrar_por_peso(10, 25)) == 2 and p.edad_media() == 3.0
    assert Protectora().estadisticas()["peso_medio_disponibles"] == 0.0

    # ---- 3. Tienda ----
    t = Tienda()
    for prod in [Producto("CAN01", "Huesos masticables", "Snacks", 3.5, 15),
                 Producto("CAN02", "Pelotas de tenis", "Juguetes", 2.25, 24),
                 Producto("CAN03", "Cama ortopédica", "Descanso", 18, 4)]:
        assert t.alta_producto(prod)
    assert t.alta_producto(Producto("can01", "X", "Y", 1, 1)) is False
    for precio, stock in ((-1, 1), (0, 1), (1, -1)):
        assert lanza(Producto, "C", "N", "K", precio, stock)
    assert t.abrir_venta("Laura") == "OK" and t.abrir_venta("Otro") == "VENTA_ABIERTA"
    assert t.anadir_linea("CAN01", 3) == "OK" and t.buscar_producto("CAN01").stock == 12
    assert t.anadir_linea("CAN01", 20) == "STOCK_INSUFICIENTE" and t.buscar_producto("CAN01").stock == 12
    for mala in (0, -1, "abc", 2.5):
        assert t.anadir_linea("CAN01", mala) == "CANTIDAD_INVALIDA"
    assert t.anadir_linea("XXX", 1) == "NO_EXISTE" and t.buscar_producto("CAN01").stock == 12
    assert t.cerrar_venta() == "OK" and t.cerrar_venta() == "SIN_VENTA"
    assert t.reponer("CAN01", 3) == "OK" and t.buscar_producto("CAN01").stock == 15
    assert t.reponer("CAN01", -1) == "CANTIDAD_INVALIDA" and t.reponer("ZZ", 1) == "NO_EXISTE"
    t.abrir_venta("Pedro")
    t.anadir_linea("CAN03", 2)
    t.anadir_linea("CAN02", 4)
    v = t.venta_actual
    assert (v.subtotal(), v.descuento(), v.total()) == (45.0, 0.0, 45.0)
    assert t.cancelar_venta() and t.buscar_producto("CAN03").stock == 4 and t.buscar_producto("CAN02").stock == 24
    assert t.cancelar_venta() is False
    t.abrir_venta("Rosa")
    t.anadir_linea("CAN03", 3)
    v = t.venta_actual
    assert (v.subtotal(), v.descuento(), v.total()) == (54.0, 5.4, 48.6)
    assert t.quitar_linea("CAN03") == "OK" and t.buscar_producto("CAN03").stock == 4
    assert t.cerrar_venta() == "VENTA_VACIA"
    t.anadir_linea("CAN03", 3)
    assert t.cerrar_venta() == "OK"
    assert t.importe_acumulado() == 59.1 and t.ticket_medio() == 29.55
    assert t.producto_mas_vendido().codigo == "CAN01"
    assert [x.codigo for x in t.productos_bajo_stock(5)] == ["CAN03"]
    assert t.valor_inventario() == 3.5 * 15 + 2.25 * 24 + 18 * 1
    assert len(t.ventas_de_cliente("laura")) == 1 and t.unidades_vendidas()["CAN03"] == 3
    assert [x.codigo for x in t.buscar_productos("juguete")] == ["CAN02"]

    # ---- 4. ColeccionRazas ----
    c = ColeccionRazas()
    for carta in [CartaRaza("RZ01", "Labrador", "Grande", "Común", 5),
                  CartaRaza("RZ02", "Husky", "Grande", "Rara", 30),
                  CartaRaza("RZ03", "Chihuahua", "Pequeño", "Común", 4)]:
        assert c.anadir(carta) == "OK"
    assert c.valor_total() == 39 and c.anadir(CartaRaza("RZ01", "X", "Y", "Z", 1)) == "DUPLICADO"
    assert c.contar() == 3 and lanza(CartaRaza, "A", "B", "C", "D", -1)
    assert c.intercambiar("RZ02", CartaRaza("RZ03", "Otro", "T", "R", 9)) == "CODIGO_OCUPADO"
    assert "RZ02" in c.cartas and c.valor_total() == 39
    assert c.intercambiar("RZ99", CartaRaza("RZ05", "A", "B", "C", 1)) == "NO_EXISTE"
    assert c.intercambiar("rz02", CartaRaza("RZ04", "Samoyedo", "Grande", "Rara", 50)) == "OK"
    assert c.contar() == 3 and c.valor_total() == 59 and "RZ02" not in c.cartas
    assert c.contar_por_rareza() == {"Común": 2, "Rara": 1}
    assert [x.codigo for x in c.top(2)] == ["RZ04", "RZ01"]
    assert [x.codigo for x in c.buscar("GRANDE")] == ["RZ01", "RZ04"]
    assert len(c.filtrar_por_rareza("común")) == 2 and c.eliminar("rz01") and not c.eliminar("rz01")

    # ---- 5. EscuelaCanina ----
    s = EscuelaCanina()
    for taller in (Taller("CER", "Obediencia básica", 2), Taller("FOT", "Agility", 3),
                   Taller("COC", "Socialización", 4)):
        assert s.alta_taller(taller) == "OK"
    assert s.alta_taller(Taller("cer", "Otro", 1)) == "DUPLICADO"
    for email, nombre, perro in (("ana@correo.es", "Ana", "Toby"), ("luis@correo.es", "Luis", "Luna"),
                                 ("eva@correo.es", "Eva", "Rex")):
        assert s.alta_participante(Participante(email, nombre, perro)) == "OK"
    assert s.alta_participante(Participante("ANA@correo.es", "Otra", "")) == "DUPLICADO"
    for malo in ("sin-arroba", "a@b", "@x.com", "a b@x.com", None):
        assert lanza(Participante, malo, "Nombre")
    assert s.inscribir("ana@correo.es", "CER") == "OK"
    assert s.inscribir("ana@correo.es", "cer") == "DUPLICADA"
    assert s.plazas_libres("CER") == 1 and s.porcentaje_ocupacion("CER") == 50.0
    assert s.inscribir("luis@correo.es", "CER") == "OK"
    assert s.inscribir("eva@correo.es", "CER") == "COMPLETO"
    assert s.inscribir("nadie@correo.es", "CER") == "NO_EXISTE_PARTICIPANTE"
    assert s.inscribir("eva@correo.es", "XXX") == "NO_EXISTE_TALLER"
    assert len(s.inscripciones) == 2 and s.esta_completo("CER") is True
    assert s.cancelar("luis@correo.es", "CER") and s.plazas_libres("CER") == 1
    assert s.cancelar("luis@correo.es", "CER") is False and len(s.inscripciones) == 1
    assert s.inscritos_taller("XXX") is None and s.plazas_libres("XXX") is None
    assert [x.nombre for x in s.buscar_participante("toby")] == ["Ana"]
    assert [x.codigo for x in s.talleres_de_participante("ana@correo.es")] == ["CER"]
    assert s.talleres_de_participante("nadie@correo.es") is None
    assert s.ranking_ocupacion()[0][0].codigo == "CER"
    assert len(s.talleres_con_plazas()) == 3
    assert s.baja_participante("ana@correo.es") and s.inscripciones == []

    # ---- 6. Servicios (herencia) ----
    g = GestorServicios()
    pelu = Peluqueria("SV01", "Marta Ruiz", 2, 40)
    tele = Teleconsulta("SV02", "Javier Soto", 1.5)
    assert pelu.calcular_importe() == 90 and tele.calcular_importe() == 30
    assert isinstance(pelu, ServicioCanino) and lanza(Peluqueria, "S", "C", 1, -3)
    try:
        ServicioCanino("SV00", "Base", 1).calcular_importe()
        base_sin_importe = False
    except NotImplementedError:
        base_sin_importe = True
    assert base_sin_importe        # la clase base obliga a implementar calcular_importe()
    assert g.alta(pelu) and g.alta(tele) and g.alta(Teleconsulta("sv01", "X", 1)) is False
    assert g.cambiar_estado("SV01", "FINALIZADO") == "TRANSICION_INVALIDA" and pelu.estado == "PENDIENTE"
    assert g.cambiar_estado("SV01", "EN_CURSO") == "OK" and g.cambiar_estado("SV01", "PENDIENTE") == "TRANSICION_INVALIDA"
    assert g.cambiar_horas("SV01", 3) == "OK" and pelu.calcular_importe() == 115
    assert g.cambiar_horas("SV01", 0) == "HORAS_INVALIDAS"
    assert g.cambiar_estado("SV01", "FINALIZADO") == "OK" and g.cambiar_horas("SV01", 5) == "FINALIZADO"
    assert g.cambiar_estado("SV99", "EN_CURSO") == "NO_EXISTE"
    rs = g.resumen()
    assert rs["por_estado"] == {"PENDIENTE": 1, "EN_CURSO": 0, "FINALIZADO": 1}
    assert rs["importe_finalizados"] == 115 and g.importe_pendiente() == 30
    assert [x.codigo for x in g.buscar("ruiz")] == ["SV01"]
    assert [x.codigo for x in g.buscar(tipo="teleconsulta")] == ["SV02"]
    assert [x.codigo for x in g.buscar(estado="finalizado")] == ["SV01"]
    assert pelu.a_fila()["tipo"] == "PELUQUERIA" and tele.a_fila()["precio_producto"] == 0.0

    print("metodos_con_self.py: todas las comprobaciones han pasado correctamente.")


if __name__ == "__main__":
    main()