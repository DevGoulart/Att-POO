class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.05
    
    def MostrarInfo(self):
        print(self.nome, self.cpf, self.salario)

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, departamento):
        super().__init__(nome, cpf, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return super().calcular_bonus() + 500 + self.salario * 0.10
    
    def MostrarInfo(self):
        print(self.nome, self.cpf, self.salario)

class Diretor(Funcionario):
    def calcular_bonus(self):
        return super().calcular_bonus() + 1000 + self.salario * 0.15
    
def MostrarInfo(self):
        print(self.nome, self.cpf, self.salario)
    

# Exemplo de uso:
funcionario1 = Funcionario("João", "123.456.789-00", 5000)
Funcionario.MostrarInfo(funcionario1)
print("Bônus do Funcionário:", funcionario1.calcular_bonus())
print("-----------------------------")

gerente1 = Gerente("Maria", "987.654.321-00", 8000, "TI")
Gerente.MostrarInfo(gerente1)
print("Bônus do Gerente:", gerente1.calcular_bonus())
print("-----------------------------")

diretor1 = Diretor("José", "111.222.333-44", 10000)
Diretor.MostrarInfo(diretor1)
print("Bônus do Diretor:", diretor1.calcular_bonus())
print("-----------------------------")
