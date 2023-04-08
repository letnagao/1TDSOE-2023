# 1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

# Nível 
# Porcentagem sobre o faturamento

# Basic
# 30%

# Silver
# 20%

# Gold
# 10%

# Platinum
# 5%

assinatura = input("Digite o tipo de assinatura (Basic, Silver, Gold ou Platinum): ").lower()
faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

if assinatura == "basic":
    bonus = faturamento_anual * 0.3
elif assinatura == "silver":
    bonus = faturamento_anual * 0.2
elif assinatura == "gold":
    bonus = faturamento_anual * 0.1
elif assinatura == "platinum":
    bonus = faturamento_anual * 0.05
else:
    print("Assinatura inválida!")
    bonus = 0

print("O valor do bônus a ser pago pelo cliente é de: R$ {:.2f}".format(bonus))
