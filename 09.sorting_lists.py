# Ordenar listas
fruits = ["Mango" , "Piña" , "Guindas" , "Guayaba" , "Maracuya"]

# Ordenamos con el metodo sort()
# fruits.sort()
fruits.sort(reverse = True)
print(fruits)

grades =[10,9,8,10,8,8]
grades.sort(reverse = True)
print(grades)

# Atencion: No funciona con listas que contienen elementos mixtos
cat_bag =[12, "Hola", True]
#cat_bag.sort()
#print(cat_bag)

# Cuidado con las mayusculas
veggie_list = ["Papas" , "Quinoa" , "Maiz" , "Choclito" , "papitas"]

#veggie_list.sort()
veggie_list.sort(key = str.lower)
print(veggie_list)