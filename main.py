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

def excluir_paciente():

    while True:


        cpf = input("Digite o CPF do paciente a ser removido: ")

        if cpf in pacientes and pacientes[cpf]:
            pacientes[cpf] = False
            print("Paciente excluído com sucesso!")
            break

        else:

            print("O paciente não foi encontrado.")
            break

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    
    for cpf, dados in pacientes.items():
        print(f"CPF: {cpf}")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
        print("-----")

while True:
    print("\n1. Adicionar paciente")
    print("2. Excluir paciente")
    print("3. Listar pacientes")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_paciente()
    elif opcao == '2':
        excluir_paciente()
    elif opcao == '3':
        listar_pacientes()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
