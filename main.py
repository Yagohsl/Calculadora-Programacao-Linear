#escalonar e classificar conforme o numero de solucoes
#ex: solucao possivel determinada (SPD), solucao possivel indeterminada (SPI), solucao indeterminada (SI)
import tkinter as tk

app = tk.Tk()
app.title("Calculadora")
app.geometry("1000x600") 


frame_entradas = tk.Frame(app)
frame_entradas.pack(expand=True) #expand=True ajuda a centralizar no meio da tela

frame_equacoes = tk.Frame(app)
frame_resultados = tk.Frame(app)


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
            
           
            entrada = tk.Entry(frame_equacoes, width=5)
            entrada.grid(row=i, column=2*j, padx=2, pady=5)

            
            simbolo = tk.Label(frame_equacoes, text=f"x{j+1}")
            simbolo.grid(row=i, column=2*j + 1, padx=2, pady=5)

            equacao.append(entrada)
        #coloca o '='
        igual = tk.Label(frame_equacoes, text="=")
        igual.grid(row=i, column=2*nVariaveis, padx=5)

        #resultado (b)
        entrada_resultado = tk.Entry(frame_equacoes, width=5)
        entrada_resultado.grid(row=i, column=2*nVariaveis + 1, padx=5, pady=5)
        equacao.append(entrada_resultado)

        sistema.append(equacao)

        #botao para escalonar
        btn_continuar = tk.Button(frame_equacoes, width=10, text="Escalonar", command = calcular_sistema)
        btn_continuar.grid(row=nEquacoes, column=0, columnspan=2*nVariaveis+2, pady=20)

      


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
    escalonar(valores_numericos)


def escalonar(sistema):
    linha = len(sistema)
    coluna = len(sistema[0]) -1
    #achando o pivo
    for i in range(min(linha,coluna)):
        maior_linha = i

        for j in range(i+1, linha):
            if( abs(sistema[j][i]) > abs(sistema[maior_linha][i])):
                maior_linha = j

        #troca linha
        sistema[i], sistema[maior_linha] = sistema[maior_linha], sistema[i]
        
        if sistema[i][i] == 0:
            continue

        for j in range(i +1, linha):
            fator = sistema[j][i] / sistema[i][i]
            for k in range(i, len(sistema[0])):
                sistema[j][k] -= fator * sistema[i][k]
    print(f'escalonada: {sistema}')

    #mostra resultados
    frame_equacoes.pack_forget()
    frame_resultados.pack(expand=True)

    for n in range(linha):
            
        resultado = tk.Label(frame_resultados, text= sistema[n])
        resultado.grid(row=n, column=0, padx=5) 


    
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




app.mainloop()

