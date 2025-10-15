def receber_numeros(qtd=10):
    numeros = []
    for i in range(qtd):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(num)
    return numeros

def verificar_presenca(numeros, numero_busca):
    posicoes = [i for i, num in enumerate(numeros) if num == numero_busca]
    return posicoes

def imprimir_resultado(numero_busca, posicoes):
    if posicoes:
        print(f"\nO número {numero_busca} está presente nas seguintes posições:")
        for pos in posicoes:
            print(f"Posição {pos}")
    else:
        print(f"\nO número {numero_busca} não está presente no array.")

def main():
    numeros = receber_numeros()
    numero_busca = int(input("\nDigite um número inteiro para verificar se está no array: "))
    posicoes = verificar_presenca(numeros, numero_busca)
    imprimir_resultado(numero_busca, posicoes)

if __name__ == "__main__":
 main()