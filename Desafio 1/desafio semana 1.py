from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]
# funcao que define se a ligacao foi feita de manha ou noite.
def classify_the_period(time):

    first_period = range(6, 23) #periodo da manha

    if time in first_period:
        return 0
    else:
        return 1

# funcao que calcula o valor da ligacao caso pertencam ao mesmo periodo.
def calc_same(delta, period):
    constant_value = 0.36
    if period == 0:
        return round(constant_value + 0.09 * delta, 2)
    else:
        return constant_value

# funcao que calcula o valor da ligacao caso pertencam a periodos diferentes.
def calc_not_same(delta,hour_start,hour_end,period_start):
    limit_0 = 22
    limit_1 = 6
    constant_value = 0.36

    if period_start == 0:
        time = limit_0 - hour_start
        delta2 = delta - time
        return round(constant_value + delta2 * 0.09 + 0.36,2)
    else:
        time = limit_1 - hour_end
        delta2 = delta - time
        return round(constant_value + delta2 * 0.09 + 0.36,2)

def classify_by_phone_number(records):
    results = [] # variavel que irei usar para armazenar os resultados.
    numbers = [] # variavel que irei usar para armazenar todos os numeros que ja ligaram(comecaram a ligacao).
    # para cada ligacao em records
    for call in records:
        # crio duas variaveis para armazenar o tempo que comecou e o tempo que acabou.
        start = datetime.fromtimestamp(call['start'])
        end = datetime.fromtimestamp(call['end'])

        # calculo a duracao da chamada
        delta = end - start

        # transformo em string para poder manipular
        start = str(start)
        end = str(end)
        delta = str(delta)

        """"
        "_" significa que nao quero armazenar na memoria o valor da variavel.
        Mas quero armazenar o outro(esse metodo ira retornar dois valores)
        Estou fazendo isso para ter a duracao da chamada, ja que a funcao retorna assim:
        00:00:00, e dessa forma nao posso trabalhar a multiplicacao para saber o valor.
        
        Primeiro separo a variavel, ficando = 00:, 00:00(sendo _ o valor de 00 e "delta_int" = 00:00
        Depois repito o processo, ficando = 00, :00(sendo delta_int o valor de 00 e _ como :00.
        Apos isso, transformo o valor de denta_int em um inteiro.
        
        Obs: Os proximos 3 blocos de codigo fazem a mesma coisa, so muda que no lugar de 'delta_int'
        eu troco para as outras variaveis que eu quero trabalhar.
        """
        _, delta_int = delta.split(':', 1)
        delta_int, _ = delta_int.split(':')
        delta_int = int(delta_int)

        _ , hour_start = start.split(' ')
        hour_start , _ = hour_start.split(':', 1)
        hour_start = int(hour_start)

        _, hour_end = end.split(' ')
        hour_end, _ = hour_end.split(':', 1)
        hour_end = int(hour_end)

        # Chamo a funcao para classificar o periodo
        period_start = classify_the_period(hour_start)
        period_end = classify_the_period(hour_end)

        # Se o periodo for igual, chamo a funcao para calcular o valor
        if period_start == period_end:
            value = calc_same(delta_int, period_start)

        # Caso contrario, chamo a outra funcao que calcula o valor.
        else:
            value = calc_not_same(delta, hour_start, hour_end, period_start)

        # Verifico se o numero que ligou para a ligacao analisada ja ligou alguma vez.
        if call['source'] in numbers:
            #Caso sim, procuro o indice dele na variavel results
            for test in range(len(results)):
                if results[test]['source'] == call['source']:
                    """"
                    Quando eu encontrar tenho que atualizar o valor de sua conta, que e a soma das chamadas
                    antigas com a atual
                    """
                    results[test]['total'] += value
                    results[test]['total'] = round(results[test]['total'], 2)
        #caso seja o numero novo, simplesmente adiciono ele a lista results.
        else:
            results.append({'source' : call['source'], 'total' : value})
        #adiciono ao registros de todos os numeros o numero que ligou da ligacao atual
        numbers.append(call['source'])
    """"
    Apos ter feito o calculo de todas as contas, organizo de maneira ordenada decrescente,
    para isso uso a funcao lamba(uma funcao que recebe varios parametros, mas so pode executar uma acao)
    ela irá usar como referencia de ordenacao os valores que estao na chave 'total'.
    """
    return sorted(results, key = lambda element: element['total'], reverse = True)
