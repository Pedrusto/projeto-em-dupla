class Usuario:
    #Representa um usuário do sistema.

    def __init__(self, nome, email):
        #Inicializa um novo usuário com nome e email.
        self.nome = nome
        self.email = email

    def __str__(self):
        #Retorna dados por texto do usuário.
        return f"Nome: {self.nome}, Email: {self.email}"


def exibir_menu():
    #Exibe o menu de opções para o usuário.
    print("\n----------- Menu -----------")
    print("1. Cadastrar Usuário")
    print("2. Exibir Lista de Usuários")
    print("3. Sair do Sistema")
    print("----------------------------")


def cadastrar_usuario():
    #Cadastra um novo usuário.
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    usuario = Usuario(nome, email)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def exibir_lista_usuarios():
    #Exibe a lista de usuários cadastrados.
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        print(usuario)
    print("------------")


def main():
    #Função principal do sistema.
    global usuarios  
    usuarios = []  # Inicializa a lista de usuários vazia

    print("\nBem-vindo ao Sistema!")

    while True:
        exibir_menu()
        opcao = input("Digite a opção a ser escolhida: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            exibir_lista_usuarios()
        elif opcao == "3":
            print("\nSaindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()