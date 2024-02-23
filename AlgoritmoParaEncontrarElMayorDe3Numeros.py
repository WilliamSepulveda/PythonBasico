num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero:"))
num3 = float(input("ingrese el tercer numero:"))

if (num1> num2) and (num1> num3): largest = num1 
elif (num2> num1) and (num2> num3): largest = num2

else: largest = num3 
print ("el mayor numero es" , largest)


