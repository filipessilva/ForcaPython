import operacoesBD
import this

this.opcao = -1
this.codigo = 0
this.campo = ""


def menu():
    print('\n/****************/')
    print( '/* FORCA PYTHON */')
    print('/****************/')
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Login\n' +
          '2. Cadastro\n' +
          '3. Esqueci meu usuario/senha\n' +
          '0. Sair')
    this.opcao = int(input())


def operacao():
    while (this.opcao != 0):

        menu()

        if this.opcao == 0:
            print('Obrigado!')

        elif this.opcao == 1:
            print('Informe o usuario:')
            usuarioo = input()
            print('Informe a senha:')
            senhaa = input()
            if usuarioo == '' or senhaa == '':
                print('Preencha todos os campos!')
            else:
                operacoesBD.verificarLogin(usuarioo, senhaa)

        elif this.opcao == 2:
            print('Informe seu CPF:')
            CPF = input()
            print('Informe seu nome:')
            nome = input()
            print('Informe seu usuario:')
            usuario = input()
            print('Informe sua senha:')
            senha = input()
            print('Informe seu email:')
            email = input()
            print('Informar sua data de nascimento: ')
            dtNasc = input()
            if usuario == '' or senha == '' or CPF == '' or nome == '' or email == '' or dtNasc =='' :
                print('Preencha todos os campos!')
            else:
                operacoesBD.inserirCadastro(CPF, nome, usuario, senha, email, dtNasc)

        elif this.opcao ==3:
            print('Informe o CPF de seu cadastro:')
            this.cpf = input();
            if this.cpf == '':
                print('Preencha o campo!')
            else:
                operacoesBD.consultarLoginSenha(this.cpf)

        else:
            print('Opção escolhida não é válida!')
