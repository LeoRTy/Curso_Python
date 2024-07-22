
user_nome = input("Digite seu nome: ")

print("Olá " + user_nome)

user_idade = int(input(user_nome + " Agora digite sua idade "))

if user_idade < 18:
	print("Você não tem idade")
else:
	print("Ok, Permitido")