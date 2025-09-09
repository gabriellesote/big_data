a = int(input("Nota 1: "))

if(a > 25):
  print("Nota inválida")
  exit()

b = int(input("Nota 2: "))
if(b > 25):
  print("Nota inválida")
  exit()

c = int(input("Nota 3: "))
if(c > 25):
  print("Nota inválida")
  exit()
d = int(input("Nota 4: "))
if(d > 25):
  print("Nota inválida")
  exit()

total = a + b + c + d
nome = input("Nome do aluno: ")

if (total >= 60):
  print(f"O aluno {nome} foi aprovado com o total de {total}")
elif (total <= 40 or total < 60):
   print(f"O aluno {nome} está de recuperação com o total de {total}")
else:
  print(f"O aluno {nome} foi reprovado com o total de {total}")
