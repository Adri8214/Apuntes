
"""BIBLIOTECA DE FUNCIONES NORMALES (SIN SELF) · TEMÁTICA CANINA
====================================================================
Funciones sueltas reutilizables en cualquier ejercicio de consola con
perros: validación, búsqueda/orden, dinero y descuentos, cálculos
caninos, formato de texto, CSV, fechas y menús.
 
Etiquetas en cada docstring:
    [EXAMEN] -> la idea apareció en un examen/ejercicio.
    [EXTRA]  -> añadida como ampliación.
 
REGLAS que cumple todo el archivo:
    * Ninguna función imprime ni pide datos: devuelven resultados.
      (print() solo aparece en main(), al final.)
    * Las funciones "a_entero" / "a_decimal" devuelven None si el texto no
      es válido, para usarlas sin try/except en main().
    * Solo biblioteca estándar.
 
ÍNDICE
    A. Conversión y validación de entradas
    B. Listas, búsqueda, filtrado y estadísticas (objetos o diccionarios)
    C. Dinero, descuentos e importes
    D. Cálculos caninos (edad, peso, ración) y fechas
    E. Formato de texto y menús (devuelven cadenas)
    F. CSV: lectura, escritura, conversión de tipos y relaciones
    G. Códigos y fábrica de subtipos (herencia)
 
Ejecuta `python funciones_sin_self.py` para lanzar las comprobaciones.
"""
import csv
import math
import shutil
import tempfile
from datetime import date, timedelta
from pathlib import Path
 
 
# =====================================================================
# A. CONVERSIÓN Y VALIDACIÓN DE ENTRADAS
# =====================================================================
def a_entero(texto):
    """[EXAMEN] '4' -> 4. Devuelve None si no es un entero válido ('3.5', 'abc', '')."""
    if isinstance(texto, bool):
        return None
    try:
        return int(str(texto).strip())
    except ValueError:
        return None
 
 
def a_decimal(texto):
    """[EXAMEN] '3,5' o '3.5' -> 3.5. None si no es número o si es nan/inf."""
    if isinstance(texto, bool):
        return None
    try:
        numero = float(str(texto).strip().replace(",", "."))
    except ValueError:
        return None
    return numero if math.isfinite(numero) else None
 
 
def texto_no_vacio(texto):
    """[EXAMEN] True si es un str con algo más que espacios."""
    return isinstance(texto, str) and bool(texto.strip())
 
 
def en_rango(valor, minimo, maximo):
    """[EXAMEN] True si minimo <= valor <= maximo (False si valor es None)."""
    return valor is not None and minimo <= valor <= maximo
 
 
def es_positivo(valor):
    """[EXAMEN] True si es número finito y > 0 (rechaza None, bool, nan, inf)."""
    if valor is None or isinstance(valor, bool):
        return False
    return math.isfinite(valor) and valor > 0
 
 
def normalizar_codigo(texto):
    """[EXAMEN] ' pr01 ' -> 'PR01'."""
    return str(texto).strip().upper()
 
 
def normalizar_email(texto):
    """[EXAMEN] ' Ana@Correo.ES ' -> 'ana@correo.es'."""
    return str(texto).strip().lower()
 
 
def es_email_valido(texto):
    """[EXAMEN] Comprobación sencilla: usuario@dominio.ext, sin espacios."""
    if not isinstance(texto, str):
        return False
    texto = texto.strip()
    usuario, arroba, dominio = texto.partition("@")
    return (bool(usuario) and arroba == "@" and "@" not in dominio
            and " " not in texto and "." in dominio.strip("."))
 
 
def capitalizar_nombre(texto):
    """[EXTRA] 'ana garcía  lópez' -> 'Ana García López'."""
    return " ".join(parte.capitalize() for parte in str(texto).split())
 
 
def estado_valido(estado, permitidos):
    """[EXAMEN] True si el estado (sin distinguir mayúsculas) está entre los permitidos."""
    return isinstance(estado, str) and estado.strip().upper() in permitidos
 
 
