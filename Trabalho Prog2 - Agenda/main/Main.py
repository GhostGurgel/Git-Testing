import tkinter as tk
from tkinter import messagebox

class AgendaSemanal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Semanal de Horários")
        self.root.resizable(False, False)

        # Mapeamento dos dias e períodos
        self.dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
        self.periodos = ["Manhã", "Tarde"]
        
        # Matriz 5x2 inicializada com 0 (0 = Vazio, 1 = Ocupado)
        self.matriz = [[0 for _ in range(2)] for _ in range(5)]
        self.botoes = []

        self._criar_interface()

    def _criar_interface(self):
        # Cabeçalho das Colunas
        tk.Label(self.root, text="Dia da Semana", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Manhã", font=("Segoe UI", 10, "bold")).grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Tarde", font=("Segoe UI", 10, "bold")).grid(row=0, column=2, padx=10, pady=10)

        # Construção visual da matriz (5 linhas x 2 colunas)
        for r, dia in enumerate(self.dias):
            tk.Label(self.root, text=dia, anchor="w", width=15, font=("Segoe UI", 9)).grid(row=r+1, column=0, padx=10, pady=5)
            
            linha_botoes = []
            for c in range(2):
                btn = tk.Button(
                    self.root,
                    text="0 (Vazio)",
                    bg="#E1E1E1",
                    fg="#000000",
                    width=14,
                    height=2,
                    relief="groove",
                    command=lambda row=r, col=c: self._alternar_estado(row, col)
                )
                btn.grid(row=r+1, column=c+1, padx=5, pady=5)
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)

        # Botão para Encerrar o Trabalho
        btn_encerrar = tk.Button(
            self.root,
            text="Encerrar Trabalho",
            bg="#0078D7",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            command=self._encerrar_sistema
        )
        btn_encerrar.grid(row=6, column=0, columnspan=3, pady=15, padx=10, sticky="ew")

    def _alternar_estado(self, linha, coluna):
        # Alterna o estado na matriz interna entre 0 e 1
        self.matriz[linha][coluna] = 1 if self.matriz[linha][coluna] == 0 else 0
        estado_atual = self.matriz[linha][coluna]

        # Atualiza o texto e a cor do botão correspondente
        btn = self.botoes[linha][coluna]
        if estado_atual == 1:
            btn.config(text="1 (Ocupado)", bg="#28A745", fg="white")
        else:
            btn.config(text="0 (Vazio)", bg="#E1E1E1", fg="#000000")

    def _encerrar_sistema(self):
        # Soma todos os horários preenchidos (valor 1) da matriz
        total_preenchidos = sum(sum(linha) for linha in self.matriz)
        
        messagebox.showinfo(
            "Relatório de Encerramento",
            f"Trabalho encerrado!\n\nTotal de horários preenchidos no período: {total_preenchidos}"
        )
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaSemanal(root)
    root.mainloop()
    