# For x veces

for i in range(3):
    print(i)  # 0 , 1 , 2

# For X veces definiendo el rango del principio y final

for a in range(8, 10):
    print(a)  # 8, 9

# For definiendo el rango y el incremento en cada iteracion
for b in range(20, 30, 2):
    print(b)  # 20, 22, 24, 28

# Foreach

palabras = ['gato', 'ventana', 'defenestrado']

for elemento in palabras:
    print(elemento)  # gato ventana desfenestrado

# Foreach con indice

paises = ['España', 'Francia', 'Alemania', 'Reino Unido']

for indice, pais in enumerate(paises):
    print(indice, pais)  # 0 España   1 Francia   2 Alemania   3 Reino Unido

# Si se necesita modificar la secuencia sobre la que estás iterando mientras estás adentro del ciclo (por ejemplo para borrar
# algunos ítems), se recomienda que hagas primero una copia. Iterar sobre una secuencia no hace implícitamente una copia.
# La notación de rango es especialmente conveniente para esto:

for palabra in palabras[:]:  # hace una copia toda la lista
    if len(palabra) > 6:
        palabras.insert(0, palabra)

print(palabras)  # ['defenestrado', 'ventana', 'gato', 'ventana', 'defenestrado']
