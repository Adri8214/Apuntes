"""Clases de dominio de la Tienda Canina Huellas. Sin print() ni input()."""
import math

UMBRAL_DESCUENTO = 50.0
PORCENTAJE_DESCUENTO = 0.10


# ---------- Funciones auxiliares de validación (devuelven valor o lanzan ValueError) ----------
def _texto_obligatorio(valor, nombre):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{nombre} no puede estar vacío")
    return valor.strip()


def _entero(valor, nombre):
    if isinstance(valor, bool):
        raise ValueError(f"{nombre} debe ser un número entero")
    if isinstance(valor, float):
        if not valor.is_integer():
            raise ValueError(f"{nombre} debe ser un número entero")
        return int(valor)
    try:
        return int(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{nombre} debe ser un número entero") from None


def _decimal(valor, nombre):
    if isinstance(valor, bool):
        raise ValueError(f"{nombre} debe ser numérico")
    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{nombre} debe ser numérico") from None
    if not math.isfinite(numero):
        raise ValueError(f"{nombre} debe ser un número finito")
    return numero


# ---------- Producto ----------
class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = _texto_obligatorio(codigo, "El código").upper()
        self.nombre = _texto_obligatorio(nombre, "El nombre")
        self.categoria = _texto_obligatorio(categoria, "La categoría")

        precio = _decimal(precio, "El precio")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        stock = _entero(stock, "El stock")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self.precio = precio
        self.stock = stock

    def reponer(self, cantidad):
        """Suma unidades al stock. Devuelve False (sin cambios) si la cantidad no es válida."""
        try:
            cantidad = _entero(cantidad, "La cantidad")
        except ValueError:
            return False
        if cantidad <= 0:
            return False
        self.stock += cantidad
        return True

    def descontar(self, cantidad):
        """Resta unidades del stock. Devuelve False (sin cambios) si no es posible."""
        try:
            cantidad = _entero(cantidad, "La cantidad")
        except ValueError:
            return False
        if cantidad <= 0 or cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True


# ---------- Línea de venta ----------
class LineaVenta:
    def __init__(self, producto, cantidad, precio_unitario):
        if not isinstance(producto, Producto):
            raise ValueError("La línea necesita un producto válido")
        cantidad = _entero(cantidad, "La cantidad")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        precio_unitario = _decimal(precio_unitario, "El precio unitario")
        if precio_unitario <= 0:
            raise ValueError("El precio unitario debe ser mayor que cero")

        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario  # precio "congelado" en el momento de la venta

    def importe(self):
        return round(self.cantidad * self.precio_unitario, 2)


# ---------- Venta ----------
class Venta:
    def __init__(self, numero, cliente):
        numero = _entero(numero, "El número de venta")
        if numero <= 0:
            raise ValueError("El número de venta debe ser positivo")
        self.numero = numero
        self.cliente = _texto_obligatorio(cliente, "El cliente")
        self.lineas = []

    def agregar_linea(self, producto, cantidad, precio_unitario=None):
        """Añade una línea; si ya hay una del mismo producto y precio, suma la cantidad."""
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

    def subtotal(self):
        return round(sum(linea.importe() for linea in self.lineas), 2)

    def descuento(self):
        """10 % sobre el total de la venta si el subtotal es >= 50 €; nunca por línea."""
        subtotal = self.subtotal()
        if subtotal >= UMBRAL_DESCUENTO:
            return round(subtotal * PORCENTAJE_DESCUENTO, 2)
        return 0.0

    def total(self):
        return round(self.subtotal() - self.descuento(), 2)


# ---------- Gestor ----------
class Tienda:
    def __init__(self):
        self.productos = {}
        self.ventas_cerradas = []
        self.venta_actual = None

    # --- Catálogo ---
    def alta_producto(self, producto):
        """True si se da de alta; False si el código ya existía."""
        if producto.codigo in self.productos:
            return False
        self.productos[producto.codigo] = producto
        return True

    def buscar_producto(self, codigo):
        return self.productos.get(str(codigo).strip().upper())

    def listar_productos(self):
        return list(self.productos.values())

    def reponer(self, codigo, cantidad):
        """Devuelve "OK", "NO_EXISTE" o "CANTIDAD_INVALIDA"."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            return "NO_EXISTE"
        if not producto.reponer(cantidad):
            return "CANTIDAD_INVALIDA"
        return "OK"

    # --- Ventas ---
    def _numero_siguiente(self):
        return max((v.numero for v in self.ventas_cerradas), default=0) + 1

    def abrir_venta(self, cliente):
        """Devuelve "OK", "VENTA_ABIERTA" o "CLIENTE_VACIO"."""
        if self.venta_actual is not None:
            return "VENTA_ABIERTA"
        try:
            venta = Venta(self._numero_siguiente(), cliente)
        except ValueError:
            return "CLIENTE_VACIO"
        self.venta_actual = venta
        return "OK"

    def anadir_linea(self, codigo, cantidad):
        """Añade una línea a la venta actual y descuenta el stock UNA sola vez.

        Devuelve "OK", "SIN_VENTA", "NO_EXISTE", "CANTIDAD_INVALIDA" o
        "STOCK_INSUFICIENTE". Si no es "OK", no se modifica nada.
        """
        if self.venta_actual is None:
            return "SIN_VENTA"
        producto = self.buscar_producto(codigo)
        if producto is None:
            return "NO_EXISTE"
        try:
            cantidad = _entero(cantidad, "La cantidad")
        except ValueError:
            return "CANTIDAD_INVALIDA"
        if cantidad <= 0:
            return "CANTIDAD_INVALIDA"
        if cantidad > producto.stock:
            return "STOCK_INSUFICIENTE"

        self.venta_actual.agregar_linea(producto, cantidad)
        producto.descontar(cantidad)
        return "OK"

    def cerrar_venta(self):
        """Devuelve "OK", "SIN_VENTA" o "VENTA_VACIA" (en ese caso la venta sigue abierta)."""
        if self.venta_actual is None:
            return "SIN_VENTA"
        if not self.venta_actual.lineas:
            return "VENTA_VACIA"
        self.ventas_cerradas.append(self.venta_actual)
        self.venta_actual = None
        return "OK"

    def cancelar_venta(self):
        """Cancela la venta actual devolviendo al stock todas sus unidades.

        No toca las ventas ya cerradas. True si había venta que cancelar.
        """
        if self.venta_actual is None:
            return False
        for linea in self.venta_actual.lineas:
            linea.producto.reponer(linea.cantidad)
        self.venta_actual = None
        return True

    def incorporar_venta(self, venta):
        """Añade una venta ya cerrada (carga desde CSV). False si el número ya existe."""
        if any(v.numero == venta.numero for v in self.ventas_cerradas):
            return False
        self.ventas_cerradas.append(venta)
        return True

    def importe_acumulado(self):
        return round(sum(v.total() for v in self.ventas_cerradas), 2)


def productos_iniciales():
    """Catálogo ficticio que se usa cuando productos.csv no existe."""
    return [
        Producto("CAN01", "Huesos masticables", "Snacks", 3.50, 15),
        Producto("CAN02", "Pelotas de tenis", "Juguetes", 2.25, 24),
        Producto("CAN03", "Cama ortopédica", "Descanso", 18.00, 4),
    ]