
import sqlite3

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

    return palavras

def criar_conta(verificacao,nome,email,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    if verificacao == 1:
        cursor.execute("""insert into empregados(email,nome,senha) VALUES (?,?,?)"""(email,nome,senha))  
        print("deu boa")
    elif verificacao == 2:
        cursor.execute("""insert into empregadores(email,nome,senha) VALUES (?,?,?)"""(email,nome,senha))  
        print("deu boa")
        
    conexao.commit()
    conexao.close()

def logar(verificacao,email,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    if verificacao == 1:
    
        cursor.execute("""SELECT * from empregados where email = ?""",(email))
        usuario = cursor.fetchall()
    
    elif verificacao == 2:
        
        cursor.execute("""SELECT * from empregadores where email = ?""",(email))
        usuario = cursor.fetchall()
    
    
    if usuario:
        if usuario[2] == senha:
            return True
        else:
            return "Senha ou email incorretos"
    return "Senha ou email incorretos"
    
    
    

if __name__ == "__main__":
    criar_tabelas()
