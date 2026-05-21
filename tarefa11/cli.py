from users_wrapper import *

while True:
    print("\n1-Listar")
    print("2-Tarefas")
    print("3-Criar")
    print("4-Buscar")
    print("5-Atualizar")
    print("6-Deletar")
    print("0-Sair")

    op = input("Opção: ")

    if op == "1":
        users = get_users()

        for u in users:
            print(u["id"], "-", u["name"])


    elif op == "2":
        user_id = input("ID: ")

        todos = get_user_todos(user_id)

        for t in todos:
            print("-", t["title"])


    elif op == "3":
        nome = input("Nome: ")
        email = input("Email: ")

        user = create_user({
            "name": nome,
            "email": email
        })

        print(user)


    elif op == "4":
        user_id = input("ID: ")

        user = get_user(user_id)

        print(user)


    elif op == "5":
        user_id = input("ID: ")

        nome = input("Novo nome: ")
        email = input("Novo email: ")

        user = update_user(user_id, {
            "name": nome,
            "email": email
        })

        print(user)


    elif op == "6":
        user_id = input("ID: ")

        delete_user(user_id)

        print("Deletado")


    elif op == "0":
        break

    else:
        print("Inválido")