#funciones
def funcion(palabra="defecto"): #"def" palabra reservada para definir una funcion
    print("primera funcion "+palabra)

funcion()
funcion("prueba")
#dos formas de definir funciones
def suma(num1,num2):
    return num1+num2
print(suma(4,5))

sumar = lambda num1,num2: num1 + num2
print(sumar(8,6))
