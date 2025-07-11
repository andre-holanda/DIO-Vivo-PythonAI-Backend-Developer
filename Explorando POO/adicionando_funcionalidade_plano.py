''' Autor: André Holanda
    Projeto: Adicionando Funcionalidades ao Plano
    Data: 09/07/2025

    Desafio:
        Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

    Condições da verificação do saldo:
        - Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        - Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
        - Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    Entrada:
        Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.
    
    Saída:
        Mensagem personalizada de acordo o saldo do cliente.
'''

# Classe UsuarioTelefone:
class PlanoTelefone():
    """ Classe PlanoTelefone
            Classe que mantem as informações do nome do usuário e saldo do plano contratado.

        Parameters
    ---------------
    nome : str
        atributo referente ao nome do usuario
    saldo : int
        atributo referente ao saldo do plano do usuário
    """
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo
    
    def nome(self):
        """Metodo nome
        Return
        ---------------
        nome : str
            retorna o nome do usuario
        """
        return self._nome
    
    def saldo(self):
        """Metodo saldo
        Return
        ---------------
        saldo : str
            retorna o saldo do plano
        """
        return self._saldo
    
    def verificar_saldo(self):
        """Metodo verificar_saldo
        Return
        ---------------
        saldo : str
            retorna o saldo do plano
        """
        return self.saldo()
    
    def mensagem_personalizada(self):
        """Metodo mensagem_personalizada
        Return
        ---------------
            retorna uma mensagem personalizada de acordo com o saldo do usuario
        """
        saldo = self.saldo()
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

# Classe UsuarioTelefone:
class UsuarioTelefone:
    """ Classe UsuarioTelefone
            Classe que mantem as informações do nome do usuário e saldo do plano contratado.

        Parameters
    ---------------
    nome : str
        atributo referente ao nome do usuario
    plano : str
        atributo referente a informação do plano contratado pelo usuário
    """
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        """ Metodo verificar_saldo
                método que retorna o saldo da conta do usuário, e uma mensagem personalizada
        Return:
        ---------------
        saldo : int
        mensagem : str
        """
        saldo = self.plano.saldo()
        mensagem = self.plano.mensagem_personalizada()

        return saldo, mensagem

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input().title()
nome_plano = input().title()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)
