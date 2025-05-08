# calcular a media de um turma de 3 alunos, que fizeram uma avaliacao 
# o usuario digita a nota dos alunos 

ct = 0
soma = 0
for numero in range(1, 3 + 1, 1):
    nota = float(input('Digite a nota de cada aluno'))
    soma += nota
    ct += 1
media = soma / ct
print(f'A media das notas foi: {media}')

#ALTERAÇOES
# mostrar a media com duas casas decimais

ct = 0
soma = 0 
for numero in range(1, 3 + 1, 1):
    nota = float(input('Digite a nota de cada aluno'))
    soma += nota
    ct += 1
media = soma / ct
print(f'A media das notas foi: {media :.2f}')
