class Pizza:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ingredientes = []
        
    def get_nombre(self):
        return self.__nombre

    def add_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)

    def calcular_precio(self):
        precio_pizza = 0
        for ingrediente in self.__ingredientes:
            precio_pizza += ingrediente.get_precio()
        return precio_pizza

    def imprimir_ascii(self):
        str_emoji = ""
        for ingrediente in self.__ingredientes:
            if ingrediente.get_simbolo() not in str_emoji:
                str_emoji += ingrediente.get_simbolo()

        return f"""
            {"  "}{"🍞"*(len(str_emoji)+2)}
            🍞{"🍅"*(len(str_emoji)+2)}🍞
            {"🍞🍅"}{str_emoji}{"🍅🍞"}
            {"🍞🍅"}{str_emoji}{"🍅🍞"}
            {"🍞🍅"}{str_emoji}{"🍅🍞"}
            {"🍞🍅"}{str_emoji}{"🍅🍞"}
            {"🍞🍅"}{str_emoji}{"🍅🍞"}
            🍞{"🍅"*(len(str_emoji)+2)}🍞
            {"  "}{"🍞"*(len(str_emoji)+2)}
        """