def normalizar_estado(estado):
    """[EXAMEN] ' robada ' -> 'ROBADA'."""
    return str(estado).strip().upper()
 
 
# =====================================================================
# B. LISTAS, BÚSQUEDA, FILTRADO Y ESTADÍSTICAS
#    Funcionan con objetos (atributos) y con diccionarios (claves).
# =====================================================================
def _valor(elemento, campo):
    """Lee `campo` de un diccionario o de un objeto."""
    if isinstance(elemento, dict):
        return elemento[campo]
    return getattr(elemento, campo)
 
 
def contiene_sin_mayusculas(texto, fragmento):
    """[EXAMEN] 'Rockrider ST100' contiene 'rock' -> True. Fragmento vacío -> False."""
    fragmento = str(fragmento).strip().casefold()
    return bool(fragmento) and fragmento in str(texto).casefold()
 
 
def buscar_en_campos(elementos, fragmento, campos):
    """[EXAMEN] Elementos cuyo texto contenga el fragmento en CUALQUIERA de los campos."""
    return [e for e in elementos
            if any(contiene_sin_mayusculas(_valor(e, c), fragmento) for c in campos)]
 
 
def filtrar_por(elementos, campo, valor):
    """[EXAMEN] Elementos con campo == valor (los textos, sin distinguir mayúsculas)."""
    if isinstance(valor, str):
        objetivo = valor.strip().casefold()
        return [e for e in elementos if str(_valor(e, campo)).strip().casefold() == objetivo]
    return [e for e in elementos if _valor(e, campo) == valor]
 
 
def ordenar_por(elementos, campo, descendente=False):
    """[EXAMEN] Lista nueva ordenada por un campo (no modifica la original)."""
    def clave(e):
        v = _valor(e, campo)
        return v.casefold() if isinstance(v, str) else v
    return sorted(elementos, key=clave, reverse=descendente)
 
 
def top_n(elementos, campo, n=3):
    """[EXAMEN-ampliación] Los n elementos con mayor valor del campo."""
    if n <= 0:
        return []
    return ordenar_por(elementos, campo, descendente=True)[:n]
 
 
def agrupar_por(elementos, campo):
    """[EXTRA] Diccionario valor_del_campo -> lista de elementos."""
    grupos = {}
    for e in elementos:
        grupos.setdefault(_valor(e, campo), []).append(e)
    return grupos
 
 
def contar_por(elementos, campo):
    """[EXAMEN] Diccionario valor_del_campo -> cantidad (p. ej. cartas por rareza)."""
    cuenta = {}
    for e in elementos:
        clave = _valor(e, campo)
        cuenta[clave] = cuenta.get(clave, 0) + 1
    return cuenta
 
 
def sumar_campo(elementos, campo):
    """[EXAMEN] Suma de un campo numérico (0 si la lista está vacía)."""
    return sum(_valor(e, campo) for e in elementos)
 
 
def media_campo(elementos, campo):
    """[EXAMEN] Media de un campo numérico; 0.0 si no hay elementos (evita dividir por 0)."""
    if not elementos:
        return 0.0
    return sumar_campo(elementos, campo) / len(elementos)
 
 
def maximo_por(elementos, campo):
    """[EXAMEN] Elemento con el mayor valor del campo, o None si no hay elementos."""
    if not elementos:
        return None
    return max(elementos, key=lambda e: _valor(e, campo))
 
 
def minimo_por(elementos, campo):
    """[EXTRA] Elemento con el menor valor del campo, o None si no hay elementos."""
    if not elementos:
        return None
    return min(elementos, key=lambda e: _valor(e, campo))
 
 
def claves_repetidas(elementos, campo):
    """[EXTRA] Lista de valores del campo que aparecen más de una vez."""
    vistos = set()
    repetidos = []
    for e in elementos:
        v = _valor(e, campo)
        if v in vistos and v not in repetidos:
            repetidos.append(v)
        vistos.add(v)
    return repetidos
 
 
