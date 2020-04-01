#frutas = ['manzana', 'pera', 'mango']
#for fruta in frutas:
        #print(frutas)


#>>> iter('cadena') # cadena
#>>> iter(['a', 'b', 'c']) # lista
#>>> iter(('a', 'b', 'c')) # tupla
#>>> iter({'a', 'b', 'c'}) # conjunto
#>>> iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

frutas = ['manzana', 'pera', 'mango']
iterador = iter(frutas)
next(iterador)
next(iterador)
next(iterador)


estudiantes = {
    'Mexico': 10,
    'Colombia': 15,
    'Puerto rico': 4,
}

for pais in estudiantes:
    print(pais)

for pais in estudiantes.keys():
     print(pais)

for numero_de_estudiantes in estudiantes.values():
     print(numero_de_estudiantes)

for pais, numero_de_estudiantes in estudiantes.items():
	print(f'pais: {pais} numero_de_estudiantes: {numero_de_estudiantes}')