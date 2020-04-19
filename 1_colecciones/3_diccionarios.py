# Diccionario, conjunto de elementos compuestos por clave:valor

diccionario = {
    'clave1': 'valor1',
    'a': 1,
    'España': 'Madrid',
    'Alemania': 'Berlin',
    'Reino Unido': 'Londres'}

# +++ Obtener elemento

# Obtiene el elemento con la clave especificada,no genera error en caso de no existir
elem = diccionario.get('Alemania')

valor_defecto = diccionario.setdefault('Monaco',
                                       'valor_defecto')  # Obtiene el valor de la key o el valor por defecto en caso de que no exista

# Obtiene el elemento con la clave especificada, genera error en caso de no existir
capital = diccionario['España']

# +++ Modificar elemento
diccionario['clave1'] = 'Capitales'

# +++ Añadir elemento
diccionario['Paris'] = 'Francia'

# +++ Eliminar elementos
del diccionario['a']  # Elinina el elemento con la clave 'a'

elemento = diccionario.pop('España')  # Elimina (y devuelve el valor) del elemento con la clave 'España'

clave_valor = diccionario.popitem()  # Elimina y devueklve la clave:valor del ultimo elemento, error en caso de que el diccionario esté vacio

# +++Obtener todos los valores de un diccionario ( como view objects https://docs.python.org/3.8/library/stdtypes.html#dict-views)
valores = diccionario.values()

# +++ Obtener todas las claves de un diccionario ( como view objects https://docs.python.org/3.8/library/stdtypes.html#dict-views)
claves = diccionario.keys()


# Usar lista/tuplas para crear las claves de un diccionario (valores vacios)
diccionario_dinamico = {}
tupla_claves = ('nombre', 'apellido', 'profesion')
diccionario_dinamico = diccionario_dinamico.fromkeys(tupla_claves)

print(claves)
