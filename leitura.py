def ler_texto(arquivo=None):
    if arquivo:
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return ""
    else:
        return input("Digite o texto para análise: ")
