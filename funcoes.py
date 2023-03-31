# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números 

def par():
    for i in range(1, 21):
        if i%2==0:
            print(i)

par()



# Exercício 2 - Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def palavra(par):
    print(par.upper())

var = 'hello world'
palavra(var)



# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def func(fazoL):
    fazoL.append(5)
    fazoL.append(6)
    print(listinha)

listinha = [1,2,3,4]
func(listinha)



# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def formal(*form):
    if len(form) > 1:
        for i in form:
            print(f'Lista de argumentos: {i}')
    else:
        print(f'Argumento: {form[0]}')

formal(10)
formal(32, 54, 76,87)



# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
lam = lambda x, y: x + y

soma = lam(10, 20)
print(soma)

