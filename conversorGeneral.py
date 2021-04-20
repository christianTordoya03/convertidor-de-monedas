menu = """
Bienvenido al conversor de monedas  $

1 - soles colombianos
2 - soles argentinos
3 - soles mexicanos
Elige una opcion: """

opcion = input(menu)

if opcion == "1":
    soles = input("How many soles mexicanos do you have?: ")
    soles = float(soles)
    valor_de_compra_dolar = 3.69
    dolares = soles / valor_de_compra_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")
elif opcion == "2":
    soles = input("How many soles colombianos do you have?: ")
    soles = float(soles)
    valor_de_compra_dolar = 3.19
    dolares = soles / valor_de_compra_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")
elif opcion == "3":
    soles = input("How many soles argentinos do you have?: ")
    soles = float(soles)
    valor_de_compra_dolar = 3.39
    dolares = soles / valor_de_compra_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")
else:
    print("Ingresa una opcion correcta por favor")
