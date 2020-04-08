def Enumeracion(objetivo, respuesta):
    while respuesta**2 < objetivo:
    ##print(respuesta)
        respuesta += 1.0

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')





objetivo = int(input('Escoge un entero:'))
metodo = input('Mediante que metodo te gustaria encontrar la raiz cuadrada?, escribe E para enumeración exhaustiva, A para aproximacion o B para busqueda binaria: ')
respuesta = 0.0

if metodo == 'E':
    Enumeracion(objetivo, respuesta)



