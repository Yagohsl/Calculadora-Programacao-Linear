import tkinter as tk

app = tk.Tk()
app.title("Calculadora")
app.geometry("1000x600") 


frame_entradas = tk.Frame(app)
frame_entradas.pack(expand=True) # expand=True ajuda a centralizar no meio da tela

# 2. Colocamos as entradas dentro do FRAME (não no app)
num1 = tk.Entry(frame_entradas, width=10)
num1.grid(row=1, column=0, padx=5) # Coluna 0 (esquerda)

num2 = tk.Entry(frame_entradas, width=10)
num2.grid(row=1, column=1, padx=5) # Coluna 1 (direita)

texto = tk.Label(frame_entradas, text="Qtd. de equações")
texto.grid(row=0, column=0, padx=5) 

texto = tk.Label(frame_entradas, text="Qtd. de variáveis")
texto.grid(row=0, column=1, padx=5) 

botao = tk.Button(frame_entradas, width = 10, text="->")
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