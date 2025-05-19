#1. Ler um numero imposto pelo usario e denominar em Positivo, Negativo ou Nulo, usando funcao
def positivo_nulo_negativo(numero):
    if numero > 0:
        print('Valor posivito')
    elif numero == 0:
        print('Valor nulo')
    else: 
        print('Valor negativo')

#programa principal
def main():
    numero = float(input('Digite um numero real:'))
    positivo_nulo_negativo(numero)

#chamada da funcao
main()

#2. Calcular o numero absoluto de um numero imposto pelo usario, usando funcao 
def numeroAbsoluto(numero):
    if numero < 0:
        return -numero
        
    else:
        return numero

def main():
    numero = float(input('Digte um numero'))
    resultado = numeroAbsoluto(numero)
    print(f'O valor absoluto é: {resultado}')
   
#chamada da funcao:
main()

#3. simular uam calculadora com as 4 operacoes, usando a funcao def

# primeiro definir todas as funcoes:
def soma(valor1, valor2):
    resultado = valor1 + valor2
   print(f'Resultado da soma: {resultado}')

def subtracao(valor1, valor2):
    resultado = valor1 - valor2
    print(f'O resultado da subtrcao foi: {resultado}'):

def divisao(valor1, valor2):
    if valor2 != 0:
    resultado = valor1 / valor2
    print(f'O resultado da divisao foi: {resultado}')

def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    print(f'O resultado da multiplicacao foi: {resultado}')


# funcao principal:
def main():
valor1 = int(input('Digite o valor 1'))
valor2 = int(input('Digite o valor 2'))
operacao = input('Digite a operacao que deseja efetuar: + , - , / , * ')

if operacao == '+':
    soma(valor1 , valor2)
    elif operacao == '-':
        subtracao(valor1, valor2)
        elif operacao == '/':
            divisao(valor1, valor2)
            elif operacao == '*':
                multiplicacao(valor1, valor2)
                else:
                    print('Operação inválida')
# executar o programa:
main()

#4. Calcular o fatorial de um numero posto pelo usuario usando funcao
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i 

def main():
    numero = int(input('Digite um numero inteiro para calcular o fatorial: '))
    if numero < 0:
        print('Fatorial não existe para numeros negativos')
    else:
    print(f'O fatorial do numero {numero} é: {fatorial}')