def sin_duplicados(elementos, campo):
    """[EXAMEN] Conserva el primer elemento de cada valor del campo (evita duplicados)."""
    vistos = set()
    resultado = []
    for e in elementos:
        v = _valor(e, campo)
        if v not in vistos:
            vistos.add(v)
            resultado.append(e)
    return resultado
 
 
def porcentaje(parte, total):
    """[EXAMEN] parte*100/total (0.0 si total es 0). 1 inscrito de 2 plazas -> 50.0."""
    if not total:
        return 0.0
    return parte * 100 / total
 
 
# =====================================================================
# C. DINERO, DESCUENTOS E IMPORTES
# =====================================================================
def redondear_dinero(cantidad):
    """[EXAMEN] Redondea a 2 decimales."""
    return round(cantidad, 2)
 
 
def importe_linea(cantidad, precio_unitario):
    """[EXAMEN] cantidad x precio_unitario, a 2 decimales."""
    return redondear_dinero(cantidad * precio_unitario)
 
 
def calcular_descuento(subtotal, porcentaje_descuento):
    """[EXTRA] Importe del descuento: 54 y 10 -> 5.4."""
    return redondear_dinero(subtotal * porcentaje_descuento / 100)
 
 
def descuento_por_umbral(subtotal, umbral=50.0, porcentaje_descuento=10.0):
    """[EXAMEN] Descuento sobre el TOTAL solo si subtotal >= umbral; si no, 0.0."""
    if subtotal >= umbral:
        return calcular_descuento(subtotal, porcentaje_descuento)
    return 0.0
 
 
def total_con_descuento(subtotal, umbral=50.0, porcentaje_descuento=10.0):
    """[EXAMEN] 54 -> 48.6 ; 45 -> 45.0."""
    return redondear_dinero(subtotal - descuento_por_umbral(subtotal, umbral, porcentaje_descuento))
 
 
def precio_con_iva(precio, iva=21.0):
    """[EXTRA] Precio con IVA incluido."""
    return redondear_dinero(precio * (1 + iva / 100))
 
 
def importe_peluqueria(horas, precio_producto=0.0, tarifa=25.0):
    """[EXAMEN] horas x tarifa + producto (2 h + 40 € -> 90.0)."""
    return redondear_dinero(horas * tarifa + precio_producto)
 
 
def importe_teleconsulta(horas, tarifa=20.0):
    """[EXAMEN] horas x tarifa (1.5 h -> 30.0)."""
    return redondear_dinero(horas * tarifa)
 
 
# =====================================================================
# D. CÁLCULOS CANINOS Y FECHAS
# =====================================================================
def edad_humana(edad_perro):
    """[EXTRA] Equivalencia APROXIMADA en años humanos (1 año -> 15, 2 -> 24, +5 por año)."""
    if edad_perro <= 0:
        return 0
    if edad_perro == 1:
        return 15
    return 24 + (edad_perro - 2) * 5
 
 
def etapa_vida(edad):
    """[EXTRA] CACHORRO (<1), ADULTO (<8) o SENIOR."""
    if edad < 1:
        return "CACHORRO"
    if edad < 8:
        return "ADULTO"
    return "SENIOR"
 
 
def categoria_por_peso(peso_kg):
    """[EXTRA] PEQUEÑO (<10 kg), MEDIANO (<25), GRANDE (<45) o GIGANTE."""
    if peso_kg < 10:
        return "PEQUEÑO"
    if peso_kg < 25:
        return "MEDIANO"
    if peso_kg < 45:
        return "GRANDE"
    return "GIGANTE"
 
 
def racion_diaria_gramos(peso_kg, porcentaje_peso=2.5):
    """[EXTRA] Ración diaria ORIENTATIVA (% del peso corporal). Consulta siempre al veterinario."""
    return round(peso_kg * 1000 * porcentaje_peso / 100)
 
 
