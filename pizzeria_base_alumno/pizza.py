class Pizza:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ingredientes = []

    def get_nombre(self):
        return self.__nombre

    def add_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)

    def imprimir_ascii(self):
        """TODO: devolver dibujo ASCII de la pizza"""

        emojis_ing= []
        for ingrediente in self.__ingredientes:
            emojis_ing.append(ingrediente.get_simbolo())
        
        str_emoji= "".join(emojis_ing)
        
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