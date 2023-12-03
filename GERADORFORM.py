import random as rd

def yureiform():
    print('Bem vindo(a) ao YureiForms! \n')

    def name_input():
        nome = (input('\nDigite seu nome: '))

        while not nome:
            print('Por favor, digite seu nome: ')
            nome = (input('Digite seu nome: '))
        
        print('Olá, {}'.format(nome.capitalize()))
        print('Prosseguindo!\n')
        return nome

    nome = name_input()

    def age_input():
        idade = (input(f'{nome.capitalize()}, digite sua idade: '))

        while not idade:
            print('Por favor, digite sua idade!')
            idade = (input(f'{nome.capitalize()}, digite sua idade: '))
        
        print('Prosseguindo!\n')
        return idade

    idade = age_input()

    def email_dom():
        email = input(f'{nome.capitalize()}, digite seu email: ')
        if '@gmail.com' in email:
            print('Prosseguindo!\n')
            pass
        elif '@outlook.com' in email:
            print('Prosseguindo!\n')
            pass
        elif '@hotmail.com' in email:
            print('Prosseguindo!\n')
            pass
        else:
            while not email:
                print('Por favor, digite seu email!')
                email = input(f'{nome.capitalize()}, digite seu email: \n')

        return email

    email = email_dom()

    def number():
        num_cont = (input(f'{nome.capitalize()}, digite seu número para contato (com DDD): '))
        print('Finalizando seu formulário\n')
        return num_cont

    num_cont = number()

    print(f'\n{nome.capitalize()}, obrigado por preencher nosso formulário! YureiForms Agradece.\n')

    #criação do número de registro do formulário
    reg_numbers = '0123456789'
    lenght = 4
    reg = ''.join(rd.sample(reg_numbers, lenght))
    print(f'O seu número de registro de formulário é: {reg}')

    #conversão do arquivo .txt para .pdf
    form = open("form.txt", "w")
    form.write(f"Bem vindo ao YureiForms!\n\n Nome: {nome.capitalize()}\n\n Idade: {idade} \n\n Email: {email} \n\n Contato: {num_cont}")
    form.close()

yureiform()