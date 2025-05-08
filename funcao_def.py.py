#funcao que calcula o dobro. 
#ela recebe um valor, calcula o dobro e retorna o valor calculado 

def dobro(valor):
    dobro = valor * 2
    return dobro

#if abaixo, para iniciar  execucao do programa iniciaç
if __name__  == "__main__":
    valor = int(input("Digite um valor"))
    valor_dobrado = dobro(valor) #valor retornado, armazenado na varialvel "valor_dobrado"
    print("O valor retornardo foi: ", valor_dobrado)


#acrescentar funcao q calcula o triplo
#recebe um valor, calcula o triplo e retorna o valor calculado

def triplo(valor):
    triplo = valor * 3
    return triplo
if __name__ == "__main__":
    valor = int(input("Digite um valor para ser calculado o seu triplo"))
    valor_triplo = triplo(valor) 
    print("O triplo do valor digitado é: ", valor_triplo)

    valor2 = int (input("número: "))
    print(dobro(valor2))

#somar dois valores. 

def somar(valor1, valor2):
    soma = valor1 + valor2
    return soma
if __name__ == "_main__":
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor_soma = soma(valor1, valor2)
    print("A soma dos valores foi: ", soma)
