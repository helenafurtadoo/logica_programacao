#gerar uma sequencia dos numeros inteiros de um em um
# usuario dornece os valores iniciais e finais da sequencia

# se i usuario escrever valor inicial menor que final, gerar sequencia crescente
# se contrario gerar sequencia decrescente

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
if valor_inicial < valor_final:
    for valor in range(valor_inicial, valor_final + 1, +1):
        print(valor)
else:
    for valor in range(valor_inicial, valor_final -1, -1):
        print(valor)