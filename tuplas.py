#tuplas
x=(1,2,3)
y=tuple((4,5,6))
print(y)
print(dir(x))
z=(1) #esto no es considerado una tupla
z=(1,) #tupla de un solo elemento

x[0]=1 #esto es un error por que una tupla no puede ser modificada

del x #elimina una variable

coordenadas={(10.1245,7895.4):"bogota",(21354.68,246.23):"medellin"}