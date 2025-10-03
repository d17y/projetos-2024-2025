contador = 0

print("Esse é o contador atual:", contador)
print("Aperte a letra Z")

while contador < 10:
    checar_tecla = input(": ") 
    if checar_tecla.lower() == "z":  
        contador += 1
        print(f"Você acertou! Contador = {contador}")
    else:
        print("Você apertou a tecla errada!")

print("Parabéns, você chegou em 10 cliques na letra Z!")
