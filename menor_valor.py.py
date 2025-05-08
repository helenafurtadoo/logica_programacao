# aula 02/04
# encontrar o menor valor de um conjunto de valores inteiros digitados pelo usuario. Na saida usar (0)

menor_valor = 999999
print("Para parar, digite zero (0)")
while True:
    valor = int(input("Digite um valor:"))
    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor
print("O menor valor é:", menor_valor)
