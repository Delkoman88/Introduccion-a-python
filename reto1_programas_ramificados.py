persona1 = input('Ingresa el nombre de la primera persona: ')
edad1 = int(input('Ingresa la edad de la primera persona: '))

persona2 = input('Ingresa el nombre de la segunda persona: ')
edad2 = int(input('Ingresa la edad de la segunda persona: '))

if persona1 > persona2:
    print(f'[persona1] + "es mayor que" + [persona2])') 
elif persona2 > persona1:
    print(f'[persona2] + "es mayor que" + [persona1])')
elif persona1 == persona2:
    print(f'[persona1] + "y" + [persona2] + "son de la misma edad")')