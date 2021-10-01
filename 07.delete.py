todo_list = ["Hacer la cama" , "Barrer el patio" , "Comer menos azucar"]

# Podemos eliminar elementos de listas con el metodo remove ()

# todo_list.remove("Hacer la cama")

# print(todo_list)

# Podemos eliminar elementos por su indice con el pop

# todo_list.pop(1)

# print(todo_list)

# Si llamamos al metodo pop() sin argumentos se elimina el ultimo elemento

# todo_list.pop()

# print(todo_list)

# Tambien tenemos el metodo especial "del". Este es un metodo especial y no tan frecuente
# Podemos pasar el indice para eliminar un elemento espeficico

del todo_list[1]

print(todo_list)

# O eliminar la coleccion completa, Incluyendo la variable referencial

del todo_list
# print(todo_list)

todo_list = ["Hacer la cama" , "Barrer el patio" , "Comer menos azucar"]

# Existe ademas el metodo clear() para vaciar la lista

todo_list.clear()
print(todo_list)