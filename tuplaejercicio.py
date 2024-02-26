nombre = input("ingresa tu nombre: ")
edad = input("ingresa tu edad: ")
id  = input("ingresa tu numero de documento: ")
altura = input("ingresa tu altura: ")
 
info = (nombre, edad, altura)

direcc = input("ingresa tu direccion de residencia: ")
edu = input("ingresa tu nivel de educacion: ")
explaboral = input("ingresa cual es tu experiencia laboral: ")

info = (f""" tu nombre es {nombre}, con una edad de {edad}, con numero de documento {id}, su altura es de {altura}, vives en {direcc},tus estudios son {edu}, y cuentas con una experiencia en {explaboral}""")

print(info)

