import tkinter as tk
from tkinter import messagebox

class AgendaSemanal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Semanal de Horários Detalhada")
        self.root.resizable(False, False)

        # Mapeamento dos dias e slots de horários de 1h
        self.dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
        self.horarios = [
            "08:00 - 09:00", 
            "09:00 - 10:00", 
            "10:00 - 11:00", 
            "12:00 - 13:00", 
            "13:00 - 14:00", 
            "14:00 - 15:00", 
            "15:00 - 16:00"
        ]
        
        # Matriz 5x7 inicializada com 0 (0 = Vazio, 1 = Ocupado)
        self.matriz = [[0 for _ in range(len(self.horarios))] for _ in range(len(self.dias))]
        self.botoes = []

        self._criar_interface()

    def _criar_interface(self):
        # Cabeçalho das Colunas (Dias da semana na primeira coluna e Horários nas demais)
        tk.Label(self.root, text="Dia / Horário", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, padx=8, pady=8)
        
        for c, horario in enumerate(self.horarios):
            tk.Label(self.root, text=horario, font=("Segoe UI", 8, "bold")).grid(row=0, column=c+1, padx=4, pady=8)

        # Construção visual da matriz (5 linhas x 7 colunas)
        for r, dia in enumerate(self.dias):
            tk.Label(self.root, text=dia, anchor="w", width=14, font=("Segoe UI", 9, "bold")).grid(row=r+1, column=0, padx=8, pady=4)
            
            linha_botoes = []
            for c in range(len(self.horarios)):
                btn = tk.Button(
                    self.root,
                    text="0 (Livre)",
                    bg="#E1E1E1",
                    fg="#000000",
                    width=10,
                    height=2,
                    font=("Segoe UI", 8),
                    relief="groove",
                    command=lambda row=r, col=c: self._alternar_estado(row, col)
                )
                btn.grid(row=r+1, column=c+1, padx=3, pady=3)
                linha_botoes.append(btn)
            self.botoes.append(linha_botoes)

        # Botão para Encerrar o Trabalho
        btn_encerrar = tk.Button(
            self.root,
            text="Encerrar Trabalho e Gerar Relatório",
            bg="#0078D7",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            command=self._encerrar_sistema
        )
        btn_encerrar.grid(row=len(self.dias)+1, column=0, columnspan=len(self.horarios)+1, pady=15, padx=10, sticky="ew")

    def _alternar_estado(self, linha, coluna):
        # Alterna o estado na matriz interna entre 0 e 1
        self.matriz[linha][coluna] = 1 if self.matriz[linha][coluna] == 0 else 0
        estado_atual = self.matriz[linha][coluna]

        # Atualiza o texto e a cor do botão correspondente
        btn = self.botoes[linha][coluna]
        if estado_atual == 1:
            btn.config(text="1 (Ocupado)", bg="#28A745", fg="white")
        else:
            btn.config(text="0 (Livre)", bg="#E1E1E1", fg="#000000")

    def _encerrar_sistema(self):
        # Soma todos os horários preenchidos (valor 1) da matriz
        total_preenchidos = sum(sum(linha) for linha in self.matriz)
        total_slots = len(self.dias) * len(self.horarios)
        
        messagebox.showinfo(
            "Relatório de Encerramento",
            f"Trabalho encerrado com sucesso!\n\n"
            f"Total de horários ocupados: {total_preenchidos} de {total_slots}\n"
            f"Taxa de ocupação: {(total_preenchidos / total_slots) * 100:.1f}%"
        )
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaSemanal(root)
    root.mainloop()