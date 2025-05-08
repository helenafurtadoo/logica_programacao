# aula 02/04
# encontrar o menor e o maior valor de um conjunto de valores inteiros. Saida == 0
ct = 0
soma = 0
menor_valor = 999999
maior_valor = -999999
print("Digite zero para parar")
while True:
    try:
       valor = int(input("Digite um valor:"))
       if valor == 0:
        break
       if valor < menor_valor:
         menor_valor = valor
       if valor> maior_valor:
         maior_valor = valor
    except ValueError:
      print("ERRO, tente novamente")
print("O menor valor encontrado foi:", menor_valor)
print("O maior valor encontrado foi:", maior_valor)
print("A soma dos valores foi")

