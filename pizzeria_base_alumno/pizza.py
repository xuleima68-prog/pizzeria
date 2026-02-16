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

        emojis_ingredientes = []
        emojis_ingredientes.append(self.__ingredientes.append(self.))
        print(emojis_ingredientes)
        return """      
                         🍞🍞🍞🍞🍞🍞🍞🍞🍞
                       🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞
                      🍞🍅{               }🍅🍞  
                     🍞🍅{                 }🍅🍞
                    🍞🍅{                   }🍅🍞
                    🍞🍅{                   }🍅🍞
                    🍞🍅{                   }🍅🍞
                    🍞🍅{                   }🍅🍞     
                     🍞🍅{                 }🍅🍞      
                      🍞🍅{               }🍅🍞       
                       🍞🍅🍅🍅🍅🍅🍅🍅🍅🍅🍞        
                         🍞🍞🍞🍞🍞🍞🍞🍞🍞
            """
    




