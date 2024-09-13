nveces = int(input("Ingrese hasta que numero desea la secuencia:"))
num1 = 0
num2 = 1
secfibonacci = []
for i in range(nveces):
    secfibonacci.append(num1)
    num1,num2 = num2, num1 + num2    
separado = '-' .join(map(str,secfibonacci)) 
print("Serie fibonacci")
print(separado)