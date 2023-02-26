lista = ["cidade", 'endereço', 'numero']
for i in lista:
    print(i)
    
tupla = ('cidade', 'endereço', 'numero')
for i in tupla:
    print(i)

conjunto = {'maçã', 'laranja', 'banan'}
for items in conjunto:
    print(items)
    
if 'laranja' in conjunto:
    print('yesss')
else:
    print('noo')