#escalonar e classificar conforme o numero de solucoes
#ex: solucao possivel determinada (SPD), solucao possivel indeterminada (SPI), solucao indeterminada (SI)
import tkinter as tk

app = tk.Tk()
app.title("Calculadora")
app.geometry("1000x600") 


frame_entradas = tk.Frame(app)
frame_entradas.pack(expand=True) #expand=True ajuda a centralizar no meio da tela

frame_equacoes = tk.Frame(app)


sistema = []
def acao_do_botao():
    frame_entradas.pack_forget()
    frame_equacoes.pack(expand=True)

    #cria entradas da equacao
    nEquacoes = int(qtdEquacoes.get())
    nVariaveis = int(qtdVariaveis.get())
    for i in range(nEquacoes):
        equacao = []
        for j in range(nVariaveis):
            
            #imprimir o '='
            if j == nVariaveis - 1:
                igual = tk.Label(frame_equacoes, text="=")
                igual.grid(row=i, column=j, padx=5) 
            
                entrada = tk.Entry(frame_equacoes, width=8)
                entrada.grid(row = i, column = j+1, padx=5, pady=5)

            else:
                entrada = tk.Entry(frame_equacoes, width=8)
                entrada.grid(row = i, column = j, padx=5, pady=5)
            equacao.append(entrada)
        sistema.append(equacao)

        #botao para escalonar
        btnContinuar = tk.Button(frame_equacoes, width=10, text="Escalonar", command = calcular_sistema)
        btnContinuar.grid(row=nEquacoes, column=0, columnspan=nVariaveis+1, pady=20)


def calcular_sistema():
    
    #guarda os valores em um vetor
    valores_numericos = []

    for i, linha in enumerate(sistema):
        valores_da_linha = []
        for j, entrada in enumerate(linha):
            valor = entrada.get()
            
            try:
                numero = float(valor) if valor != "" else 0.0
                valores_da_linha.append(numero)
            except ValueError:
                print(f"Erro na linha {i}, coluna {j}: '{valor}' não é um número")
        
        valores_numericos.append(valores_da_linha)
    
    print("Sua matriz de números:", valores_numericos)

#escalonando
def escalonar(sistema):
    for i, linha in enumerate(sistema):
        for j, entrada in enumerate(linha):
            pass


#pagina 1
#entradas das variaveis
qtdEquacoes = tk.Entry(frame_entradas, width=10)
qtdEquacoes.grid(row=1, column=0, padx=5) 

qtdVariaveis = tk.Entry(frame_entradas, width=10)
qtdVariaveis.grid(row=1, column=1, padx=5)

texto1 = tk.Label(frame_entradas, text="Qtd. de equações")
texto1.grid(row=0, column=0, padx=5) 

texto2 = tk.Label(frame_entradas, text="Qtd. de variáveis")
texto2.grid(row=0, column=1, padx=5) 

btnContinuar = tk.Button(frame_entradas, width = 10, text="Continuar", command = acao_do_botao)
btnContinuar.grid(row = 2, column = 0,pady=20,columnspan=2)



#pagina 2









app.mainloop()

'''
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
'''