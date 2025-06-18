''' Autor: André Holanda
    Projeto: Criando uma Lista de Equipamentos
    Data: 17/06/2025

    Desafio: Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

    Requisitos:
        Formato esperado:
            O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.
        Entrada:
            Uma string representando o número de telefone.

        Saída:
            Uma mensagem indicando se o número de telefone é válido ou inválido.
'''

import re

# Função que recebe um número telefônico e valida conforme um padrão pré estabelecido
def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\)\s9\d{4}[-]\d{4}$"

    if re.match(pattern, phone_number):  
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita o número de telefone do usário
phone_number = input()  

# Chama a função para validar o número e salva o retorno na variável result
result = validate_numero_telefone(phone_number)

# Imprime o resultado se o número é válido ou não
print(result)