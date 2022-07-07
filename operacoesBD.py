import mysql.connector
import conexaoBD
import menuPrincipal

db_connection = conexaoBD.conectar()
con = db_connection.cursor()


def inserirCadastro(CPF, nome, usuario, senha, email, dataDeNascimento):
    try:
        sql = "insert into cadastro(cpf,nome,usuario,senha,email,dataDeNascimento) values ('{}', '{}', '{}', '{}', '{}', '{}')".format(CPF, nome, usuario, senha, email, tratarData(dataDeNascimento))
        con.execute(sql)
        db_connection.commit()
        print("{} CADASTRO REALIZADO!".format(con.rowcount))

    except Exception as erro:
        return erro


def tratarData(texto):
    separado = texto.split('/')
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano, mes, dia)

def verificarLogin(usuarioo,senhaa):

    try:
        sql = 'select usuario, senha from cadastro'
        con.execute(sql)
        for (usuario, senha) in con:
            loginincorreto = 0
            if usuario == usuarioo and senha == senhaa:
                print('\nLogado com Sucesso')
                menuPrincipal.operacao()

            else:
                loginincorreto += 1
        if loginincorreto != 0:
           print("Usuario ou senha incorreto")


    except Exception as erro:
        print(erro)

def atualizar(CPF, campo, novoDado):
    try:
        sql = "update cadastro set {} = '{}' where CPF = '{}'".format(campo, novoDado, CPF)
        con.execute(sql)
        db_connection.commit()
        print('{} Atualizado'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluir(CPF):
    try:
        sql = "delete from cadastro where CPF = '{}'".format(CPF)
        con.execute(sql)
        db_connection.commit()
        print('{} CONTA EXLUIDA!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def consultarLoginSenha(cpf):
    try:
        sql = "select usuario,senha from cadastro where CPF ='{}'".format(cpf)
        con.execute(sql)

        for (usuario, senha) in con:
            print('Usuario: {}\nSenha: {}'.format( usuario, senha))
        print('\n')
    except Exception as erro:
        print(erro)