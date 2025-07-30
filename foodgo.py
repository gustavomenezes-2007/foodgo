log = {}
print("FoodGo")
input("pressione enter para iniciar")


def cadastro_login():
    while True:
        print("\033c")
        conta = input("\nescolha uma opção\n 1 - cadastrar  2 - logar\n")

        if conta == "1":
            while True:
                nome = input("digite um nome de usuario\n")
                senha = input("digite sua senha(a senha deve conter ao menos 8 caracteres)\n")

                if len(senha) < 8:
                    print("insira uma senha valida")
                    input("pressione enter para continuar")
                    continue
                else:
                    log[nome] = senha
                    break

        elif conta == "2":
            while True:
                nome = input("digite um nome de usuario ou aperte 3 para retornar\n")

                if nome == "3":
                    break
                elif nome in log:
                    senha = input("digite sua senha\n")

                    if senha == log[nome]:
                        print("bem vindo")
                        input("pressione enter para continuar")
                        print("\033c")
                        menu()
                        return
                    else:
                        print("senha invalida")
                        input("pressione enter para continuar")
                        continue

                else:
                    print("invalido")
                    input("pressione enter para continuar")
                    continue
        else:
            print("\033c")
            print("digite um numero valido")
            input("pressione enter para continuar")
            continue


def menu():
    pedidos = {}
    carrinho = {}
    while True:
        print("\033c")
        escolha = input("1 - pedir  2 - pedidos  3 - sair\n")

        if escolha == "1":
            while True:
                print("""opções
1 - pão com ovo
2 - suco de uva
3 - finalizar pedido
4 - voltar""")
                decidir = input()

                if decidir == "1":
                    carrinho["pão com ovo"] = carrinho.get("pão com ovo", 0) + 1
                    print(carrinho)
                    input("pressione enter para continuar")

                elif decidir == "2":
                    carrinho["suco de uva"] = carrinho.get("suco de uva", 0) + 1
                    print(carrinho)
                    input("pressione enter para continuar")

                elif decidir == "3":
                    for item in carrinho:
                        pedidos[item] = pedidos.get(item, 0) + carrinho[item]
                    carrinho.clear()
                    print("\033c")
                    print("pedido finalizado")
                    input("pressione enter para continuar")
                    break

                elif decidir == "4":
                    carrinho.clear()
                    break

                else:
                    print("\033c")
                    print("invalido")
                    input("pressione enter para continuar")

        elif escolha == "2":
            print("\033c")
            print("seu pedido:")
            if pedidos:
                for item, valor in pedidos.items():
                    print(item, valor)
            else:
                print("\033c")
                print("nenhum pedido realizado")
            input("pressione enter para continuar")

        elif escolha == "3":
            break

        else:
            print("invalido")
            input("pressione enter para continuar")


cadastro_login()
