def agename(age, name):
    print(age, name)
agename(17,'pedro')

def primary():
    print('função primaria')
    def secundary():
        print('função secundaria')
    secundary()
primary()


valor = None

def numero(num):
    return num

valor = numero(10)
print(valor)

valor = numero(11)
print(valor)
