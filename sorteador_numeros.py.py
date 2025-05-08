# gerar 5  numeros aleatorios sorteador pelo computador
# devem estar em um intervalo de zero a 95
# add a soma dos numeros sorteados
soma = 0
import random
print('Numeros sorteados: ')
for numero in range(1, 6):
    numero_sorteado = random.randit(0, 95)
    print(numero_sorteado)
    soma += numero_sorteado
print(f'A soma dos numeros sorteados foi: {soma}')
