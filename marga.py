
numero = 4752
print(numero)
print("----------- ")
numero1 = numero % 10
numero2= numero//10 % 10
numero3= numero//100 % 10
numero4 = numero//1000 

numerofinal = [numero1,numero2,numero3,numero4]
print(numerofinal)
numero = 7452
numero_invertido = int(str(numero)[::-1])

print(numero_invertido)