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
