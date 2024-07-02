import random
import os

def menu():
    print("""
    ██████╗░███████╗███╗░░░███╗  ██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░
    ██╔══██╗██╔════╝████╗░████║  ██║░░░██║██║████╗░██║██╔══██╗██╔══██╗
    ██████╦╝█████╗░░██╔████╔██║  ╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║
    ██╔══██╗██╔══╝░░██║╚██╔╝██║  ░╚████╔╝░██║██║╚████║██║░░██║██║░░██║
    ██████╦╝███████╗██║░╚═╝░██║  ░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝
    ╚═════╝░╚══════╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░
    """)

    print("""
    Digite 1 para cadastrar um produto
    Digite 2 para alterar um produto
    Digite 3 para gerar um relatorio
    Digite 4 para vender
    Digite 5 para sair
    """)


produtos = []

def casdastrar():
        # função para cadastrar um produto na loja
        nome_do_produto = input("Digite o nome do produto: ")
        descricao_do_produto = input("Digite uma descrição para o produto: ")
        quantidade_do_produto = int(input("Digite a quantidade do produto: "))
        if quantidade_do_produto < 0:
            while quantidade_do_produto < 0:
                print("Quantidade invalida, por favor digita uma nova quantidade: ")
                quantidade_do_produto = int(input("Digite uma nova quantidade: "))
        codigo_do_produto = random.randrange(10000, 99999)
        print(f"Codigo do produto = {codigo_do_produto}")
        produto_para_cadastrar = {
            "nome":nome_do_produto,
            "descricao":descricao_do_produto,
            "quantidade":quantidade_do_produto,
            "codigo":codigo_do_produto
        }
        produtos.append(produto_para_cadastrar)
        print("Produto cadastrado com sucesso!!")

        retornar_ao_menu()


def alterar():
        # função para alterar o nome e descrição de um produto na loja
        codigo_produto = int(input("Digite o codigo do produto que deseja alterar: "))
        produto_encontrado = None
        for produto in produtos:
             if produto["codigo"] == codigo_produto:
                  produto_encontrado = produto
                  break
        if produto_encontrado:
            novo_nome_do_produto = input("Digite o novo nome do produto: ")
            novo_descricao_do_produto = input("Digite a nova descrição do produto: ")
            produto_encontrado["nome"] = novo_nome_do_produto
            produto_encontrado["descricao"] = novo_descricao_do_produto
            print("Produto alterado com sucesso!")
        else:
            print("Produto não encontrado!")

        retornar_ao_menu()


def gerar_relatorio():
    # função para gerar um relatorio dos produtos da loja
    print(f"{"Nome do produto".ljust(20)} | {"Descrição".ljust(20)} | {"Quantidade".ljust(20)} | {"Codigo".ljust(20)}")
    print("~" * (len(f"{"Nome do produto".ljust(15)} | {"Descrição".ljust(15)} | {"Quantidade".ljust(15)} | {"Codigo".ljust(15)}")))
    for produto in produtos:
        nome_produto = produto["nome"]
        descricao = produto["descricao"]
        quantidade = str(produto["quantidade"])
        codigo = str(produto["codigo"])
        print(f"{nome_produto.ljust(20)} | {descricao.ljust(20)} | {quantidade.ljust(20)} | {codigo.ljust(20)}")

    retornar_ao_menu()


def vender():
    # função que vende os produtos da loja
    codigo_produto_venda = int(input("Digite o codigo do produto que deseja vender: "))
    produto_para_venda = None
    for produto in produtos:
          if produto["codigo"] == codigo_produto_venda:
               produto_para_venda = produto
               break
    if produto_para_venda:
        if produto["quantidade"] > 0:
            print("Produto vendido!")
            produto["quantidade"] -= 1
        else:
            print("Produto fora de estoque!")
    else: 
        print("Produto não encontrado!")
    
    retornar_ao_menu()
    

def retornar_ao_menu():
    # função que volta ao menu principal apos cada ação
    input("Digite qualquer tecla para voltar ao menu: ")
    os.system("cls")
    main()


def opcao():
    # função de opções de escolha do que o usuario escolher fazer 
    op = int(input("Digite sua opção: "))
    match op:
        case 1:
            casdastrar()
        case 2:
            alterar()
        case 3:
            gerar_relatorio()
        case 4:
            vender()
        case 5:
            print("Saindo do programa...")
        case _:
            print("Opção inválida!")


def main():
    menu()
    opcao()


if __name__ == "__main__":
    main()