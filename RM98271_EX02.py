# 2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana        (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

# solicita ao usuário a quantidade de votos de cada dia da semana
segunda = int(input("Digite a quantidade de votos para segunda-feira: "))
terca = int(input("Digite a quantidade de votos para terça-feira: "))
quarta = int(input("Digite a quantidade de votos para quarta-feira: "))
quinta = int(input("Digite a quantidade de votos para quinta-feira: "))
sexta = int(input("Digite a quantidade de votos para sexta-feira: "))

# cria uma lista com os votos de cada dia da semana
votos = [segunda, terca, quarta, quinta, sexta]

# verifica qual o dia da semana com maior número de votos
dia_escolhido = votos.index(max(votos))  # index retorna o índice do maior valor na lista
dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
nome_dia_escolhido = dias_da_semana[dia_escolhido]

# exibe o dia escolhido com o número de votos recebidos
print("O dia escolhido foi {} com {} votos.".format(nome_dia_escolhido, max(votos)))
