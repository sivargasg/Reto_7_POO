from queue import Queue
from collections import namedtuple
import json

class MenuItem:
    """
    Representa un ítem del menú con un nombre y un precio.
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
    Representa una bebida en el menú, que hereda de MenuItem.
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
    Representa un aperitivo en el menú, que hereda de MenuItem.
    """
    def __init__(self, name: str, price: float, porcion: str):
        """
        Inicializa un nuevo aperitivo con un nombre, un precio y una porción.
        Args:
            name (str): El nombre del aperitivo.
            price (float): El precio del aperitivo.
            porcion (str): La porción del aperitivo.
        """
        super().__init__(name, price)
        self.porcion = porcion

class PlatoPrincipal(MenuItem):
    """
    Representa un plato principal en el menú, que hereda de MenuItem.
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
    
    def get_items(self):
        """
        Devuelve una lista de descripciones de los ítems en la orden.
        Returns:
            list: Lista de descripciones de los ítems en la orden.
        """
        items = []
        for item in self.items:
            descripcion = [item.name]
            if isinstance(item, Bebida):
                descripcion.append(item.tamaño)
            elif isinstance(item, Aperitivo):
                descripcion.append(item.porcion)
            elif isinstance(item, PlatoPrincipal):
                descripcion.append(item.acompañamientos)
            items.append(descripcion)
        return items

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

    @staticmethod
    def cargar_menu(ruta):
        """
        Carga un menú desde un archivo JSON.
        Args:
            ruta (str): La ruta del archivo JSON a cargar.
        Returns:
            MenuSet: Un objeto MenuSet con las listas de ítems del menú.
        """
        with open(ruta, 'r') as archivo:
            datos = json.load(archivo)
            bebidas = [Bebida(**item) for item in datos.get('bebidas', [])]
            aperitivos = [Aperitivo(**item) for item in datos.get('aperitivos', [])]
            platos_principales = [PlatoPrincipal(**item) for item in datos.get('platos_principales', [])]
            return MenuSet(bebidas=bebidas, aperitivos=aperitivos, platos_principales=platos_principales)

    @staticmethod
    def guardar_menu(menu, ruta):
        """
        Guarda un menú en un archivo JSON.
        Args:
            menu (MenuSet): El menú a guardar.
            ruta (str): La ruta del archivo JSON.
        """
        datos = {
            'bebidas': [item.__dict__ for item in menu.bebidas],
            'aperitivos': [item.__dict__ for item in menu.aperitivos],
            'platos_principales': [item.__dict__ for item in menu.platos_principales]
        }
        with open(ruta, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f'Menú guardado en {ruta}')
        
    @staticmethod
    def agregar_item_menu(menu, item, categoria):
        """
        Agrega un ítem al menú en la categoría especificada.
        Args:
            menu (MenuSet): El menú al que se agregará el ítem.
            item (MenuItem): El ítem a agregar.
            categoria (str): La categoría a la que se agregará el ítem ('bebidas', 'aperitivos' o 'platos_principales').
        """
        if categoria == 'bebidas':
            menu.bebidas.append(item)
        elif categoria == 'aperitivos':
            menu.aperitivos.append(item)
        elif categoria == 'platos_principales':
            menu.platos_principales.append(item)

    @staticmethod
    def actualizar_item_menu(menu, item, categoria, index):
        """
        Actualiza un ítem existente en el menú en la categoría especificada.
        Args:
            menu (MenuSet): El menú en el que se actualizará el ítem.
            item (MenuItem): El ítem actualizado.
            categoria (str): La categoría del ítem a actualizar ('bebidas', 'aperitivos' o 'platos_principales').
            index (int): El índice del ítem a actualizar.
        """
        if categoria == 'bebidas':
            menu.bebidas[index] = item
        elif categoria == 'aperitivos':
            menu.aperitivos[index] = item
        elif categoria == 'platos_principales':
            menu.platos_principales[index] = item

    @staticmethod
    def eliminar_item_menu(menu, categoria, index):
        """
        Elimina un ítem del menú en la categoría especificada.
        Args:
            menu (MenuSet): El menú del que se eliminará el ítem.
            categoria (str): La categoría del ítem a eliminar ('bebidas', 'aperitivos' o 'platos_principales').
            index (int): El índice del ítem a eliminar.
        """
        if categoria == 'bebidas':
            del menu.bebidas[index]
        elif categoria == 'aperitivos':
            del menu.aperitivos[index]
        elif categoria == 'platos_principales':
            del menu.platos_principales[index]

# Definición de la namedtuple MenuSet
MenuSet = namedtuple('MenuSet', ['bebidas', 'aperitivos', 'platos_principales'])

menu = MenuSet(
    bebidas=[
        Bebida("Nuka-Cola", 2.0, "Mediana"),
        Bebida("Agua", 1.0, "Media"),
        Bebida("Jugo de Fresa", 1.5, "Mediana")
    ],
    aperitivos=[
        Aperitivo("Papas Fritas", 2.0, "Grande"),
        Aperitivo("Plátano Maduro", 2.0, "Mediana"),
        Aperitivo("Ahuyama", 3.5, "Mediana")
    ],
    platos_principales=[
        PlatoPrincipal("Arroz con Pollo", 6.0, ["Papas Fritas", "Ensalada"]),
        PlatoPrincipal("Ensalada", 4.5, ["Vinagreta"]),
        PlatoPrincipal("Pechuga Asada", 6.0, ["Arroz", "Ensalada"]),
        PlatoPrincipal("Pizza", 8.5, ["Jugo"])
    ]
)

# Guardar el menú en un archivo JSON
Orden.guardar_menu(menu, "menu.json")

# Cargar el menú desde un archivo JSON
menu_cargado = Orden.cargar_menu('menu.json')

# Agregar una nueva bebida al menú
nueva_bebida = Bebida("Choca-colas", 2.5, "Grande")
Orden.agregar_item_menu(menu_cargado, nueva_bebida, 'bebidas')

bebida_actualizada = Bebida("Fan-Ta-Stick", 2.0, "Mediana")
Orden.actualizar_item_menu(menu_cargado, bebida_actualizada, 'bebidas', 0)

Orden.eliminar_item_menu(menu_cargado, 'aperitivos', 1)

Orden.guardar_menu(menu_cargado, 'menu_actualizado.json')

orden1 = Orden()
orden1.agregar_item(menu_cargado.aperitivos[1])   
orden1.agregar_item(menu_cargado.platos_principales[2])

orden2 = Orden()
orden2.agregar_item(menu_cargado.bebidas[0])

orden3 = Orden()
orden3.agregar_item(menu_cargado.platos_principales[1])

cola_FIFO = Queue(maxsize=3)

cola_FIFO.put(orden1)
cola_FIFO.put(orden2)
cola_FIFO.put(orden3)

if cola_FIFO.full():
    print("La fila se llenó")
else:
    print("Aún hay sitio en la fila")

contador = 1
while not cola_FIFO.empty():
    orden = cola_FIFO.get()
    print(f"Entregando orden {contador}")
    print("Entregando elemento:", orden.get_items())
    print(f"Total sin descuento: {orden.calcular_total()}")
    print(f"Total con descuento del 10%: {orden.aplicar_descuento(10)}")
    contador += 1

