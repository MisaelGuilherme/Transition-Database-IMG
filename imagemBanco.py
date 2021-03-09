from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector

class aplication:

    def conexao_banco(self):
        
        self.banco  =  mysql.connector.connect(
            host='localhost',
            user='root',
            password='123')

        self.cursor = self.banco.cursor()

        self.cursor.execute('CREATE DATABASE IF NOT EXISTS image')
        self.cursor.execute('USE image')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS img(foto BLOB NOT NULL)''')
    
    def __init__(self):
        
        def exibir_arquivo(self):
            
            self.cursor.execute('SELECT * FROM img')
            valido = self.cursor.fetchall()

            imageCompilada = valido[0][0]

            caminho = r"C:\Users\Ryan\Desktop\imgbanco\Fotob1.png"
            
            with open(caminho, 'wb') as arquivoCompilado:
                arquivoCompilado.write(imageCompilada)
        
        def inserir_imagem():
            
            try:
                
                #Criando comando de inserção no banco de dado, e armazenando dados da imagem em binário na tupla
                tuplaComandoSQL = "INSERT INTO img (foto) VALUE (%s)"
                tuplaImagem = (imageBinary,)
                
                #Enviando dados para o Banco de dados
                self.cursor.execute(tuplaComandoSQL, tuplaImagem)
                self.banco.commit()
                
                messagebox.showinfo('Database', 'Imagem salva com sucesso!')
            
            except: messagebox.showerror('Alerta', 'Ops... Algo deu errado')
            
        def selecionar_imagem():
            
            global imagem
            global imageBinary
            
            try:
                
                #Abrindo o arquivo
                caminhoIMG = filedialog.askopenfilename(title='selecione um arquivo', filetypes=(("Imagem PNG", "*.png"), ("All files", "*.*")))
            
            except: pass

            #Com o caminho da imagem armazenada o arquivo será de modo leitura e em binário
            with open(caminhoIMG, 'rb') as arquivoBinary:
                imageBinary = arquivoBinary.read() #lendo o arquivo que está em binário e armazenando na variável
            
            #Invocando função para selecinar imagem através de seu caminho
            imagem = PhotoImage(file=caminhoIMG)
            
            #Configurando em label a imagem selecionada
            label = Label(root)
            label.pack() 
            label.configure(image=imagem)
            
            botConfirmar = Button(root, text='Confirmar', command=inserir_imagem)
            botConfirmar.place(relx=0.40, rely=0.70)
        
        root = Tk()
        
        root.geometry('300x300')

        menu = Menu(root)
        root.config(menu=menu)
        
        self.conexao_banco()
        
        menu.add_command(label='Abrir arquivo', command=selecionar_imagem)
        
        root.mainloop()

aplication()