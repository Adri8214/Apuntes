class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

class LineaVenta:
    def __init__(self, producto_codigo, cantidad, precio_unitario):
        self.producto = producto_codigo
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

class Venta:
    def __init__(self, numero, cliente, cerrada=False):
        self.numero = str(numero)
        self.cliente = cliente
        self.lineas = []
        self.cerrada = cerrada

    def agregar_linea(self, linea):
        self.lineas.append(linea)

    @property
    def subtotal(self):
        return sum(linea.subtotal for linea in self.lineas)

    @property
    def total(self):
        sub = self.subtotal
        # Aplica un 10% de descuento si el subtotal es >= 50 €
        if sub >= 50.0:
            return sub * 0.90
        return sub

class FloristeriaGestor:
    def __init__(self):
        self.productos = {}  # Diccionario {codigo: Producto}
        self.ventas_cerradas = []
        self.venta_actual = None

    def cargar_catalogo_inicial(self):
        if not self.productos:
            defecto = [
                Producto("FLO01", "Rosas", "Flor", 3.50, 15),
                Producto("FLO02", "Tulipanes", "Flor", 2.25, 24),
                Producto("FLO03", "Orquídeas", "Flor", 18.00, 4)
            ]
            for p in defecto:
                self.productos[p.codigo] = p

    def alta_producto(self, codigo, nombre, categoria, precio, stock):
        if not codigo or not nombre:
            return False, "El código y el nombre no pueden estar vacíos."
        if codigo in self.productos:
            return False, "Ya existe un producto con ese código."
        try:
            p = float(precio)
            s = int(stock)
            if p < 0 or s < 0:
                return False, "El precio y el stock no pueden ser negativos."
        except ValueError:
            return False, "El precio y el stock deben ser numéricos."
        
        self.productos[codigo] = Producto(codigo, nombre, categoria, p, s)
        return True, "Producto dado de alta con éxito."

    def reponer_producto(self, codigo, cantidad):
        if codigo not in self.productos:
            return False, "El producto no existe."
        try:
            cant = int(cantidad)
            if cant <= 0:
                return False, "La cantidad a reponer debe ser mayor a cero."
        except ValueError:
            return False, "Cantidad inválida."
        
        self.productos[codigo].stock += cant
        return True, "Stock repuesto correctamente."

    def iniciar_venta(self, numero, cliente):
        if self.venta_actual and not self.venta_actual.cerrada:
            return False, "Ya hay una venta en curso."
        if not numero or not cliente:
            return False, "El número de venta y el cliente son obligatorios."
        self.venta_actual = Venta(numero, cliente)
        return True, "Venta iniciada."

    def agregar_linea_venta(self, codigo_producto, cantidad):
        if not self.venta_actual or self.venta_actual.cerrada:
            return False, "No hay ninguna venta abierta."
        if codigo_producto not in self.productos:
            return False, "El producto no existe en el catálogo."
        try:
            cant = int(cantidad)
            if cant <= 0:
                return False, "La cantidad debe ser mayor que cero."
        except ValueError:
            return False, "Cantidad inválida."

        prod = self.productos[codigo_producto]
        if cant > prod.stock:
            return False, "Stock insuficiente para la cantidad solicitada."

        # Descontar stock una sola vez
        prod.stock -= cant
        linea = LineaVenta(prod.codigo, cant, prod.precio)
        self.venta_actual.agregar_linea(linea)
        return True, "Línea añadida con éxito."

    def cerrar_venta(self):
        if not self.venta_actual or self.venta_actual.cerrada:
            return False, "No hay venta abierta para cerrar."
        if not self.venta_actual.lineas:
            return False, "No se puede cerrar una venta sin líneas."
        
        self.venta_actual.cerrada = True
        self.ventas_cerradas.append(self.venta_actual)
        self.venta_actual = None
        return True, "Venta cerrada y registrada en el historial."

    def cancelar_venta_actual(self):
        if not self.venta_actual or self.venta_actual.cerrada:
            return False, "No hay venta abierta para cancelar."
        # Devolver stock reservado
        for linea in self.venta_actual.lineas:
            if linea.producto in self.productos:
                self.productos[linea.producto].stock += linea.cantidad
        self.venta_actual = None
        return True, "Venta cancelada y stock devuelto."