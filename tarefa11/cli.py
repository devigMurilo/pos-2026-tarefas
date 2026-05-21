from users_wrapper import (
    get_users,
    get_user,
    create_user,
    update_user,
    delete_user,
    get_user_todos
)

while True:
    print("\n===== MENU =====")
    print("1 - Listar todos usuários")
    print("2 - Listar tarefas de um usuário")
    print("3 - Criar usuário")
    print("4 - Ler usuário por ID")
    print("5 - Atualizar usuário")
    print("6 - Deletar usuário")
    print("0 - Sair")

    option = input("Escolha uma opção: ")

    
    if option == "1":
        users = get_users()

        for user in users:
            print(f'{user["id"]} - {user["name"]}')

    
    elif option == "2":
        user_id = input("ID do usuário: ")

        todos = get_user_todos(user_id)

        for todo in todos:
            status = "[x]" if todo["completed"] else "[ ]"
            print(f'{status} {todo["title"]}')

    
    elif option == "3":
        name = input("Nome: ")
        email = input("Email: ")

        new_user = create_user({
            "name": name,
            "email": email
        })

        print("Usuário criado:")
        print(new_user)


    elif option == "4":
        user_id = input("ID do usuário: ")

        user = get_user(user_id)

        print(user)

    
    elif option == "5":
        user_id = input("ID do usuário: ")

        name = input("Novo nome: ")
        email = input("Novo email: ")

        updated_user = update_user(user_id, {
            "name": name,
            "email": email
        })

        print("Usuário atualizado:")
        print(updated_user)

    
    elif option == "6":
        user_id = input("ID do usuário: ")

        success = delete_user(user_id)

        if success:
            print("Usuário deletado com sucesso!")


    elif option == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
