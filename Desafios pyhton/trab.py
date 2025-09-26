class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # privado

    # GET: permite ler o valor
    def get_nome(self):
        return self.__nome

    # SET: permite alterar o valor
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

# Testando
p = Pessoa("Davi")
print(p.get_nome())  # lê o nome: Davi

p.set_nome("Carlos")  # altera o nome
print(p.get_nome())   # lê o novo nome: Carlos

print(p.__nome)       # ERRO! Não dá para acessar direto
