
# CLASES PARA LA GESTION DE CONCIERTOS


# Clase principal Entrada
class Entrada:

    def __init__(self, concierto):
        self.concierto = concierto

    def get_precio_total(self):
        # Devuelve el precio base del concierto
        return self.concierto.precio_base

    def __str__(self):
        return f"Entrada general para {self.concierto.artista} - {self.get_precio_total():.2f} €"


# Clase EntradaGrada, hereda de Entrada
class EntradaGrada(Entrada):

    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    def get_precio_total(self):
        # La entrada de grada mantiene el precio base
        return self.concierto.precio_base

    def __str__(self):
        return f"Entrada de grada para {self.concierto.artista} - {self.get_precio_total():.2f} €"


# Clase EntradaPista, hereda de Entrada
class EntradaPista(Entrada):

    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    def get_precio_total(self):
        # La entrada de pista cuesta un 10% mas
        return self.concierto.precio_base * 1.10

    def __str__(self):
        return f"Entrada de pista para {self.concierto.artista} - {self.get_precio_total():.2f} €"


# Clase EntradaVIP, hereda de Entrada
class EntradaVIP(Entrada):

    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    def get_precio_total(self):
        # Con consumicion cuesta un 20% mas
        # Sin consumicion cuesta un 15% mas
        if self.incluye_consumicion:
            return self.concierto.precio_base * 1.20
        else:
            return self.concierto.precio_base * 1.15

    def __str__(self):
        return f"Entrada VIP para {self.concierto.artista} - {self.get_precio_total():.2f} €"


# Clase Concierto
class Concierto:

    def __init__(self, artista, ciudad, precio_base, aforo_maximo, activo=True):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = []
        self.activo = activo

    def calcular_recaudacion(self):
        # Suma el precio de todas las entradas vendidas
        recaudacion = 0.0

        for entrada in self.entradas_vendidas:
            recaudacion += entrada.get_precio_total()

        return recaudacion

    def calcular_precio_medio(self):
        # Evita dividir entre cero cuando no hay ventas
        if len(self.entradas_vendidas) == 0:
            return 0.0

        return self.calcular_recaudacion() / len(self.entradas_vendidas)

    def entradas_disponibles(self):
        # Comprueba si quedan entradas disponibles
        return len(self.entradas_vendidas) < self.aforo_maximo

    def __str__(self):
        return f"Concierto de {self.artista} en {self.ciudad}"


# Clase Usuario
class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.entradas_compradas = []
        self.conciertos_asistidos = set()
        self.valoraciones = {}

    def comprar_entrada(self, concierto, tipo_entrada):

        # Comprobar si el concierto esta activo
        if not concierto.activo:
            raise Exception("El concierto no esta activo.")

        # Comprobar si el usuario ya ha asistido
        if concierto in self.conciertos_asistidos:
            raise Exception("Ya has asistido a este concierto.")

        # Comprobar si quedan entradas disponibles
        if not concierto.entradas_disponibles():
            raise Exception("No quedan entradas disponibles.")

        # Crear la entrada segun el tipo seleccionado
        tipo = tipo_entrada.strip().lower()

        if tipo == "general":
            entrada = Entrada(concierto)

        elif tipo == "grada":
            entrada = EntradaGrada(concierto, "1A")

        elif tipo == "pista":
            entrada = EntradaPista(concierto, True)

        elif tipo == "vip":
            entrada = EntradaVIP(concierto, True)

        else:
            raise Exception("El tipo de entrada no es valido.")

        # Guardar la entrada en el concierto
        concierto.entradas_vendidas.append(entrada)

        # Guardar la entrada en el usuario
        self.entradas_compradas.append(entrada)

        # Registrar el concierto como asistido
        self.conciertos_asistidos.add(concierto)

    def valorar(self, concierto, valoracion):

        # Comprobar que el usuario haya asistido
        if concierto not in self.conciertos_asistidos:
            raise Exception("No has asistido a este concierto.")

        # Comprobar que la valoracion este entre 0 y 10
        if valoracion < 0 or valoracion > 10:
            raise Exception("La valoracion debe estar entre 0 y 10.")

        # Guardar o modificar la valoracion
        self.valoraciones[concierto] = valoracion

    def __str__(self):
        return f"{self.nombre} (ha asistido a {len(self.conciertos_asistidos)})"
