
print("calculadora")

decisao = "nao"


while (decisao.lower() == "nao" or decisao.lower() == "n" ):

	num1 = input("digite um numero: ")
	num1 = int(num1)
	operador = input("digite um operador (+-/***): ")
	num2 = int(input("digite um numero: "))

	#soma
	if operador == "+":
		operacao = num1 + num2

	#- subtracao
	if operador == "-":
		operacao = num1 - num2

	#* multiplicacao
	if operador == "*":
		operacao = num1 * num2

	#/ divisao
	if operador == "/":
		operacao = num1 / num2

	#** exponencial
	if operador == "**":
		operacao = num1 ** num2

	print("resultado")
	print(operacao)	

	decisao = input("deseja sair? Responda (Sim / Nao)")		
	
	pass