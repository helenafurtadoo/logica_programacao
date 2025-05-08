# aula 02/04
# lert altura e genero de n pessoas. Saida com: maior altura do gp, menor altura do gp,
# quantidade de homens e mulheres

ct_masc = 0
ct_fem = 0
maior_altura = 0
menor_altura = 3
print("Digite zero para parar")
while True:
    altura = float(input("Digite a sua altura:"))
    if altura == 0:
        break
    genero = input("digite F para feminino, e M para masculino:")
    if genero == "M":
        ct_masc = ct_masc + 1
        if genero == "F":
            ct_fem = ct_fem + 1
            if altura > maior_altura:
                maior_altura = altura
                if altura < menor_altura:
                    menor_altura = altura
print("A maior altura foi:", maior_altura)
print()
print("A menor altura foi:", menor_altura)
print()
print("A quantidade de homens foi:", ct_masc)
print()
print("A quantidade de mulheres foi:", ct_fem)
print()
