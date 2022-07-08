import this
import forca
import operacoesBD

this.opcao2 = -1
this.opcao3 = -1
this.CPF = 0
this.campo = ""



def menu():
    print('\n/****************/')
    print( '/* FORCA PYTHON */')
    print('/****************/')
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. JOGAR FORCA PYTHON !\n' +
          '2. Alterar Dados Cadastrais\n' +
          '3. Excluir Conta\n'+
          '0. Sair')
    this.opcao2 = int(input())


def operacao():
    while (this.opcao2 != 0):

        menu()

        if this.opcao2 == 0:
            print('Obrigado!')

        elif this.opcao2 == 1:
            forca.forca()

        elif this.opcao2 == 2:
            alterarDadosCadastrais()

        elif this.opcao2 == 3:
            print("Informe seu CPF para excluir a conta")
            this.CPF = int(input())
            operacoesBD.excluir(this.CPF)
            exit()


        else:
            print('Opção escolhida não é válida!')


def menu2():
    print('\n/****************/')
    print( '/* FORCA PYTHON */')
    print('/****************/')
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Atualizar Nome\n' +
          '2. Atulizar Usuario\n' +
          '3. Atualizar Senha\n' +
          '4. Atualizar Email\n' +
          '5. Atualizar Data de Nascimento\n' +
          '0. Sair')
    this.opcao3 = int(input())


def alterarDadosCadastrais():
    while (this.opcao3 != 0):

        menu2()

        if this.opcao3 == 1:
            print("Informe o CPF para atualizar o dado desejado")
            this.CPF = int(input())
            print("Informe o novo nome: ")
            this.campo = input()
            if this.CPF or this.campo == '':
                print('Preencha todos os campos!')
            else:
                operacoesBD.atualizar(this.CPF, 'nome', this.campo )

        elif this.opcao3 == 2:
            print("Informe o CPF para atualizar o dado desejado")
            this.CPF = int(input())
            print("Informe o novo usuario: ")
            this.campo = input()
            if this.CPF or this.campo == '':
                print('Preencha todos os campos!')
            else:
                operacoesBD.atualizar(this.CPF, 'usuario', this.campo )

        elif this.opcao3 == 3:
            print("Informe o CPF para atualizar o dado desejado")
            this.CPF = int(input())
            print("Informe a nova senha: ")
            this.campo = input()
            if this.CPF or this.campo == '':
                print('Preencha todos os campos!')
            else:
                operacoesBD.atualizar(this.CPF, 'senha', this.campo )

        elif this.opcao3 == 4:
            print("Informe o CPF para atualizar o dado desejado")
            this.CPF = int(input())
            print("Informe o novo email: ")
            this.campo = input()
            if this.CPF or this.campo == '':
                print('Preencha todos os campos!')
            else:
                operacoesBD.atualizar(this.CPF,'email', this.campo)

        elif this.opcao3 == 5:
            print("Informe o CPF para atualizar o dado desejado")
            this.CPF = int(input())
            print("Informe a nova data de nascimento: ")
            this.campo = input()
            if this.CPF or this.campo == '':
                print('Preencha todos os campos!')
            else:
                operacoesBD.atualizar(this.CPF, 'dataDeNascimento', operacoesBD.tratarData(this.campo))
