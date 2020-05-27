Dark sky é um serviço de previsão do tempo por API. Temos uma função que faz uma requisição para a api
do Dark sky passando a latitude e a longitude de algum lugar no planeta e a api retorna a temperatura. Nossa função
converte para celsius e retorna o valor da temperatura.


Escreva um teste que seja possível testar off-line a chamada para api do Dark sky e a conversão para celsius.
Use a bibliteca Pytest e os seguntes dados para testar a função **get_temperature**.

    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16
