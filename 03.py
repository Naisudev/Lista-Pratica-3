# Exercício 03

numero = int(input("Escolha um número: "))

if numero <= 10:
    for conta in range(1,11):
        print(conta*numero)

else:
    print("O número precisa estar entre 1 e 10")