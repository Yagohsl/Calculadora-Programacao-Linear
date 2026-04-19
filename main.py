def isInteger(num):
    if num.is_integer():
        return str(int(num))
    return str(num)

numEq = int(input("Digite a quantidade de equações: "))
numVar = int(input("Digite a quantidade de variáveis: "))

represSistema = ''
sistema = []
equacao = []
for i in range(numEq):
    print(f"Equação {i+1}:")
    for j in range(numVar):
        valor = float(input(f"Digite o valor da variável {j+1}: "))
        equacao.append(valor)

        indice = i * numVar + j

        if valor >= 0:
            represSistema += " + " + isInteger(valor) + "x" + str(j+1)
        else:
            represSistema += " - " + isInteger(abs(valor)) + "x" + str(j+1)
    sistema.append(equacao)
    represSistema += '\n'



print(represSistema)
print(sistema)
