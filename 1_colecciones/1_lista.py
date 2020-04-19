# Listas , conjunto de datos que pueden ser de distinto tipos y modificados
lista = [4, 3, 2, 1, 0, -1, -2, -3, -4]

lista_vacia = []

# +++ Obtener elemento en la posicion 1
elemento1 = lista[1]  # 3

# +++ Obtener un elemento empezando a contar del final (Ej: penultimo)
penultimo = lista[-2]  # -3

# Asignar valores a variables de una lista
date_list = [13, 2, 2020]
day, month, year = date_list
# day 13
# month 2
# year 2020

# +++Cambio valor elemento
lista[1] = 'valor cambiado'

# +++ Rangos lista[pos_ini:pos_final] (se empieza a contar en 0 y el elemento pos_final no esta incluido)
rango_3_6 = lista[3:6]  # De la posicion 3 a la sexta

rango_3_final = lista[3:]  # De la posicion 3 al final

rango_principio_3 = lista[:3]  # De la posicion 0 al hasta el tercero

rango_3_ultimos = lista[-3:]  # De la posicion -3 al final [-2, -3, -4]

rango_principio_penultimo = lista[:-2]  # Del principio hasta el penultimo [4, 'valor cambiado', 2, 1, 0, -1, -2]

rango_entero = lista[:]  # Todos los elementos

# +++ Añadir elementos a una lista
lista.append('Elemento añadido')  # Añadir elemento al final de la lista

lista.insert(3, 'Insertado')  # Añadir enelento en la posicion incicada

lista2 = ['a', 'b']  # Añadir elementos de otro objeto iterable
lista.extend(lista2)
lista.extend(['c', 'd'])

lista += ['w']  # Hace la misma funcion que extend
lista += lista2

lista_1 = [1, 2, 3]  # Unir listas
lista_2 = [1, 2, 3]
union_lista1_lista2 = lista_1 + lista_2  # [1, 2, 3, 1, 2, 3]

# +++ Eliminar elementos
lista.remove('valor cambiado')  # Elimina la primera ocurreccia que tenga el valor indicado en el parametro

del lista[3]  # Elimina el elemento de la lista con el indice 3

ultimo_elemento_borrado = lista.pop()  # Elimina ( y devuelve ) el ultimo valor de la lista

lista_2.clear()  # Elimina todos los elementos de una lista

del lista_1[1:]  # Elimina un rango de la lista, en este caso a del elemento con indice 1 al final

# +++ Comprobar si un elemento se encuentra dentro de una lista
a_en_lista = 'a' in lista  # True
e_en_lista = 'e' in lista  # False

# +++ Obtener indice de un elemento en la lista
indice_a = lista.index('a')  # Obtener el indice del primer elemento con valor 'a'

# +++ Obtener el numero de veces que esta un elemento en la lista
numero_veces_a = lista.count('a')

# +++ Obtener numero de elementos que tiene la lista
num_elementos = len(lista)

# +++ Ordenar lista
numeros = [5, 4, 2, 6, 2, 5]
numeros.sort()  # [2, 2, 4, 5, 5, 6]

# +++ Convertir lista en tupla
tupla = tuple(lista)

print(lista_1)
