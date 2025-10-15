def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    resultado = 0
    negativo = False

    # Trata sinais
    if b < 0:
        b = -b
        negativo = True

    for _ in range(b):
        resultado = soma(resultado, a)

    return -resultado if negativo else resultado

def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)
    return resultado

def escolher_operacao(a, b, operacao):
    if operacao == "soma":
        return soma(a, b)
    elif operacao == "subtracao":
        return subtracao(a, b)
    elif operacao == "multiplicacao":
        return multiplicacao(a, b)
    elif operacao == "potencia":
        return potencia(a, b)
    else:
        return "Operação inválida."

def main():
    print("Operações disponíveis: soma, subtracao, multiplicacao, potencia")
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    operacao = input("Digite a operação desejada: ").lower()

    resultado = escolher_operacao(a, b, operacao)
    print(f"\nResultado da operação '{operacao}' entre {a} e {b}: {resultado}")

if __name__ == "__main__":
    main()