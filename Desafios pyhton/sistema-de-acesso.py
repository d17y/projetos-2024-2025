#---------SISTEMA DE ACESSO SIMPLES----------------
# Separado em dias da semana/cargo

cargo = input("Qual o seu cargo? ").strip().lower()
dia = input("Qual é o dia da semana? ").strip().lower()

if cargo == "funcionario" and (dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta" or dia == "sexta"):
    print("Acesso Liberado")

elif cargo == "gerente" or cargo == "diretor" or cargo == "presidente":
    print("Acesso Liberado")

else:
    print("Acesso Negado")
