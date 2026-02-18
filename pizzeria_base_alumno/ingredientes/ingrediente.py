class Ingrediente:
    """
    Clase base que representa un ingrediente de una pizza.
    """

    def __init__(self, nombre, simbolo, precio):
        self.__nombre = nombre
        self.__simbolo = simbolo
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_simbolo(self):
        return self.__simbolo

#ampliación

    def get_precio(self):
        return self.__precio
    