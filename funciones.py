# def imprimir_mensaje():
#     print("mensaje especial: ")
#     print("estoy aprendiendo a usar funciones en python!")


# imprimir_mensaje()

def conversacion(mensaje):
    print("hola")
    print(mensaje)
    print("adios")


opcion = int(input("ELige una opcion(1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else:
    print("escribe la opcion correcta")
