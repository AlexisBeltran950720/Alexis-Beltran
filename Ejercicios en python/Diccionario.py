nombres = []
edades = []
nombresedades = {}
ndepersonas = int(input("Cuantas personas deseas agreagar\n"))
for i in range(ndepersonas):
    print("Ingresa el nombre")
    nombre = input()
    print("Ingresa la edad")
    edad = int(input())
    nombres.append(nombre)
    edades.append(edad)
nombresedades = dict(zip(nombres,edades))
print("La informacion en el diccionario es :",nombresedades)