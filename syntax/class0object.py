class minhaclasse:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def cumprimentar(self):
        print(f"hiii {self.nome}" )
    def __repr__(self):
        return str(self.__dict__)
   

primeiro = minhaclasse('pedro', 'henrique')
print(primeiro)
primeiro.cumprimentar()
