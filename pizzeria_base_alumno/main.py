from pizzeria import Pizzeria
from pedido import Pedido
from pizza import Pizza
from ingredientes.queso import Queso
from ingredientes.carne import Carne
from ingredientes.vegetal import Vegetal

def main():
    print("""
  ▄▄▄▄▄▄     ▄▄▄▄▄▄  ▄▄▄▄▄▄     ▄▄▄▄▄       ▄▄      ▄▄▄▄▄   
 █▀██▀▀▀█▄  █▀ ██   █▀██▀▀▀█▄  ██▀▀▀▀█▄   ▄█▀▀█▄   ██▀▀▀▀█▄ 
   ██▄▄▄█▀     ██     ██▄▄▄█▀  ▀██▄  ▄▀   ██  ██   ▀██▄  ▄▀ 
   ██▀▀▀       ██     ██▀▀▀      ▀██▄▄    ██▀▀██     ▀██▄▄  
 ▄ ██          ██   ▄ ██       ▄   ▀██▄ ▄ ██  ██   ▄   ▀██▄ 
 ▀██▀        ▄▄██▄▄ ▀██▀       ▀██████▀ ▀██▀  ▀█▄█ ▀██████▀ 
""")
    pizzeria = Pizzeria()
    pedido = Pedido()

    while True:
        pizzeria.mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            nombre_pizza = input("Dale un nombre a tu pizza: ")
            pizza = Pizza(nombre_pizza)
            # TODO: añadir ingredientes
            # muestra al usuario opciones para que elija qué ingredientes quiere añadir a su pizza, 
            # hasta que elija la opción de terminar pizza
            # Por ejemplo, así añadiría Queso y después terminaría la pizza.
            
            while True:
                print("""
Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza                      
""")
                opcion_ingrediente = input("Elige un ingrediente: ")
                if opcion_ingrediente == "1":
                    pizza.add_ingrediente(Queso)
                elif opcion_ingrediente == "2":
                    pizza.add_ingrediente(Carne)
                elif opcion_ingrediente == "3":
                    pizza.add_ingrediente(Vegetal)
                elif opcion_ingrediente == "0":
                    break
                else:
                    break
            """
                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza
                Elige ingrediente: 1

                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza
                Elige ingrediente: 0
            """
            print("ingredientes")

            pedido.add_pizza(pizza)
        elif opcion == "2":
            pedido.mostrar_pedido()
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()

