def mi_funcion():
    pass


mi_funcion()


def funcion_con_parametros(param1, param2):
    print(param1)
    print(param2)


funcion_con_parametros('hola', 'adios')


def funcion_con_return(param1):
    return param1


funcion_con_return('Carlos')


def funcion_parametros_defecto(param1='defecto'):
    print(param1)


funcion_parametros_defecto()


def funcion_parametros_keywords(modo, separador):
    print(separador + modo)


funcion_parametros_keywords(separador=',', modo='normal')
