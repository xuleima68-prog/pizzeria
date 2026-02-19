class Pizza:
    def __init__(self, nombre, precio = 10):
        self.__nombre = nombre
        self.__ingredientes = []
        self.__precio = precio
    def get_nombre(self):
        return self.__nombre

    def add_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)

    def imprimir_ascii(self):
        """TODO: devolver dibujo ASCII de la pizza"""
        queso = 0
        vegetal = 0
        carne = 0
        emojis_ing= []
        for ingrediente in self.__ingredientes:
            emojis_ing.append(ingrediente.get_simbolo())
        str_emoji= "".join(emojis_ing)
        for emoji in emojis_ing:
            if emoji == "🧀":
                queso +=1
            elif emoji == "🌱":
                vegetal += 1
            elif emoji == "🥩":
                carne += 1
        
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
