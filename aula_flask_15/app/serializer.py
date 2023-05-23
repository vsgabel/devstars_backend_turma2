import jwt
import datetime

class Serializer:
    '''
    Baseado no código de Robin Uphoff, obtido em 15 de junho de 2022
    Classe estática com dois métodos para geração de um token e sua confirmação utilizando
    a biblioteca PyJWT. Para instalar este requisito:
    pip install pyjwt
    Referências:
    https://stackoverflow.com/questions/71292764/which-timed-jsonwebsignature-serializer-replacement-for-itsdangerous-is-better
    '''
    @staticmethod
    def generate_confirmation_token(secret_key:str, user_id:int, expiration=86400):
        '''
        Gera um token de confirmação com a id do usuário e uma expiração.
        Recebe como retorno um token de 121 caracteres.
        secret_key: str, chave utilizada nas configurações do app
        user_id: int, id do usuário que será confirmada
        expiration: int, número de segundos para expirar o token
        (str, int, int) -> str
        '''
        token = jwt.encode(
            {
                "confirm": user_id,
                "exp": datetime.datetime.now(tz=datetime.timezone.utc)
                       + datetime.timedelta(seconds=expiration)
            },
            secret_key,
            algorithm="HS256"
        )
        return token

    @staticmethod
    def confirm(secret_key:str, user_id:int, token:str, treshold=10):
        '''
        Confirma o token gerado pelo método generate_confirmation_token,
        considerando treshold segundos de tolerância.
        secret_key: str, chave utilizada nas configurações do app
        user_id: int, id do usuário logado
        token: str, token gerado anteriormente
        treshold: int, segundos de tolerância para a validação da chave
        (str, int, str, int) -> bool
        '''
        try:
            data = jwt.decode(
                token,
                secret_key,
                leeway=datetime.timedelta(seconds=treshold),
                algorithms=["HS256"]
            )
        except:
            return False

        if data.get('confirm') != user_id:
            return False
        return True