def a_fecha(texto):
    """[EXTRA] 'AAAA-MM-DD' -> date, o None si no es una fecha válida."""
    try:
        return date.fromisoformat(str(texto).strip())
    except ValueError:
        return None
 
 
def proxima_fecha(fecha_iso, dias=365):
    """[EXTRA] Fecha ISO dentro de `dias` días (p. ej. próxima vacuna). None si es inválida."""
    base = a_fecha(fecha_iso)
    if base is None:
        return None
    return (base + timedelta(days=dias)).isoformat()
 
 
def dias_hasta(fecha_iso, hoy_iso=None):
    """[EXTRA] Días que faltan hasta una fecha (negativo si ya pasó). None si es inválida."""
    destino = a_fecha(fecha_iso)
    hoy = a_fecha(hoy_iso) if hoy_iso is not None else date.today()
    if destino is None or hoy is None:
        return None
    return (destino - hoy).days
 
 
def esta_vencida(fecha_iso, hoy_iso=None):
    """[EXTRA] True si la fecha ya pasó (p. ej. vacuna caducada). None si es inválida."""
    dias = dias_hasta(fecha_iso, hoy_iso)
    if dias is None:
        return None
    return dias < 0
 
 
# =====================================================================
# E. FORMATO DE TEXTO Y MENÚS (devuelven cadenas; imprime main())
# =====================================================================
def formatear_euros(cantidad):
    """[EXAMEN] 48.6 -> '48.60 €'."""
    return f"{cantidad:.2f} €"
 
 
def formatear_kg(peso):
    """[EXAMEN] 30 -> '30.0 kg'."""
    return f"{peso:.1f} kg"
 
 
def formatear_porcentaje(valor):
    """[EXAMEN] 50 -> '50.0 %'."""
    return f"{valor:.1f} %"
 
 
def separador(longitud=40, caracter="-"):
    """[EXTRA] Línea de separación."""
    return caracter * longitud
 
 
def texto_menu(titulo, opciones):
    """[EXAMEN] Construye el texto del menú. `opciones` = lista de (clave, texto)."""
    lineas = [f"\n========== {titulo} =========="]
    lineas += [f"{clave}. {texto}" for clave, texto in opciones]
    return "\n".join(lineas)
 
 
def opcion_valida(opcion, opciones):
    """[EXAMEN] True si la opción tecleada está en la lista de (clave, texto)."""
    return str(opcion).strip() in [clave for clave, _ in opciones]
 
 
def tabla_texto(cabeceras, filas):
    """[EXTRA] Tabla alineada en texto plano; las columnas se ajustan al contenido."""
    filas = [[str(valor) for valor in fila] for fila in filas]
    anchos = [len(str(c)) for c in cabeceras]
    for fila in filas:
        for i, valor in enumerate(fila):
            anchos[i] = max(anchos[i], len(valor))
    def linea(valores):
        return " | ".join(str(v).ljust(anchos[i]) for i, v in enumerate(valores))
    resultado = [linea(cabeceras), "-+-".join("-" * a for a in anchos)]
    resultado += [linea(fila) for fila in filas]
    return "\n".join(resultado)
 
 
# =====================================================================
# F. CSV
#    Siempre: csv estándar, with open(...), encoding="utf-8", newline="".
# =====================================================================
def existe_archivo(ruta):
    """[EXTRA] True si el fichero existe."""
    return Path(ruta).is_file()
 
 
def leer_csv(ruta, campos):
    """[EXAMEN] Lista de diccionarios (todo texto). ValueError si la cabecera no coincide.
 
    Lanza OSError/FileNotFoundError si el fichero no se puede abrir.
    """
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != list(campos):
            raise ValueError("Las columnas del CSV no tienen el formato esperado")
        return list(lector)
 
 
