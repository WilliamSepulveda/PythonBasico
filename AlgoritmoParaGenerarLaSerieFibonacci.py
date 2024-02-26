n = int(input("ingresa un numero: "))
a = 1
b = 1 
c = 1
while c <= n:
    if c % 2 == 1:
      print (a, end=",") 
      a += b
    
    else: 
     print(b, end=",")
    b += a
    c += 1


