from tkinter import *
from tkinter import ttk
#basedados
import sqlite3 
#pdf
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image 
#browser
import webbrowser
from PIL import ImageTk , Image

janela = Tk()

#backend

class Relatorios():
    def printCliente(self):
        webbrowser.open("relatorios/clientes.pdf")

    def gerar_relatorioCliente(self):
        self.clt = canvas.Canvas("clientes.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.moradaRel = self.morada_entry.get()

        #titulo
        self.clt.setFont("Helvetica-Bold", 24)
        self.clt.drawString(150, 750, "RELATORIO DE CLIENTES")

        #corpo
        self.clt.setFont("Helvetica-Bold", 12)
        self.clt.drawString(50, 700, "Codigo: " )
        self.clt.drawString(50, 680, "Nome: " )
        self.clt.drawString(50, 660, "Telefone: " )
        self.clt.drawString(50, 640, "Morada: " )

        self.clt.setFont("Helvetica", 12)
        self.clt.drawString(150, 700, self.codigoRel )
        self.clt.drawString(150, 680, self.nomeRel )
        self.clt.drawString(150, 660, self.telefoneRel )
        self.clt.drawString(150, 640, self.moradaRel )

        self.clt.showPage()
        self.clt.save()
        self.printCliente()

class funcs():
    def limpar_dados_ecra(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.morada_entry.delete(0, END)
    def ligar_bd(self):
        self.conn = sqlite3.connect("gestao_clt.db")
        self.cursor = self.conn.cursor()
    
    def desliga_bd(self):
        self.conn.close()
        
    def criarTabelas(self):
        self.ligar_bd(); print("ligando ao banco de dados")
        #criar a tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY,
            nome_clt CHAR(50) NOT NULL,
            telefone_clt INTEGER(12) NOT NULL,
            morada_clt CHAR(50) NOT NULL
        );
        """)
        self.conn.commit(); print("tabela criada")
        self.desliga_bd(); print("desligando ao banco de dados")

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.morada = self.morada_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.ligar_bd()
        
        self.cursor.execute("""
        INSERT INTO clientes (nome_clt, telefone_clt, morada_clt) VALUES (?, ?, ?)
        """, (self.nome, self.telefone, self.morada))
        self.conn.commit()
        self.desliga_bd()
        self.select_lista()
        self.limpar_dados_ecra()
        
    def select_lista(self):
        self.listaclt.delete(*self.listaclt.get_children())
        self.ligar_bd()
        lista =self.cursor.execute(""" SELECT cod, nome_clt, telefone_clt, morada_clt FROM clientes ORDER BY cod ASC; """)
        for i in lista:
            self.listaclt.insert("", END, values=i)
        self.desliga_bd()

    def OnDoubleClick(self, event):
        self.limpar_dados_ecra()
        self.listaclt.selection()
        
        for n in self.listaclt.selection():
            col1, col2, col3, col4 = self.listaclt.item(n, "values")
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.morada_entry.insert(END, col4)
    
    def apagar_cliente(self):
        self.variaveis()
        self.ligar_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desliga_bd()
        self.limpar_dados_ecra()
        self.select_lista()

    def alterar_cliente(self):
        self.variaveis()
        self.ligar_bd()
        self.cursor.execute("""UPDATE clientes SET nome_clt = ?, telefone_clt = ?, morada_clt = ? WHERE cod = ? """, (self.nome, self.telefone, self.morada, self.codigo))
        self.conn.commit()
        self.desliga_bd()
        self.limpar_dados_ecra()
        self.select_lista()

    def procurar_cliente(self):
        self.ligar_bd()
        self.listaclt.delete(*self.listaclt.get_children())

        self.nome_entry.insert(END, "%")
        nome = self.nome_entry.get()
        self.cursor.execute(""" SELECT cod, nome_clt, telefone_clt, morada_clt FROM clientes WHERE nome_clt LIKE "%"  ORDER BY nome_clt ASC """ % nome)
        for i in self.cursor.fetchall():
            self.listaclt.insert("", END, values=i)
        self.desliga_bd()
        self.limpar_dados_ecra()
        
class application(funcs, Relatorios):
    def __init__(self):
        self.tela()
        self.frames_da_tela()
        self.windgets_frame_cima() 
        self.lista_frame_baixo()
        self.criarTabelas()
        self.select_lista()
        self.Menus()
        janela.mainloop()
        
#frontend
    def tela(self):
        janela.title("Registo de Clientes")
        janela.configure(background="#1e3743")
        janela.geometry("780x500")
        janela.resizable(True, True)
        janela.maxsize(width=980, height=700)
        janela.minsize(width=680, height=420)
        
    def frames_da_tela(self):
        self.frame_cima = Frame(janela, bd=4, bg="#F8F8FF", highlightbackground="#87CEFA", highlightthickness=3)
        self.frame_cima.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.frame_baixo = Frame(janela, bd=4, bg="#F8F8FF", highlightbackground="#87CEFA", highlightthickness=3)
        self.frame_baixo.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)
        
    def windgets_frame_cima(self):
        # canvas
        self.canvas_bt = Canvas(self.frame_cima, bd=0, bg="black", heighlightbackground="green", highlightthickness=3)
        self.canvas_bt.place(relx=0.15, rely=0.08, relwidth=0.5, relheight=0.19)

        #botao limpar    
        self.bt_limpar = Button(self.frame_cima, text="Limpar", bd=3, width=10, height=2, bg="#87CEFA", fg="black", font="Arial 10 bold", command=self.limpar_dados_ecra)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        #botao procurar    
        self.bt_procurar = Button(self.frame_cima, text="Procurar", bd=3, width=10, height=2, bg="#87CEFA", fg="black", font="Arial 10 bold",command=self.procurar_cliente)
        self.bt_procurar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.15)    
        
        #botao novo    
        self.bt_novo = Button(self.frame_cima, text="Novo", bd=3, width=10, height=2, bg="#87CEFA", fg="black", font="Arial 10 bold", command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        #botao alterar    
        self.bt_alterar = Button(self.frame_cima, text="Alterar", bd=3, width=10, height=2, bg="#87CEFA", fg="black", font="Arial 10 bold", command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.72, rely=0.1, relwidth=0.1, relheight=0.15)

        #botao apagar    
        self.bt_apagar = Button(self.frame_cima, text="Apagar", bd=3, width=10, height=2, bg="#87CEFA", fg="black", font="Arial 10 bold", command=self.apagar_cliente)
        self.bt_apagar.place(relx=0.84, rely=0.1, relwidth=0.1, relheight=0.15)
        
        #criar label e entrada do codigo
        self.lb_codigo = Label(self.frame_cima, text="Código",bg="#F8F8FF", fg="#1E90FF", font="times 12 bold")
        self.lb_codigo.place(relx=0.05, rely=0.01, relwidth=0.1, relheight=0.08)
        
        self.codigo_entry = Entry(self.frame_cima,  bd=2)
        self.codigo_entry.place(relx=0.05, rely=0.12, relwidth=0.12, relheight=0.10)

        #criar label e entrada do nome
        self.lb_nome = Label(self.frame_cima, text="Nome", bg="#F8F8FF", fg="#1E90FF", font="times 12 bold")
        self.lb_nome.place(relx=0.05, rely=0.3, relwidth=0.1, relheight=0.08)
        
        self.nome_entry = Entry(self.frame_cima, bd=2)
        self.nome_entry.place(relx=0.05, rely=0.42, relwidth=0.42, relheight=0.10)
        
        #criar label e entrada do telefone
        self.lb_telefone = Label(self.frame_cima, text="Telemovel", bg="#F8F8FF", fg="#1E90FF", font="times 12 bold")
        self.lb_telefone.place(relx=0.72, rely=0.3, relwidth=0.1, relheight=0.08)
        
        self.telefone_entry = Entry(self.frame_cima , bd=2)
        self.telefone_entry.place(relx=0.72, rely=0.42, relwidth=0.12, relheight=0.10)
        
        #criar label e entrada da morada
        self.lb_morada = Label(self.frame_cima, text="Morada", bg="#F8F8FF", fg="#1E90FF", font="times 12 bold")
        self.lb_morada.place(relx=0.05, rely=0.6, relwidth=0.1, relheight=0.08)
        
        self.morada_entry = Entry(self.frame_cima , bd=2)
        self.morada_entry.place(relx=0.05, rely=0.72, relwidth=0.52, relheight=0.10)
        
    def lista_frame_baixo(self):
        self.listaclt = ttk.Treeview(self.frame_baixo, height=3, columns=("col1", "col2","col3", "col4"))
        self.listaclt.heading("#0", text="")
        self.listaclt.heading("#1", text="Código")
        self.listaclt.heading("#2", text="Nome")
        self.listaclt.heading("#3", text="Telefone")
        self.listaclt.heading("#4", text="Morada")
        
        self.listaclt.column("#0", width=1)
        self.listaclt.column("#1", width=50)
        self.listaclt.column("#2", width=200)
        self.listaclt.column("#3", width=125)
        self.listaclt.column("#4", width=200)
        
        self.listaclt.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.95)
        
#criar scrool
        self.scroollista = Scrollbar(self.frame_baixo, orient="vertical")
        self.listaclt.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.97, rely=0.01, relwidth=0.02, relheight=0.949)
        self.listaclt.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        def Quit(): self.janela.destroy()
        
        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatorios", menu=filemenu2)
        
        filemenu.add_command(label="Novo")
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Salvar")
        filemenu.add_command(label="Apagar Cliente", command=self.apagar_cliente)
        filemenu.add_command(label="Sair", command=Quit)


        filemenu2.add_command(label="Ficha do cliente", command=self.gerar_relatorioCliente)

        
        janela.config(menu=menubar)

application()

