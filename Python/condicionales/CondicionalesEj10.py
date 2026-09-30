
#! La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#!     · Ingredientes vegetarianos: Pimiento y tofu.
#!     · Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#! Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
#! Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida
#! es vegetariana o no y todos los ingredientes que lleva.

vegetariana = "Pimiento, Tofu, Mozzarella, Tomate"
no_vegetariana = "Peperoni, Jamón, Salmón, Mozzarella, Tomate"

tipo_pizza = input("¿Que tipo de pizza desea? (vegetariana/no vegetariana): ").lower()

if tipo_pizza == "vegetariana":
    print("Ingredientes pizza Vegetariana: ")
    print(vegetariana)
    ingrediente = input("Introduce un ingrediente a mayores: ")
    print("==== Tipo de pizza elegida:",tipo_pizza,"====")
    print("Ingredientes: ",vegetariana,"y", ingrediente)
elif tipo_pizza == "no vegetariana":
    print("Ingredientes pizza No Vegetariana: ")
    print(no_vegetariana)
    ingrediente = input("Introduce un ingrediente a mayores: ")
    print("==== Tipo de pizza elegida:",tipo_pizza,"====")
    print("Ingredientes: ",no_vegetariana,"y", ingrediente)
else:
    print("Solo hay vegetariana y no vegetariana")



