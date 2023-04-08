# 3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

# Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:

# VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

# POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

# define duas listas vazias para armazenar as notas dos alunos
notas_impares = []
notas_pares = []

# solicita ao professor as notas dos alunos ímpares
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
for i in range(1, 50, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    notas_impares.append(nota)

# solicita ao professor as notas dos alunos pares
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
for i in range(2, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    notas_pares.append(nota)

# calcula a média das notas dos alunos ímpares e pares
media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

# determina qual metade da sala teve a maior nota
if media_impares > media_pares:
    metade_maior = "ímpares"
elif media_pares > media_impares:
    metade_maior = "pares"
else:
    metade_maior = "as duas metades"

# exibe as médias das notas e qual metade teve a maior nota
print("A média das notas dos alunos ímpares é: {:.2f}".format(media_impares))
print("A média das notas dos alunos pares é: {:.2f}".format(media_pares))
print("A metade da sala com a maior nota é: {}".format(metade_maior))
