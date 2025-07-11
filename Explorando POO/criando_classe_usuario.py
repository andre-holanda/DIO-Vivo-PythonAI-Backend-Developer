''' Autor: André Holanda
    Projeto: Criando uma Classe de Usuários
    Data: 09/07/2025

    Desafio:
        Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.
    
    Entrada:
        Nome do usuário, número de telefone e plano.

    Saída:
        Mensagem indicando que o usuário foi criado com sucesso.
'''

# Classe UsuarioTelefone:
class UsuarioTelefone():
    """ Class UsuarioTelefone

        Parameters
    ---------------
    nome : str
        atributo referente ao nome do usuario
    numero : int
        atributo referente ao número telefônico do usuário
    plano : str
        atributo referente ao plano de telefonia do usuário
    """
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# Entrada:
nome = input().title()  
numero = input()  
plano = input().title()  

# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)