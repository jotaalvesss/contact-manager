pacientes = {}
medicos = {}

def adicionar_paciente():
    while True:
        
        cpf = input("CPF: ")
        if cpf.isalpha():
            print("O CPF deve ser representado em números.\nInsira os dados novamente:")
            continue

        if cpf in pacientes and pacientes[cpf]:
            print("Paciente já cadastrado.")
            return

        nome = input("Nome: ")

        idade = input("Idade: ")
        if idade.isalpha():
            print("A idade deve ser representada em números.\nInsira os dados novamente:")
            continue

        endereco = input("Endereço: ")

        telefone = input("Telefone: ")
        if telefone.isalpha():
            print("O telefone deve ser representado em números.\nInsira os dados novamente:")
            continue

        if not cpf or not nome or not idade or not endereco or not telefone:
            print("Por favor, preencha todos os campos.")
            continue

        pacientes[cpf] = {"Nome": nome, "Idade" : idade, "Endereco" : endereco, "Telefone" : telefone,}

        print("Novo paciente cadastrado com sucesso!")
        break
