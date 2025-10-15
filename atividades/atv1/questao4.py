def receber_numeros(mensagem, qtd=6):
    numeros = []
    print(mensagem)
    while len(numeros) < qtd:
        try:
            num = int(input(f"Digite o {len(numeros)+1}º número: "))
            if num < 1 or num > 60:
                print("Número inválido! Digite um número entre 1 e 60.")
            elif num in numeros:
                print("Número repetido! Digite um número diferente.")
            else:
                numeros.append(num)
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    return numeros

def contar_acertos(sorteados, jogados):
    return len(set(sorteados) & set(jogados))

def main():
    sorteados = receber_numeros("Informe os 6 números sorteados na Mega-Sena:")
    jogados = receber_numeros("Informe os 6 números que você jogou:")
    
    pontos = contar_acertos(sorteados, jogados)
    
    print(f"\nVocê acertou {pontos} número(s)!")
    if pontos > 0:
        acertos = set(sorteados) & set(jogados)
        print(f"Números acertados: {sorted(acertos)}")
    else:
        print("Infelizmente, nenhum número foi acertado.")

if __name__ == "__main__":
    main()