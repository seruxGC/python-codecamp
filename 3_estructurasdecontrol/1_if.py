verdadero = True
falso = False
cinco = 5


def uno_mayor_cero():
    return 1 > 0


def uno_menor_cero():
    return 1 < 0


if verdadero:
    print('Escribo verdadero')

if uno_menor_cero():
    print('Uno menor cero')
elif uno_mayor_cero():
    print('Uno mayor cero')

if not verdadero:
    print('La variable es falsa')
else:
    print('La variable es verdadera')

if ( falso or falso ) or ( not verdadero or falso):
    print('Pasa validacion')
else:
    print('No pasa validacion')


