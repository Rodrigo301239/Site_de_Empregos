
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash

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
    
    conexao.commit()
    
def texto():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    palavras = "ROBOCOPGAY!"
    #cursor.execute(''' INSERT INTO Banco (teste) VALUES (?)''', (palavras,))
    
    #conexao.commit()
    return palavras

def criar_conta(etapa,nome,email,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    if etapa == 1:
    
        cursor.execute("""insert into empregados(email) VALUES (?)""",(email,))
        print("deu boa")
    
    conexao.commit()

if __name__ == "__main__":
    criar_tabelas()
