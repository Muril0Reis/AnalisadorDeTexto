import re
from collections import Counter

def limpar_pontuacao(texto):
    texto = texto.lower()  # Converte para minúsculas
    texto = re.sub(r'[^\w\s]', '', texto)  # Remove pontuações
    texto = re.sub(r'\s+', ' ', texto)  # Substitui múltiplos espaços por um único
    return texto.strip()  # Remove espaços extras no início e no fim

def contar_palavras(texto):
    texto_limpo = limpar_pontuacao(texto)
    palavras = texto_limpo.split()
    return len(palavras)

def contar_frases(texto):
    frases = re.split(r'[.!?]', texto)  # Divide por ., !, ou ?
    return len([frase.strip() for frase in frases if frase.strip()])

def frequencia_palavras(texto):
    texto_limpo = limpar_pontuacao(texto)
    palavras = texto_limpo.split()
    return Counter(palavras)

def palavra_mais_frequente(frequencias):
    max_frequencia = max(frequencias.values())
    palavras_mais_frequentes = [
        palavra for palavra, freq in frequencias.items() if freq == max_frequencia
    ] 
    return palavras_mais_frequentes, max_frequencia

def exibir_resultados(texto):
    print(f"Texto original:\n{texto}\n")

    texto_limpo = limpar_pontuacao(texto)
    print(f"Texto limpo:\n{texto_limpo}\n")

    num_palavras = contar_palavras(texto)
    num_frases = contar_frases(texto)
    frequencias = frequencia_palavras(texto)
    palavras, frequencia = palavra_mais_frequente(frequencias)

    print("\n--- Resultados da Análise ---")
    print(f"Número de palavras: {num_palavras}")
    print(f"Número de frases: {num_frases}")
    print("\nFrequência de palavras:")
    for palavra, frequencia in frequencias.items():
        print(f"{palavra}: {frequencia}")
    if palavras:
        print(
            f"\nPalavras mais frequentes: {', '.join(palavras)} com {frequencia} ocorrências."
        )
    else:
        print("\nNenhuma palavra foi encontrada.")
