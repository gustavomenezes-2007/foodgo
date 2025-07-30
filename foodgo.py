import json
import os

log = {}
pedidos_arquivo = "pedidos.json"


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def carregar_pedidos():
    if os.path.exists(pedidos_arquivo):
        with open(pedidos_arquivo, "r") as f:
            return json.load(f)
    return {}


def salvar_pedidos(pedidos):
    with open(pedidos_arquivo, "w") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)


def cadastro_login():
    while True:
        limpar_tela()
        conta = input("\nescolha uma opção\n 1 - cadastrar  2 - logar\n")

        if conta == "1":
            while True:
                nome = input("digite um nome de usuario\n")
                if nome in log:
                    print("Nome de usuário já existe, escolha outro.")
                    input("pressione enter para continuar")
                    continue

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
                        limpar_tela()
                        menu(nome)

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
            limpar_tela()
            print("digite um numero valido")
            input("pressione enter para continuar")
            continue


def menu(usuario):
    pedidos = carregar_pedidos()
    carrinho = {}
    endereco = None

    if usuario in pedidos:
        endereco = pedidos[usuario].get("endereco")

    while True:
        limpar_tela()
        print(f"Usuário: {usuario}")
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
                    if not carrinho:
                        print("Carrinho vazio! Adicione algum item antes de finalizar.")
                        input("pressione enter para continuar")
                        continue

                    if usuario not in pedidos:
                        pedidos[usuario] = {"itens": {}, "endereco": None}

                    # Atualizar itens do pedido
                    for item in carrinho:
                        pedidos[usuario]["itens"][item] = pedidos[usuario]["itens"].get(item, 0) + carrinho[item]

                    carrinho.clear()
                    limpar_tela()
                    print("Pedido finalizado!")

                    # Solicitar endereço se ainda não cadastrado ou se o usuário quiser alterar
                    if not pedidos[usuario]["endereco"]:
                        print("Por favor, informe seu endereço para entrega:")
                        endereco = input("Endereço: ")
                        pedidos[usuario]["endereco"] = endereco
                    else:
                        print(f"Endereço atual: {pedidos[usuario]['endereco']}")
                        mudar = input("Deseja alterar o endereço? (s/n): ").lower()
                        if mudar == 's':
                            endereco = input("Novo endereço: ")
                            pedidos[usuario]["endereco"] = endereco

                    salvar_pedidos(pedidos)
                    input("pressione enter para continuar")
                    break

                elif decidir == "4":
                    carrinho.clear()
                    break

                else:
                    limpar_tela()
                    print("invalido")
                    input("pressione enter para continuar")

        elif escolha == "2":
            limpar_tela()
            print("seu pedido:")
            if usuario in pedidos and pedidos[usuario]["itens"]:
                for item, valor in pedidos[usuario]["itens"].items():
                    print(f"{item}: {valor}")
                if pedidos[usuario]["endereco"]:
                    print(f"Endereço de entrega: {pedidos[usuario]['endereco']}")
            else:
                print("nenhum pedido realizado")
            input("pressione enter para continuar")

        elif escolha == "3":
            break

        else:
            print("invalido")
            input("pressione enter para continuar")


print("FoodGo")
input("pressione enter para iniciar")
cadastro_login()