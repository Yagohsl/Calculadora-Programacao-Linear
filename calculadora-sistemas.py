import tkinter as tk
from tkinter import font as tkfont
import copy

# ── Paleta acadêmica ─────────────────────────────────────────────────────────
COR_FUNDO       = "#FAFAF8"
COR_PAINEL      = "#F0EFE9"
COR_BORDA       = "#BFBDB3"
COR_TEXTO       = "#1A1A1A"
COR_TEXTO_FRACO = "#555550"
COR_DESTAQUE    = "#2B4A8B"   # azul escuro estilo universitário
COR_SPD         = "#1A6B3A"
COR_SPI         = "#8B6A00"
COR_SI          = "#8B1A1A"
COR_PASSO       = "#E8E6DE"
FONTE_MONO      = ("Courier New", 10)
FONTE_TITULO    = ("Georgia", 13, "bold")
FONTE_NORMAL    = ("Georgia", 10)
FONTE_PEQUENA   = ("Georgia", 9)
FONTE_CLASSIF   = ("Georgia", 12, "bold")

app = tk.Tk()
app.title("Calculadora de Sistemas Lineares")
app.configure(bg=COR_FUNDO)
app.resizable(False, False)

sistema = []

# ── Frames principais ────────────────────────────────────────────────────────
frame_entradas   = tk.Frame(app, bg=COR_FUNDO)
frame_equacoes   = tk.Frame(app, bg=COR_FUNDO)
frame_resultados = tk.Frame(app, bg=COR_FUNDO)

frame_entradas.pack(expand=True)

# ── Utilitários de layout ────────────────────────────────────────────────────
def separador(parent, row, colspan):
    tk.Frame(parent, height=1, bg=COR_BORDA).grid(
        row=row, column=0, columnspan=colspan, sticky="ew", pady=6
    )

def titulo_secao(parent, texto, row, colspan):
    tk.Label(parent, text=texto, font=FONTE_TITULO,
             bg=COR_FUNDO, fg=COR_DESTAQUE).grid(
        row=row, column=0, columnspan=colspan, pady=(10, 4)
    )

def formatar_linha(linha):
    return "  ".join(f"{v:8.3f}" for v in linha)

# ── Funções matemáticas ───────────────────────────────────────────────────────
def calcular_posto(mat):
    posto = 0
    for linha in mat:
        if any(abs(v) > 1e-9 for v in linha[:-1]):
            posto += 1
    return posto

def classificar_sistema(mat_esc, n_var):
    for linha in mat_esc:
        if all(abs(v) < 1e-9 for v in linha[:-1]) and abs(linha[-1]) > 1e-9:
            return "Sistema Impossível (SI)", COR_SI
    posto = calcular_posto(mat_esc)
    if posto == n_var:
        return "Sistema Possível e Determinado (SPD)", COR_SPD
    return "Sistema Possível e Indeterminado (SPI)", COR_SPI

def escalonar_com_passos(mat_original):
    """Retorna (matriz_escalonada, lista_de_passos)."""
    mat   = copy.deepcopy(mat_original)
    linha = len(mat)
    col   = len(mat[0]) - 1
    passos = []

    for i in range(min(linha, col)):
        # pivoteamento parcial
        maior = i
        for j in range(i + 1, linha):
            if abs(mat[j][i]) > abs(mat[maior][i]):
                maior = j
        if maior != i:
            mat[i], mat[maior] = mat[maior], mat[i]
            passos.append((f"Troca L{i+1} ↔ L{maior+1}", copy.deepcopy(mat)))

        if abs(mat[i][i]) < 1e-9:
            continue

        for j in range(i + 1, linha):
            if abs(mat[j][i]) < 1e-9:
                continue
            fator = mat[j][i] / mat[i][i]
            sinal = "-" if fator >= 0 else "+"
            fator_abs = abs(fator)
            # formata o fator como fração simples se possível
            from fractions import Fraction
            frac = Fraction(fator).limit_denominator(100)
            frac_str = str(frac) if frac.denominator != 1 else str(frac.numerator)
            desc = f"L{j+1} ← L{j+1} {sinal} {frac_str}·L{i+1}"
            for k in range(i, len(mat[0])):
                mat[j][k] -= fator * mat[i][k]
            passos.append((desc, copy.deepcopy(mat)))

    return mat, passos

