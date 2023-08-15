class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0
        self.saques_restantes = 3
        self.depositos_totais = 0
        self.saques_totais = 0

class Usuario:
    def __init__(self, nome, senha, logradouro, bairro, cidade, estado, celular, cpf):
        self.nome = nome
        self.senha = senha
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.celular = celular
        self.cpf = cpf
        self.contas_correntes = []

def cadastrar_usuario():
    print("================= CADASTRO =================")
    nome = input("Nome: ")
    senha = input("Senha: ")
    logradouro = input("Logradouro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    celular = input("Número de Celular: ")
    cpf = input("CPF: ")
    print("=============================================")

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("============= CPF já cadastrado =============")
            return
    
    novo_usuario = Usuario(nome, senha, logradouro, bairro, cidade, estado, celular, cpf)
    usuarios.append(novo_usuario)
    print("====== Cadastro realizado com sucesso! =======")

def realizar_login():
    nome = input("Nome: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.nome == nome and usuario.senha == senha:
            return usuario
    return None

def criar_conta_corrente(usuario):
    numero_conta = f"{len(usuario.contas_correntes)+1:04}"
    nova_conta = ContaCorrente(numero_conta)
    usuario.contas_correntes.append(nova_conta)
    print(f"====== Conta corrente criada! ======")
    print(f"Número da conta: {numero_conta}")

def acessar_conta_corrente(usuario):
    numero_conta = input("Informe o número da conta corrente: ")
    for conta in usuario.contas_correntes:
        if conta.numero == numero_conta:
            return conta
    return None

def deposito(conta):
    valor = float(input("Digite o valor do depósito: "))
    conta.saldo += valor
    conta.depositos_totais += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")

def saque(conta):
    if conta.saques_restantes > 0:
        valor = float(input("Digite o valor do saque: "))
        if valor <= conta.saldo:
            conta.saldo -= valor
            conta.saques_totais += valor
            conta.saques_restantes -= 1
            print(f"Saque de R${valor:.2f} realizado com sucesso! Saques restantes: {conta.saques_restantes}")
        else:
            print("======== Saldo insuficiente ========")
    else:
        print("======== Você atingiu o limite máximo de saques ========")

def extrato(conta):
    print("=============== Extrato ===============")
    print(f"Saldo: R${conta.saldo:.2f}")
    print(f"Total depositado: R${conta.depositos_totais:.2f}")
    print(f"Total sacado: R${conta.saques_totais:.2f}")
    print(f"Saques restantes: {conta.saques_restantes}")
    print(f"=======================================")

def mostrar_contas_correntes(usuario):
    print(f"=======================================")
    print("Contas Correntes:")
    for conta in usuario.contas_correntes:
        print(f"Número da Conta: {conta.numero}")
    print(f"=======================================")

def main():
    while True:
        print("=============== SEJA BEM VINDO ===============")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")
        print(f"=============================================")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            usuario_logado = realizar_login()
            if usuario_logado:
                while True:
                    print("========= CONTAS CORRENTE ===========")
                    print("1. Criar Conta Corrente")
                    print("2. Acessar Conta Corrente")
                    print("3. Retornar")
                    print("=====================================")
                    opcao = input("Escolha uma opção: ")

                    if opcao == "1":
                        criar_conta_corrente(usuario_logado)
                    elif opcao == "2":
                        conta_acessada = acessar_conta_corrente(usuario_logado)
                        if conta_acessada:
                            while True:
                                print("========= Sua Conta Corrente ===========")
                                print("1. Depósito")
                                print("2. Saque")
                                print("3. Extrato")
                                print("4. Mostrar Lista de Contas Correntes")
                                print("5. Voltar")
                                print("========================================")
                                opcao_conta = input("Escolha uma opção: ")

                                if opcao_conta == "1":
                                    deposito(conta_acessada)
                                elif opcao_conta == "2":
                                    saque(conta_acessada)
                                elif opcao_conta == "3":
                                    extrato(conta_acessada)
                                elif opcao_conta == "4":
                                    mostrar_contas_correntes(usuario_logado)
                                elif opcao_conta == "5":
                                    break
                                else:
                                    print("======= Opção inválida =======")
                        else:
                            print("== Conta corrente não encontrada ==")
                    elif opcao == "3":
                        break
                    else:
                        print("======= Opção inválida =======")
            else:
                print("=============== Login inválido ==============")
        elif escolha == "2":
            cadastrar_usuario()
        elif escolha == "3":
            break
        else:
            print("======= Opção inválida =======")

usuarios = []
main()
