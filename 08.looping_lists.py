todo_list = ["Sacar la basura" , "Barrer la entrada" , "Pasear al boby" , "Regar las plantas"]

# Partir recorriendo con el clasico "for"
for todo in todo_list:
    print(todo)

print("-----------------")
# Tambien podemos utilizar la estructura de control "while"

index = 0
while index < len (todo_list):
    print(todo_list[index])
    index += 1

print("-----------------")

#Hay otra forma de recorre las lista
# Una forma mas avanzada utilizando list comprehensios
[print(todo) for todo in todo_list]