# ── Tela 1 — entradas iniciais ────────────────────────────────────────────────
tk.Label(frame_entradas, text="Calculadora de Sistemas Lineares",
         font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_DESTAQUE).grid(
    row=0, column=0, columnspan=2, pady=(20, 2)
)
tk.Label(frame_entradas,
         text="Escalonamento por Eliminação de Gauss  ·  Classificação SPD / SPI / SI",
         font=FONTE_PEQUENA, bg=COR_FUNDO, fg=COR_TEXTO_FRACO).grid(
    row=1, column=0, columnspan=2, pady=(0, 14)
)
separador(frame_entradas, 2, 2)

tk.Label(frame_entradas, text="Nº de equações", font=FONTE_NORMAL,
         bg=COR_FUNDO, fg=COR_TEXTO).grid(row=3, column=0, padx=20, pady=4, sticky="e")
tk.Label(frame_entradas, text="Nº de variáveis", font=FONTE_NORMAL,
         bg=COR_FUNDO, fg=COR_TEXTO).grid(row=4, column=0, padx=20, pady=4, sticky="e")

estilo_entry = dict(width=6, font=FONTE_NORMAL, relief="solid",
                    bd=1, bg="white", fg=COR_TEXTO)
qtdEquacoes = tk.Entry(frame_entradas, **estilo_entry)
qtdEquacoes.grid(row=3, column=1, padx=20, pady=4, sticky="w")
qtdVariaveis = tk.Entry(frame_entradas, **estilo_entry)
qtdVariaveis.grid(row=4, column=1, padx=20, pady=4, sticky="w")

separador(frame_entradas, 5, 2)

def botao_estilo(parent, texto, comando):
    return tk.Button(parent, text=texto, command=comando,
                     font=FONTE_NORMAL, bg=COR_DESTAQUE, fg="white",
                     activebackground="#1A3366", activeforeground="white",
                     relief="flat", bd=0, padx=16, pady=6, cursor="hand2")

botao_estilo(frame_entradas, "Continuar →", lambda: acao_do_botao()).grid(
    row=6, column=0, columnspan=2, pady=16
)

app.update_idletasks()
# ajusta a janela ao conteúdo da tela 1
def ajustar_janela():
    app.update_idletasks()
    w = app.winfo_reqwidth()  + 40
    h = app.winfo_reqheight() + 40
    app.geometry(f"{w}x{h}")

ajustar_janela()

