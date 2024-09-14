# Algotitmo média: criar um algoritmo que leia 4 notas
# e apresente uma média final

print("Olá! Vamos ver qual será sua média.")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("sua média é", media)
if(media >= 80):
    print("Você está aprovado!")
else:
    print("Você está reprovado!")

print("continue o bom trabalho!")