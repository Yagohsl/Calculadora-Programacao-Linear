import tkinter as tk

app = tk.Tk()
app.title("Calculadora")
app.geometry("1000x600") 


frame_entradas = tk.Frame(app)
frame_entradas.pack(expand=True) #expand=True ajuda a centralizar no meio da tela

frame_equacoes = tk.Frame(app)


def acao_do_botao():
    frame_entradas.pack_forget()
    frame_equacoes.pack(expand=True)

    #cria entradas da equacao
    sistema = []
    nEquacoes = int(qtdEquacoes.get())
    nVariaveis = int(qtdVariaveis.get())
    for i in range(nEquacoes):
        equacao = []
        for j in range(nVariaveis):
            entrada = tk.Entry(frame_equacoes, width=8)
            entrada.grid(row = i, column = j, padx=5, pady=5)
            equacao.append(entrada)
        sistema.append(equacao)

#entradas das variaveis
qtdEquacoes = tk.Entry(frame_entradas, width=10)
qtdEquacoes.grid(row=1, column=0, padx=5) 

qtdVariaveis = tk.Entry(frame_entradas, width=10)
qtdVariaveis.grid(row=1, column=1, padx=5)

texto1 = tk.Label(frame_entradas, text="Qtd. de equações")
texto1.grid(row=0, column=0, padx=5) 

texto2 = tk.Label(frame_entradas, text="Qtd. de variáveis")
texto2.grid(row=0, column=1, padx=5) 

botao = tk.Button(frame_entradas, width = 10, text="->", command = acao_do_botao)
botao.grid(row = 2, column = 0,pady=20,columnspan=2)













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