total_excelente = 0
total_bom = 0
total_ruim = 0
for i in range(1, 11):
 Nome = input("Digite seu nome: ")
 Idade = int(input("Digite sua idade: "))
 Opiniao = input("Digite sua opinião sobre o nosso serviço (1: Excelente, 2: Bom, 3: Ruim): ")
 if Opiniao == "1":
     total_excelente += 1
 elif Opiniao == "2":
     total_bom += 1
 elif Opiniao == "3":
     total_ruim += 1
print("RESULTADO DA PESQUISA:")
print("a) Quantidade de respostas EXCELENTE:", total_excelente)
print("b) Quantidade de respostas RUIM:", total_ruim)