# ── Tela 2 — entrada das equações ─────────────────────────────────────────────
def acao_do_botao():
    global sistema
    sistema = []
    for w in frame_equacoes.winfo_children():
        w.destroy()

    frame_entradas.pack_forget()
    frame_equacoes.pack(expand=True, padx=20, pady=10)

    nEq  = int(qtdEquacoes.get())
    nVar = int(qtdVariaveis.get())

    titulo_secao(frame_equacoes, "Insira os coeficientes do sistema", 0, 2*nVar+4)
    tk.Label(frame_equacoes,
             text="(deixe em branco para zero)",
             font=FONTE_PEQUENA, bg=COR_FUNDO, fg=COR_TEXTO_FRACO).grid(
        row=1, column=0, columnspan=2*nVar+4, pady=(0,8)
    )

    for i in range(nEq):
        equacao = []
        for j in range(nVar):
            entrada = tk.Entry(frame_equacoes, width=5, font=FONTE_MONO,
                               relief="solid", bd=1, bg="white",
                               fg=COR_TEXTO, justify="center")
            entrada.grid(row=i+2, column=2*j, padx=3, pady=4)

            sub = "₁₂₃₄₅₆₇₈₉"[j] if j < 9 else str(j+1)
            tk.Label(frame_equacoes, text=f"x{sub}", font=FONTE_NORMAL,
                     bg=COR_FUNDO, fg=COR_TEXTO_FRACO).grid(
                row=i+2, column=2*j+1, padx=2
            )
            if j < nVar - 1:
                tk.Label(frame_equacoes, text="+", font=FONTE_NORMAL,
                         bg=COR_FUNDO, fg=COR_TEXTO_FRACO).grid(
                    row=i+2, column=2*j+2, padx=0
                )
            equacao.append(entrada)

        tk.Label(frame_equacoes, text=" = ", font=FONTE_NORMAL,
                 bg=COR_FUNDO, fg=COR_TEXTO).grid(row=i+2, column=2*nVar, padx=4)
        b = tk.Entry(frame_equacoes, width=5, font=FONTE_MONO,
                     relief="solid", bd=1, bg="white",
                     fg=COR_TEXTO, justify="center")
        b.grid(row=i+2, column=2*nVar+1, padx=3, pady=4)
        equacao.append(b)
        sistema.append(equacao)

    separador(frame_equacoes, nEq+2, 2*nVar+4)
    botao_estilo(frame_equacoes, "Escalonar →",
                 calcular_sistema).grid(
        row=nEq+3, column=0, columnspan=2*nVar+4, pady=10
    )
    ajustar_janela()

# ── Tela 3 — resultados ───────────────────────────────────────────────────────
def calcular_sistema():
    valores = []
    for i, linha in enumerate(sistema):
        row = []
        for j, e in enumerate(linha):
            v = e.get()
            try:
                row.append(float(v) if v.strip() != "" else 0.0)
            except ValueError:
                print(f"Erro L{i} C{j}: '{v}'")
        valores.append(row)

    mat_original = copy.deepcopy(valores)
    mat_esc, passos = escalonar_com_passos(valores)
    mostrar_resultados(mat_original, mat_esc, passos)

def mostrar_resultados(mat_orig, mat_esc, passos):
    for w in frame_resultados.winfo_children():
        w.destroy()

    frame_equacoes.pack_forget()
    frame_resultados.pack(expand=True, fill="both", padx=20, pady=10)

    nLin = len(mat_orig)
    nVar = len(mat_orig[0]) - 1

    # ── Matriz original ──────────────────────────────────────────────────────
    titulo_secao(frame_resultados, "Matriz Aumentada — Original", 0, 1)

    canvas_orig = tk.Canvas(frame_resultados, bg=COR_FUNDO, highlightthickness=0)
    canvas_orig.grid(row=1, column=0, pady=4)
    desenhar_matriz(canvas_orig, mat_orig)

    separador(frame_resultados, 2, 1)

    # ── Passo a passo ────────────────────────────────────────────────────────
    titulo_secao(frame_resultados, "Passo a Passo — Eliminação de Gauss", 3, 1)

    frame_passos = tk.Frame(frame_resultados, bg=COR_FUNDO)
    frame_passos.grid(row=4, column=0, pady=4)

    if not passos:
        tk.Label(frame_passos, text="(nenhuma operação necessária)",
                 font=FONTE_PEQUENA, bg=COR_FUNDO,
                 fg=COR_TEXTO_FRACO).pack()
    else:
        for idx, (desc, mat) in enumerate(passos):
            bloco = tk.Frame(frame_passos, bg=COR_PASSO,
                             relief="flat", bd=0, padx=10, pady=6)
            bloco.pack(fill="x", pady=3)
            tk.Label(bloco, text=f"Passo {idx+1}:  {desc}",
                     font=("Courier New", 10, "bold"),
                     bg=COR_PASSO, fg=COR_DESTAQUE).pack(anchor="w")
            c = tk.Canvas(bloco, bg=COR_PASSO, highlightthickness=0)
            c.pack(anchor="w", pady=(4,0))
            desenhar_matriz(c, mat, bg=COR_PASSO)

    separador(frame_resultados, 5, 1)

    # ── Matriz escalonada ────────────────────────────────────────────────────
    titulo_secao(frame_resultados, "Matriz Escalonada — Resultado Final", 6, 1)
    canvas_esc = tk.Canvas(frame_resultados, bg=COR_FUNDO, highlightthickness=0)
    canvas_esc.grid(row=7, column=0, pady=4)
    desenhar_matriz(canvas_esc, mat_esc)

    separador(frame_resultados, 8, 1)

    # ── Classificação ────────────────────────────────────────────────────────
    classif, cor = classificar_sistema(mat_esc, nVar)
    tk.Label(frame_resultados, text=classif,
             font=FONTE_CLASSIF, bg=COR_FUNDO, fg=cor).grid(
        row=9, column=0, pady=8
    )
    explicacao = {
        COR_SPD: f"Posto = nº de variáveis = {nVar}  →  solução única.",
        COR_SPI: f"Posto ({calcular_posto(mat_esc)}) < nº de variáveis ({nVar})  →  infinitas soluções.",
        COR_SI:  "Linha 0 = k (k ≠ 0) detectada  →  sistema sem solução.",
    }
    tk.Label(frame_resultados, text=explicacao[cor],
             font=FONTE_PEQUENA, bg=COR_FUNDO, fg=COR_TEXTO_FRACO).grid(
        row=10, column=0, pady=(0, 6)
    )

    separador(frame_resultados, 11, 1)

    # ── Botão reiniciar ──────────────────────────────────────────────────────
    botao_estilo(frame_resultados, "⟳  Novo sistema", reiniciar).grid(
        row=12, column=0, pady=14
    )
    ajustar_janela()

