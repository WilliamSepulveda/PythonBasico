n =int(input("ingresa el numero:"))
x = 1
y = 0
while x <= n:
    if n % x <= 0:
      y = y + 1
    x = x + 1 
if y == 2:
  print("el  numero" ,n, "es primo: ")
else:
  print("el numero " ,n, " no es primo: ")

    

