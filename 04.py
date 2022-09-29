# Exercício 04 (arigatô, Fare-san!)

media = 0
soma = 0
idades = [2,4,6]
idades.append(int(input("Digite sua idade para obter a média da lista: ")))
for elemento in idades:
    soma = soma + elemento

media = soma/len(idades)
print(media)