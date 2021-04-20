def comprar(valor_de_venta):
    dolar = float(input("Cuantos dolares deseas comprar?: "))
    costo = dolar * valor_de_venta
    costo = round(costo, 2)
    costo = str(costo)
    print(f"{dolar}$ seria igual a {costo}soles")


def vender(valor_de_compra):
    dolar = float(input("Cuantos dolares deseas vender?: "))
    costo = dolar * valor_de_compra
    costo = round(costo, 2)
    costo = str(costo)
    print(f"{dolar}$ seria igual a {costo} soles")


def cambio(mensaje, valor_de_venta, valor_de_compra):
    print(mensaje)
    dolares = (input("Que transaccion deseas realizar, comprar o vender dolar?: "))
    if dolares == "comprar":
        comprar(valor_de_venta)
    elif dolares == "vender":
        vender(valor_de_compra)
    else:
        print("Elige una transaccion")


menu = """
*****************************************************************************************
Bienvenido a la plataforma de casas de cambio, tenemos las siguientes opciones! 

1 - tkambio
2 - $ tucambista
3 - cambio seguro
4 - cambiX
5 - dollar house

ELige una opcion:  
*****************************************************************************************
"""

opcion = int(input(menu))

if opcion == 1:
    cambio("Elegiste la casa de cambio tkambio!", 3.75, 3.95)
elif opcion == 2:
    cambio("Elegiste la casa de cambio $ tucambista!", 3.55, 3.85)
elif opcion == 3:
    cambio("Elegiste la casa de cambio cambio seguro!", 3.35, 3.45)
elif opcion == 4:
    cambio("Elegiste la casa de cambio cambiX!", 3.65, 3.35)
elif opcion == 5:
    cambio("Elegiste la casa de cambio dollar house!", 3.85, 3.55)
else:
    print("Elige una de las opciones")
