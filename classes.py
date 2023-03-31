# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, 
# passando 2 parâmetros e depois faça uma chamada aos atributos e métodos

# from math import sqrt

# class Rocket():
     
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
        
#     def move_rocket(self, x_increment=0, y_increment=1):
#         self.x += x_increment
#         self.y += y_increment
        
#     def print_rocket(self):
#         print(self.x, self.y)
        
# roc1 = Rocket(94, 23)
# roc1.move_rocket()
# roc1.print_rocket()


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

# class Pessoa():
#     def __init__(self, nome, cidade, telefone, email):
#         self.nome = nome
#         self.cidade = cidade
#         self.telefone = telefone
#         self.email = email

#     def falar(self):
#         print(f'OI, meu nome é {self.nome}')

#     def estudar(self):
#         print('Estou estudando')

# pessoa = Pessoa('Thiago', 'José da Penha', '2943-4343', 'thiago@email.com')
# pessoa.falar()
# pessoa.estudar()



# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

# class SmartFone():
#     def __init__(self, tamanho, interface):
#         self.tamanho = tamanho
#         self.interface = interface

    
# class MP3player(SmartFone):
#     def __init__(self, tamanho, interface, capacidade):
#         super().__init__(tamanho, interface)
#         self.capacidade = capacidade


