class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def cumprimentar(self):
        print(f"hiii {self.nome}" )
    def __repr__(self):
        return str(self.__dict__)
   

primeiro = Pessoa('pedro', 'henrique')
print(primeiro)
primeiro.cumprimentar()

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, curso):
        super().__init__(nome, sobrenome)
        self.curso = curso
    def __repr__333(self):
        return super().__repr__()
    
segundo = Aluno('pedro','henrique', 'S.I')
print(segundo)
