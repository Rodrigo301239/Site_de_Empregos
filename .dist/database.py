import customtkinter
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash

customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1400x800")
verificacao = 0
card_frame = customtkinter.CTkFrame(
    root,
    border_width=2,
    border_color="green",
    corner_radius=20
    )

card_title = customtkinter.CTkLabel(
        card_frame,
        text="📝 Escolha uma Opção",
        font=("Arial", 16, "bold"),
        text_color="#4ECB71"  # Cor do texto
    )
card_title.pack(pady=12)
card_frame.pack(pady=60, padx=750, fill="both", expand=True)

def conectar_banco():
    conexao = sqlite3.connect("Banco.db")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists empregados
                   (email text primary key, nome text, senha text)''' )
    
    cursor.execute('''create table if not exists empregadores
                   (email text primary key, nome text, senha text)''' )

    cursor.execute('''create table if not exists Curriculo (id integer primary key, nome text, contato integer, endereco text, horarios text, escolaridade text, email_usuario text,
             FOREIGN KEY(email_usuario) REFERENCES empregados(email))''')
    
    cursor.execute('''create table if not exists Vaga (id integer primary key, nome text, requisitos text, disponibilidade integer, salario double, email_usuario text,
             FOREIGN KEY(email_usuario) REFERENCES empregadores(email))''')
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Candidatos (id INTEGER PRIMARY KEY, candidato_nome TEXT, candidato_email TEXT,
        FOREIGN KEY (candidato_nome) REFERENCES empregados(nome),
        FOREIGN KEY (candidato_email) REFERENCES empregados(email))""")
    
    
    
    conexao.commit()
    
    
def empresas_aleatorias():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("""insert into empregadores(email,nome,senha) VALUES (?,?,?)""",("empresa1@gmail.com","Simas Turbo",123))
    cursor.execute("""INSERT INTO empregadores(email, nome, senha) VALUES (?, ?, ?)""", 
               ("techjobs@empresa.com", "Tech Jobs", 123))
    cursor.execute("""INSERT INTO empregadores(email, nome, senha) VALUES (?, ?, ?)""", 
                ("vagasrh@empresa.com", "Vagas RH", 123))
    cursor.execute("""INSERT INTO empregadores(email, nome, senha) VALUES (?, ?, ?)""", 
                ("construtora@concreto.com", "Construtora Concreto", 123))
    cursor.execute("""INSERT INTO empregadores(email, nome, senha) VALUES (?, ?, ?)""", 
                ("hospitalvida@saude.com", "Hospital Vida", 123))
    
    
    
    cursor.execute("""insert into vaga(nome,requisitos,disponibilidade,salario,email_usuario) VALUES (?,?,?,?,?)""",("Assistente de mão","Cursando ensino médio","qualquer",1200,"empresa1@gmail.com"))
    cursor.execute("""INSERT INTO vaga(nome, requisitos, disponibilidade, salario,email_usuario) VALUES (?, ?, ?, ?,?)""", 
               ("Desenvolvedor Júnior", "Tecnico em TI", "Integral", 3000,"techjobs@empresa.com"))
    cursor.execute("""INSERT INTO vaga(nome, requisitos, disponibilidade, salario,email_usuario) VALUES (?, ?, ?, ?,?)""", 
                ("Auxiliar Administrativo", "Ensino médio completo", "Manhã", 1800,"vagasrh@empresa.com"))
    cursor.execute("""INSERT INTO vaga(nome, requisitos, disponibilidade, salario,email_usuario) VALUES (?, ?, ?, ?,?)""", 
                ("Pedreiro", "Ensino médio completo", "Integral", 2500,"construtora@concreto.com"))
    cursor.execute("""INSERT INTO vaga(nome, requisitos, disponibilidade, salario,email_usuario) VALUES (?, ?, ?, ?,?)""", 
                ("Enfermeiro", "Enfermagem", "Integral", 4000,"hospitalvida@saude.com"))

    
    conexao.commit()
           

if __name__ == "__main__":
    criar_tabelas()
    empresas_aleatorias()
    
    
    
    
    
    
    

def criar_conta(verificacao,nome,email,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    senha_criptografada = generate_password_hash(senha)
    
    if verificacao == 1:
        cursor.execute("""insert into empregados(email,nome,senha) VALUES (?,?,?)""",(email,nome,senha_criptografada))  
        
    elif verificacao == 2:
        cursor.execute("""insert into empregadores(email,nome,senha) VALUES (?,?,?)""",(email,nome,senha_criptografada))  
        
        
    conexao.commit()
    conexao.close()

def login(verificacao,email,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    
    
    try:
        if verificacao == 1:
            cursor.execute('''SELECT count(email) from empregados WHERE email=?''',(email,))
            conexao.commit()
            quantidade_de_emails = cursor.fetchone()
            if(quantidade_de_emails[0] < 0):
                print("LOG: email não encontrado.")
                return False
            cursor.execute("""SELECT * from empregados where email = ?""",(email,))
            
            conexao.commit()
               
            senha_criptografada = cursor.fetchone()
            resultado_verificacao = check_password_hash(senha_criptografada[0], senha)
            return resultado_verificacao
            
        elif verificacao == 2:
            cursor.execute('''SELECT count(email) from empregados WHERE email=?''',(email,))
            conexao.commit()
            quantidade_de_emails = cursor.fetchone()
            if(quantidade_de_emails[0] < 0):
                print("LOG: email não encontrado.")
                return False
            cursor.execute("""SELECT * from empregadores where email = ?""",(email,))
            conexao.commit()
            senha_criptografada = cursor.fetchone()
            resultado_verificacao = check_password_hash(senha_criptografada[0], senha)
            print("OOOOOOOOOOK")
            return resultado_verificacao
            
    except:
        return False
    
    

    