def desenhar_matriz(canvas, mat, bg=COR_FUNDO):
    """Desenha a matriz com colchetes [ ] no canvas."""
    nLin = len(mat)
    nCol = len(mat[0])
    cell_w, cell_h = 72, 22
    pad_x, pad_y   = 14, 6
    W = pad_x * 2 + cell_w * nCol + 10
    H = pad_y * 2 + cell_h * nLin

    canvas.config(width=W, height=H)

    # colchetes
    bx, ex = 6, W - 6
    canvas.create_line(bx, pad_y,     bx+6, pad_y,     fill=COR_TEXTO, width=2)
    canvas.create_line(bx, pad_y,     bx,   H-pad_y,   fill=COR_TEXTO, width=2)
    canvas.create_line(bx, H-pad_y,   bx+6, H-pad_y,   fill=COR_TEXTO, width=2)
    canvas.create_line(ex, pad_y,     ex-6, pad_y,     fill=COR_TEXTO, width=2)
    canvas.create_line(ex, pad_y,     ex,   H-pad_y,   fill=COR_TEXTO, width=2)
    canvas.create_line(ex, H-pad_y,   ex-6, H-pad_y,   fill=COR_TEXTO, width=2)

    # linha separadora antes do vetor b
    sep_x = pad_x + cell_w * (nCol - 1) + cell_w // 2 - 4
    canvas.create_line(sep_x, pad_y+2, sep_x, H-pad_y-2,
                       fill=COR_BORDA, width=1, dash=(4,3))

    for i in range(nLin):
        for j in range(nCol):
            v = mat[i][j]
            txt = f"{v:.3f}".rstrip('0').rstrip('.')
            if txt == "-0": txt = "0"
            x = pad_x + j * cell_w + cell_w // 2
            y = pad_y + i * cell_h + cell_h // 2
            canvas.create_text(x, y, text=txt,
                               font=FONTE_MONO, fill=COR_TEXTO, anchor="center")

# ── Reiniciar ─────────────────────────────────────────────────────────────────
def reiniciar():
    global sistema
    sistema = []
    for w in frame_resultados.winfo_children():
        w.destroy()
    frame_resultados.pack_forget()
    qtdEquacoes.delete(0, tk.END)
    qtdVariaveis.delete(0, tk.END)
    frame_entradas.pack(expand=True)
    ajustar_janela()

app.mainloop()