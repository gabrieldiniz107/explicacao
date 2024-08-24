# escreva um programa que receba 4 notas e calcule a média aritmética
# se a média for maior ou igual a 6, imprima APROVADO
# se a média for menor que 6, imprima REPROVADO

nota1 = int(input("Qual o valor da nota 1?"))
nota2 = int(input("Qual o valor da nota 2?"))
nota3 = int(input("Qual o valor da nota 3?"))
nota4 = int(input("Qual o valor da nota 4?"))

media = (nota1 + nota2 + nota3 + nota4)/4

if media>=6 :
    print(media)
    print("Seu aluno está aprovado!")
elif media < 6 :
    print(media)
    print ("Seu aluno foi reprovado")