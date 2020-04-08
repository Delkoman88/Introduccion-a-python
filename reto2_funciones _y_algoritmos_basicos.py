def Enumeracion(objetivo, respuesta):
    while respuesta**2 < objetivo:
    ##print(respuesta)
        respuesta += 1.0

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')

def Aproximacion(objetivo, respuesta):
    epsilon = 0.001
    paso = epsilon**2
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
   ## print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def Busqueda_bin(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
        print (f'La raiz cuadrada de {objetivo} es {respuesta}')

objetivo = int(input('Escoge un entero:'))
metodo = input('Mediante que metodo te gustaria encontrar la raiz cuadrada?, escribe E para enumeración exhaustiva, A para aproximacion o B para busqueda binaria: ')
respuesta = 0.0

if metodo == 'E':
    Enumeracion(objetivo, respuesta)
elif metodo == 'A':
    Aproximacion(objetivo, respuesta)
elif metodo == 'B':
    Busqueda_bin(objetivo)
else:
    print('Por favor ingresa un metodo valido')



