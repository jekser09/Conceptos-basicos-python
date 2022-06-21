#Caracteristicas String "str"
myStr="Hola Mundo"
print(dir(myStr))
#el motodo dir() nos mostrara los metodos que podemos utilizar en la variable myStr
#metodos ejemplos
print("--------------------")
print("metodo upper: ",myStr.upper()) #texto a mayusculas
print("--------------------")
print("metodo lower: ",myStr.lower()) #texto a minusculas
print("--------------------")
print("metodo swapcase: ",myStr.swapcase()) #intercambia mayusculas con minusculas y tambien al contrario
print("--------------------")
print(myStr.replace('Hola','Adios')) #reemplazar una palabra con otra
print(myStr.replace('Hola','Adios').upper()) #Lammar un metodo desde otro
print("--------------------")
print(myStr)
print("cantidad de o: ",myStr.count('o')) #contar caracteres
print("--------------------")
print(myStr) 
print("empieza con la palabra 'Hello'?: ",myStr.startswith("Hello")) #saber si una cadena empieza con una palabra
print("empieza con la palabra 'Hola'?: ",myStr.startswith("Hola"))
print("----------")
myStr[3]
print(f"hola {myStr}")