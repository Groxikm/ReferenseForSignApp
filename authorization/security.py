import token_service as ts
from flask import Request


class ErrorMessage:
    def __init__(self, message: str) -> None:
        self._message = message

    def get_dto(self) -> dict:
        return {
            "error-message": self._message
        }


class EndpointsSecurityService:
    def __init__(self) -> None:
        self._service = ts.TokenServiceImpl()

    def secure_by_validation_of_jwt(self, token: str) -> dict:
        if self._service.verify(token) == False:
            return ErrorMessage("token invalid").get_dto()

        return None
