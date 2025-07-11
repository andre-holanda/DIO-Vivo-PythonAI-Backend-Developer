''' Autor: André Holanda
    Projeto: Realizando Chamadas
    Data: 09/07/2025

    Desafio:
        Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

    Entrada:
        Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

    Saída:
        Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.
'''
# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    """ Classe UsuarioTelefone
            Classe que mantem as informações do nome do usuário, o número do telefone e o saldo do plano contratado.

        Parameters
    ---------------
    nome : str
        atributo referente ao nome do usuario
    numero : int
        atributo referente ao número do telefône do usuário (possui uma mascara)
    plano : str
        atributo referente a informação do plano contratado pelo usuário
    """
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        """ Metodo fazer_chamada
                método que verifica o custo da ligação, e se tem saldo no plano para realizar a ligação.
        Parameters
        ---------------
        destinatario : int
            atributo referente ao número de telefône do destinatário
        duracao : int
            atributo referente ao tempo de ligação

        Return:
        ---------------
        mensagem : str
            mensagem personalizada com o sucesso da ligação ou saldo insuficiente.
        """
        custo = self.plano.custo_chamada(duracao)

        if self.plano.verificar_saldo() >= custo:
            self.plano.deduzir_saldo(custo)
            saldo_restante = self.plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return f"Saldo insuficiente para fazer a chamada."

# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    """ Classe Plano
            Classe que mantem a informação do saldo do usuário.

        Parameters
    ---------------
    saldo_inicia : int
        atributo referente ao saldo iniciado do plano
    """
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    # Metodo verificar_saldo
    def verificar_saldo(self):
        """Metodo verificar_saldo
        Return
        ---------------
        saldo : str
            retorna o saldo do plano
        """
        return self.saldo

    # Metodo custo_chamada
    def custo_chamada(self, duracao):
        """ Metodo custo_chamada
                método que calcula o valor total da chamada com base na duração da chamada.
        Parameters
        ---------------
        duracao : int
            atributo referente ao tempo de ligação

        Return:
        ---------------
        custo : float
            Retorna o custo total da chamada.
        """
        custo = duracao * 0.10
        return custo

    # Metodo deduzir_saldo
    def deduzir_saldo(self, custo):
        """ Metodo deduzir_saldo
                método que atualiza o saldo do plano.
        Parameters
        ---------------
        custo : float
            atributo referente ao custo da ligação, que é debitado do saldo atual
        """
        self.saldo -= custo

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    """ Classe UsuarioPrePago
            Classe que herda os atributos da classe pai (UsuarioTelefone).
    """
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))