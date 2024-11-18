import re
from collections import Counter

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_frases(texto):
    frases = re.split(r'[.!?]', texto)
    return len([frase for frase in frases if frase.strip()])

def frequencia_palavras(texto):
    palavras = texto.lower().split()
    return dict(Counter(palavras))
def limpar_pontuacao(texto):
    return re.sub(r'[^\w\s]', '', texto)  # Remove pontuação

def frequencia_palavras(texto):
    texto_limpo = limpar_pontuacao(texto)
    palavras = texto_limpo.lower().split()
    return dict(Counter(palavras))


def palavra_mais_frequente(frequencias):
    return max(frequencias, key=frequencias.get), frequencias[max(frequencias, key=frequencias.get)]

def contar_caracteres(texto):
    caracteres = {'letras': 0, 'numeros': 0, 'pontuacao': 0, 'outros': 0}
    for char in texto:
        if char.isalpha():
            caracteres['letras'] += 1
        elif char.isdigit():
            caracteres['numeros'] += 1
        elif char in '.,!?;:':
            caracteres['pontuacao'] += 1
        else:
            caracteres['outros'] += 1
    return caracteres

def exibir_resultados(texto):
    num_palavras = contar_palavras(texto)
    
    num_frases = contar_frases(texto)
    
    frequencias = frequencia_palavras(texto)
    
    palavra, frequencia = palavra_mais_frequente(frequencias)
    
    caracteres = contar_caracteres(texto)
    
    print("\n--- Resultados da Análise ---")
    print(f"Número de palavras: {num_palavras}")
    print(f"Número de frases: {num_frases}")
    print("\nFrequência de palavras:")
    for palavra, frequencia in frequencias.items():
        print(f"{palavra}: {frequencia}")
    
    print(f"\nPalavra mais frequente: '{palavra}' com {frequencia} ocorrências.")
    print("\nContagem de caracteres:")
    for tipo, quantidade in caracteres.items():
        print(f"{tipo}: {quantidade}")
