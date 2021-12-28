"""
Desafio
Crie uma função que receba um numero qualquer e encontre o maior numero formado por digitos consecutivos naquele numero
"""
"""
EX1
entrada - 53590
saida - 90

EX2
entrada - 674030098567819
saida - 5678

EX3
entrada - 9012364509789
saida - 90123

EX4
entrada - 9067
saida - 90
"""


def pegarMaiorSequencia():
    valor = str(entrada).strip()
    maiorSequencia = ""
    sequenciaAtual = valor[0]

    for giro in range(len(valor) - 1):  # Toda vez que girar anda uma casa na variavel
        valorAtual = valor[giro]
        proximoValor = valor[giro + 1]

        if int(proximoValor) == int(valorAtual) + 1 or (valorAtual == "9" and proximoValor == "0"):
            # Calcular em int, pois str não soma corretamente
            sequenciaAtual += proximoValor

        else:  # Quebra de sequencia

            if sequenciaAtual > maiorSequencia:
                # Se a sequencia atual foi maior, salvara
                maiorSequencia = sequenciaAtual

            sequenciaAtual = proximoValor  # usar proximo valor para recomeçar loop

    if int(sequenciaAtual) >= int(maiorSequencia):
        maiorSequencia = sequenciaAtual

    return maiorSequencia


entrada = int(input('digite uma sequencia de numeros:  '))
saida = pegarMaiorSequencia()
print(f'A maior sequencia é:', saida)
