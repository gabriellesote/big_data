def receber_dados(qtd=10):
    alunos = []
    for i in range(qtd):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nota = float(input(f"Digite a nota do aluno {nome}: "))
        alunos.append({"nome": nome, "nota": nota})
    return alunos

def calcular_media(alunos):
    return sum(aluno["nota"] for aluno in alunos) / len(alunos)

def encontrar_maior_menor(alunos):
    maior = max(alunos, key=lambda x: x["nota"])
    menor = min(alunos, key=lambda x: x["nota"])
    return maior, menor

def listar_abaixo_media(alunos, media):
    return [aluno for aluno in alunos if aluno["nota"] < media]

def listar_acima_ou_igual_media(alunos, media):
    return [aluno for aluno in alunos if aluno["nota"] >= media]

def imprimir_resultados(alunos):
    media = calcular_media(alunos)
    print(f"\nMédia das notas: {media:.2f}")

    maior, menor = encontrar_maior_menor(alunos)
    print(f"Maior nota: {maior['nota']} - Aluno: {maior['nome']}")
    print(f"Menor nota: {menor['nota']} - Aluno: {menor['nome']}")

    abaixo = listar_abaixo_media(alunos, media)
    print("\nAlunos com nota abaixo da média:")
    for aluno in abaixo:
        print(f"{aluno['nome']} - Nota: {aluno['nota']}")

    acima = listar_acima_ou_igual_media(alunos, media)
    print("\nAlunos com nota acima ou igual à média:")
    for aluno in acima:
        print(f"{aluno['nome']} - Nota: {aluno['nota']}")


def main():
    alunos = receber_dados()
    imprimir_resultados(alunos)


if __name__ == "__main__":
    main()
