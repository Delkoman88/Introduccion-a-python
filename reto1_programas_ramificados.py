persona1 = input('Ingresa el nombre de la primera persona: ')
edad1 = int(input('Ingresa la edad de la primera persona: '))

persona2 = input('Ingresa el nombre de la segunda persona: ')
edad2 = int(input('Ingresa la edad de la segunda persona: '))

if edad1 > edad2:
    print(f'{persona1} es mayor que {persona2}') 
elif edad2 > edad1:
    print(f'{persona2} es mayor que {persona1}')
elif edad1 == edad2:
    print(f'{persona1} y {persona2} son de la misma edad')