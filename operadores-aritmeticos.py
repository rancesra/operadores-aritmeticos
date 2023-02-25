# programa para implementar los operadores aritmeticos

print("----------------------------------------------")
print("--------------OPERADORES ARITMETICOS----------")
print("----------------------------------------------")

# INPUT

x = int(input("DIGITE EL VALOR DE X: "))
y = int(input("DIGITE EL VALOR DE Y: "))

# processing

s =  x + y
r = x - y
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

#output

print("----------------------------------------------")
print("---------------------RESULTADOS---------------")
print("----------------------------------------------")

print("SUMA: " + str(s))
print("RESTA: " + str(r))
print("MULTIPLICACION: " + str(m))
print("DIVISION: " + str(d))
print("MODULO: " + str(mod))
print("DIVISION PARTE ENTERA: " + str(de))
print("POTENCIA: " + str(p))