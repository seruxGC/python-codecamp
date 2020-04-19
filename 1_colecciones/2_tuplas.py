# Tupla , conjunto de elementos inmutables (no se pueden añadir,eliminar, cambiar elementos )

# Ventajas respecto a las listas: Mas rapidas , menos espacio, formatean Strings, pueden usarse como claves en un diccionario

tupla = (1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'a')

tupla_un_elemento = ('elemento',)  # Se tiene que añadir una coma (,) al final del elemento

# +++ Obtener un elemento de la tupla
elemento2 = tupla[1]

# Asignar valores a variables de una tupla
date_tuple = (13, 2, 2020)
day, month, year = date_tuple
# day 13
# month 2
# year 2020

# +++ Comprobar si un elemento se encuentra dentro de una tupla
a_en_lista = 'a' in tupla  # True

# +++ Obtener el numero de veces que esta un elemento en la tupla
numero_veces_a = tupla.count('a')

# +++ Obtener numero de elementos que tiene la tupla
num_elementos = len(tupla)

# +++ Obtener indice de un elemento en la tupla
indice = tupla.index('a')

# +++ Convertir tupla en lista
lista = list(tupla)  # 2
