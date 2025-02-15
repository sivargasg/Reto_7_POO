class MenuItem:
    """
    Representa un ítem del menú con un nombre y un precio.

    Atributos:
        name (str): El nombre del ítem.
        price (float): El precio del ítem.

    Métodos:
        calcular_precio_total(): Devuelve el precio del ítem.
    """
    def __init__(self, name: str, price: float):
        """
        Inicializa un nuevo ítem del menú con un nombre y un precio.

        Args:
            name (str): El nombre del ítem.
            price (float): El precio del ítem.
        """
        self.name = name
        self.price = price

    def calcular_precio_total(self):
        """
        Calcula el precio total del ítem.

        Returns:
            float: El precio del ítem.
        """
        return self.price


class Bebida(MenuItem):
    """
    Representa una bebida en el menú.

    Atributos:
        tamaño (str): El tamaño de la bebida.

    Hereda de:
        MenuItem
    """
    def __init__(self, name: str, price: float, tamaño: str):
        """
        Inicializa una nueva bebida con un nombre, un precio y un tamaño.

        Args:
            name (str): El nombre de la bebida.
            price (float): El precio de la bebida.
            tamaño (str): El tamaño de la bebida.
        """
        super().__init__(name, price)
        self.tamaño = tamaño


class Aperitivo(MenuItem):
    """
    Representa un aperitivo en el menú.

    Atributos:
        porción (str): La porción del aperitivo.

    Hereda de:
        MenuItem
    """
    def __init__(self, name: str, price: float, porción: str):
        """
        Inicializa un nuevo aperitivo con un nombre, un precio y una porción.

        Args:
            name (str): El nombre del aperitivo.
            price (float): El precio del aperitivo.
            porción (str): La porción del aperitivo.
        """
        super().__init__(name, price)
        self.porción = porción


class PlatoPrincipal(MenuItem):
    """
    Representa un plato principal en el menú.

    Atributos:
        acompañamientos (list): Lista de acompañamientos del plato principal.

    Hereda de:
        MenuItem
    """
    def __init__(self, name: str, price: float, acompañamientos: list):
        """
        Inicializa un nuevo plato principal con un nombre, un precio y una lista de acompañamientos.

        Args:
            name (str): El nombre del plato principal.
            price (float): El precio del plato principal.
            acompañamientos (list): Lista de acompañamientos del plato principal.
        """
        super().__init__(name, price)
        self.acompañamientos = acompañamientos


class Orden:
    """
    Representa una orden en el restaurante.

    Atributos:
        items (list): Lista de ítems del menú en la orden.

    Métodos:
        agregar_item(item): Agrega un ítem del menú a la orden.
        calcular_total(): Calcula el total de la orden.
        aplicar_descuento(porcentaje): Aplica un descuento al total de la orden.
    """
    def __init__(self):
        """
        Inicializa una nueva orden con una lista vacía de ítems.
        """
        self.items = []

    def agregar_item(self, item: MenuItem):
        """
        Agrega un ítem del menú a la orden.

        Args:
            item (MenuItem): El ítem del menú a agregar.
        """
        self.items.append(item)

    def calcular_total(self):
        """
        Calcula el total de la orden sumando los precios de todos los ítems.

        Returns:
            float: El total de la orden.
        """
        return sum(item.calcular_precio_total() for item in self.items)

    def aplicar_descuento(self, porcentaje: float):
        """
        Aplica un descuento al total de la orden.

        Args:
            porcentaje (float): El porcentaje de descuento a aplicar.

        Returns:
            float: El total de la orden con el descuento aplicado.
        """
        total = self.calcular_total()
        return total * (1 - porcentaje / 100)


menu = [
    Bebida("Nuka-Cola", 2.0, "Mediana"),
    Bebida("Agua", 1.0, "Media"),
    Bebida("Jugo de Fresa", 1.5, "Mediana"),
    Aperitivo("Papas Fritas", 2.0, "Grande"),
    Aperitivo("Plátano Maduro", 2.0, "Mediana"),
    Aperitivo("Ahuyama", 3.5, "Mediana"),
    PlatoPrincipal("Arroz con Pollo", 6.0, ["Papas Fritas", "Ensalada"]),
    PlatoPrincipal("Ensalada", 4.5, ["Vinagreta"]),
    PlatoPrincipal("Pechuga Asada", 6.0, ["Arroz", "Ensalada"]),
    PlatoPrincipal("Pizza", 8.5, ["Jugo"])
]

orden = Orden()
orden.agregar_item(menu[2])
orden.agregar_item(menu[5])
orden.agregar_item(menu[8])

print(f"Total sin descuento: {orden.calcular_total()}")
print(f"Total con descuento del 10%: {orden.aplicar_descuento(10)}")

