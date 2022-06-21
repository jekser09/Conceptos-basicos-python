#listas
lista=[41,65,87,54,99]
colores=["rojo","amarillo","verde"]
listaEntreLista=[10,"palabra",False,[1,2,3]]
list() #metodo para crear listas
lista2=list((10,20))
range(1,20) #crea listas en un rango
lista3=list(range(1,100))
print(f"lista 3: {lista3}")
print("informacion sobre listas: ",dir(lista))
lista[2] #posicion de un elemento de la lista
41 in lista #pregunta si "41" esta en la lista
print("colores: ",colores)
print("esta rojo en los colores? ","rojo" in colores)
print("esta morado en los colores? ","morado" in colores)
colores[2]="morado"
print(colores)
colores.append("violeta") #añadir un elemento
print(colores)
colores.extend(["gris","negro"]) #añadir elementos
print(colores)
colores.insert(1,"magenta") #añadir un elemento en una posicion
print(colores)
len(colores) #metodo para saber el tamaño de una lista
colores.insert(len(colores),"rosa")
print(colores)
colores.pop() #quita el ultimo elemento de la lista
colores.pop(0) #quita un elemento segun su posicion
print(colores)
colores.remove("amarillo") #elimina un elemento de la lista
print(colores)
colores.clear() #limpia la lista entera
colores2=["rojo","azul","amarillo"]
colores2.sort() #ordena alfabeticamente
colores2.sort(reverse=True) #ordena al contrario
colores2.index() #indica la posicion de un elemento
print("donde esta amarillo?: ",colores2.index("amarillo"))
colores2.count() #para contar cuantas veces hay un elemento
print(colores2.count("rojo"))
