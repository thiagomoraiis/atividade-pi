# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

pergunta = str(input('Qual o dia da semana?'))
if pergunta == 'sabado' or pergunta == 'domingo':
    print('Hoje é dia de descansar')
else:
    print('Vai trabalhar, baiano')



# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

frutas = ['manga', 'banana', 'maça', 'morango', 'melancia']
if 'morango' in frutas:
    print('Morango esta na lista')
else:
    print('Morango não esta na lista')



# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

lista = []
tupla = (1, 2, 3, 4)
for i in tupla:
    i *= 2
    lista.append(i)

print(lista)
# 


# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela

for i in range(100, 150):
    if i%2==0:
        print(i)



# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela

temperatura = 40
while temperatura > 35:
    print(temperatura)
    temperatura -= 1


# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0
while contador < 100:
    print(contador)
    contador += 1
    if contador == 23:
        break



# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

lista = []
var = 4
while var <= 20:
    print(var)
    var += 1
    if var%2==0:
        lista.append(var)
 
print(lista)



# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)

nums = list(range(5, 45, 2))
print(nums)



# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.

temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')


# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 
count = frase.count('r')
print(f'A quantidade de letras r presente na frase é {count}')