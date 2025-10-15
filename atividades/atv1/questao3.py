def receber_numeros(qtd=10):
    numeros = []
    for i in range(qtd):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(num)
    return numeros

def substituir_negativos_por_zero(numeros):
    numeros_alterados = [0 if num < 0 else num for num in numeros]
    return numeros_alterados

def imprimir_antes_e_depois(original, alterado):
    print("\nAntes da alteração:")
    print(original)
    print("\nDepois da alteração (negativos substituídos por 0):")
    print(alterado)

def main():
    numeros = receber_numeros()
    numeros_alterados = substituir_negativos_por_zero(numeros)
    imprimir_antes_e_depois(numeros, numeros_alterados)

if __name__ == "__main__":
    main()