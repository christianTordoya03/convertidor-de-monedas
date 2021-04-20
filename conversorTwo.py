dolares_two = input("How many dolar do you have?: ")
dolares_two = float(dolares_two)
valor_de_venta_dolar = 3.66
comprar_soles = valor_de_venta_dolar * dolares_two
soles_two = round(comprar_soles, 2)
soles_two = str(soles_two)
print("Tienes $" + soles_two + " " + "soles")

soles = input("How many soles do you want to change?: ")
soles = float(soles)
valor_de_compra_dolar = 3.69
dolares = soles / valor_de_compra_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares +" " + "dolares") 