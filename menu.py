from leitura import ler_texto
from analise import exibir_resultados

def menu():
    while True:
        print("\nMenu:")
        print("1. Digitar texto diretamente")
        print("2. Analisar texto de um arquivo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            texto = ler_texto()
            exibir_resultados(texto)
        elif escolha == "2":
            arquivo = input("Digite o nome do arquivo (com extensão): ")
            texto = ler_texto(arquivo)
            if texto:
                exibir_resultados(texto)
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
