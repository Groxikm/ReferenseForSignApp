# token_service.py
from abc import ABC, abstractmethod
import jwt
import datetime
from datetime import timedelta
import settings

class TokenService(ABC):

    @abstractmethod
    def verify(self, token: str) -> bool:
        """
        checks if the token is valid
        """
        pass

    @abstractmethod
    def encode(self, username: str) -> str:
        """
        encodes the token
        """
        pass

class TokenServiceImpl(TokenService):

    def __init__(self) -> None:
        self._SECRET_KEY = settings.SECRET_KEY


    def verify(self, token: str) -> bool:
        try:
            decoded = jwt.decode(token, self._SECRET_KEY, algorithms=["HS256"])
            exp = datetime.datetime.strptime(decoded['expiration'], "%m/%d/%Y_%H:%M:%S")
            if datetime.datetime.now() > exp:
                return False
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False
        return False

    def encode(self, username: str) -> str:
        expiration = datetime.datetime.now()+timedelta(0, 300)
        payload = {
            'username': username,
            'expiration': expiration.strftime("%m/%d/%Y_%H:%M:%S")
        }
        token = jwt.encode(payload, self._SECRET_KEY, algorithm="HS256")
        
        return token