def escribir_csv(ruta, campos, filas):
    """[EXAMEN] Sobrescribe el CSV con cabecera + filas (diccionarios). Devuelve True."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(campos))
        escritor.writeheader()
        escritor.writerows(filas)
    return True
 
 
def anadir_fila_csv(ruta, campos, fila):
    """[EXTRA] Añade una fila al final; escribe la cabecera si el fichero no existe o está vacío."""
    ruta = Path(ruta)
    escribir_cabecera = not ruta.is_file() or ruta.stat().st_size == 0
    with open(ruta, "a", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(campos))
        if escribir_cabecera:
            escritor.writeheader()
        escritor.writerow(fila)
    return True
 
 
def contar_filas_csv(ruta, campos):
    """[EXTRA] Número de filas de datos (sin la cabecera)."""
    return len(leer_csv(ruta, campos))
 
 
def copia_seguridad(ruta):
    """[EXTRA] Copia 'fichero.csv' como 'fichero.csv.bak' y devuelve la ruta de la copia."""
    origen = Path(ruta)
    destino = origen.with_name(origen.name + ".bak")
    shutil.copyfile(origen, destino)
    return destino
 
 
def convertir_fila(fila, conversiones):
    """[EXAMEN] Convierte campos de texto a su tipo: {"edad": int, "peso": float}.
 
    Acepta coma decimal. Lanza ValueError si algún valor no se puede convertir.
    Devuelve una copia; la fila original no se modifica.
    """
    resultado = dict(fila)
    for campo, funcion in conversiones.items():
        valor = resultado.get(campo)
        try:
            if isinstance(valor, str) and funcion is float:
                valor = valor.replace(",", ".")
            resultado[campo] = funcion(valor)
        except (TypeError, ValueError):
            raise ValueError(f"Valor no válido en la columna '{campo}': {valor!r}") from None
    return resultado
 
 
def agrupar_filas(filas, clave):
    """[EXAMEN] Agrupa filas por una columna manteniendo el orden.
 
    Para reconstruir ventas: una fila por línea, agrupadas por 'numero'.
    """
    grupos = {}
    for fila in filas:
        grupos.setdefault(fila[clave], []).append(fila)
    return grupos
 
 
def separar_por_referencias(filas, campo, claves_validas):
    """[EXAMEN] (validas, invalidas) según si fila[campo] está en claves_validas.
 
    Sirve para no crear inscripciones a emails o talleres inexistentes al cargar.
    """
    validas = []
    invalidas = []
    for fila in filas:
        if str(fila.get(campo, "")).strip() in claves_validas:
            validas.append(fila)
        else:
            invalidas.append(fila)
    return validas, invalidas
 
 
# =====================================================================
# G. CÓDIGOS Y FÁBRICA DE SUBTIPOS (HERENCIA)
# =====================================================================
def generar_codigo(prefijo, existentes, ancho=2):
    """[EXTRA] Siguiente código libre: ('PR', ['PR01','PR04']) -> 'PR05'."""
    prefijo = str(prefijo).upper()
    mayor = 0
    for codigo in existentes:
        codigo = str(codigo).strip().upper()
        if codigo.startswith(prefijo) and codigo[len(prefijo):].isdigit():
            mayor = max(mayor, int(codigo[len(prefijo):]))
    return f"{prefijo}{mayor + 1:0{ancho}d}"
 
 
def siguiente_numero(numeros):
    """[EXAMEN] Siguiente número correlativo (1 si no hay ninguno)."""
    return max(numeros, default=0) + 1
 
 
def fabricar(tipo, clases_por_tipo, *args, **kwargs):
    """[EXAMEN] Crea el subtipo correcto según el campo `tipo` del CSV.
 
    clases_por_tipo = {"PELUQUERIA": Peluqueria, "TELECONSULTA": Teleconsulta}
    ValueError si el tipo es desconocido (se rechazan los tipos no previstos).
    """
    clave = str(tipo).strip().upper()
    if clave not in clases_por_tipo:
        raise ValueError(f"Tipo desconocido: {tipo!r}")
    return clases_por_tipo[clave](*args, **kwargs)
 