def adicionar_contato(agenda):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    
    agenda.append(contato)
    print("Contato adicionado com sucesso!\n")


def listar_contatos(agenda):
    if not agenda:
        print("Nenhum contato cadastrado.\n")
        return
    
    print("\n--- LISTA DE CONTATOS ---")
    for i, contato in enumerate(agenda):
        print(f"{i} - {contato['nome']} | {contato['telefone']} | {contato['email']}")
    print()


def buscar_contato(agenda):
    nome = input("Digite o nome para buscar: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            print("Contato encontrado:")
            print(contato)
            print()
            return
    print("Contato não encontrado.\n")


def excluir_contato(agenda):
    nome = input("Digite o nome do contato para excluir: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            print("Contato excluído com sucesso!\n")
            return
    print("Contato não encontrado.\n")


def menu():
    agenda = []
    
    while True:
        print("""
===== AGENDA DIGITAL =====
1 - Adicionar contato
2 - Listar contatos
3 - Buscar contato
4 - Excluir contato
5 - Sair
""")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            listar_contatos(agenda)
        elif opcao == "3":
            buscar_contato(agenda)
        elif opcao == "4":
            excluir_contato(agenda)
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!\n")


menu()
