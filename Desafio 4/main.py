import jwt


def create_token(data, secret):
    token = jwt.encode(data, secret, algorithm= 'HS256') # irei criar o token nessa linha.
    return token

def verify_signature(token):
    try: # aqui ele irá testar se o da algum erro na aplicacao do metodo do jwt.
        encoder = jwt.decode(token, 'acelera', algorithms='HS256')

    except jwt.exceptions.InvalidSignatureError: # verificando.
        return {"error": 2}

    else:
        return encoder # caso nao de erro, ele ira retornar o que foi decodificado.