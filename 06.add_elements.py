todo_list = ["Sacar la basura" , "Barrer la entrada" , "Pasear al boby" , "Regar las plantas"]

# Para agregar elementos podemos utilizar la funcion insert () que viene en todas las listas. El primer parámetro es el índice que ocupara el nuevo elemento

todo_list.insert(2, "Dejar la Cocacola")

# Podemos agregar directamente al final con el metodo append () que tambien viene en todas las lista

todo_list.append("Cocinar saludable")

print(todo_list)

# Mezclar listas

movies = ["Matrix" , "Wars Star" , " El viejo de las argollas"]
books = ["Poemas de Baldor" , "Chiste de Proschle" , "Horoscopo Xino"]

# El metodo extend incorpora al arreglo lo que se esta extendiendo
movies.extend(books)
# Aca movies tendra el contenido de ambas listas
print(movies)
# La lista books sigue existiendo
print(books)
