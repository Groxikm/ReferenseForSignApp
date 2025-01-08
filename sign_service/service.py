from abc import abstractmethod, ABC
import sign_service.signature as signature
from abstractions.data_access import repository


class SignatureService:
    def __init__(self, repo: repository.Repository) -> None:
        self._repo = repo

    def add_new(self, signature_dto: dict) -> signature.Signature:
        return signature.from_db_dto(self._repo.create(signature.Signature.from_web_dto(signature_dto)))

    def update(self, signature_dto: dict) -> signature.Signature:
        self._repo.update(signature.Signature.from_web_dto(signature_dto))
        signature_obj = signature.from_db_dto(self._repo.find_by_id(signature_dto.get("id")))
        return signature_obj

    def delete(self, id: str) -> None:
        self._repo.delete_by_id(id)

    def find_by_id(self, id: str) -> signature.Signature:
        return signature.from_db_dto(self._repo.find_by_id(id))

    def find_all_by_page(self, start_from: str, page_size: int) -> list[signature.Signature]:
        db_dtos = self._repo.find_all_by_page(start_from, page_size)
        signature_dtos = list()
        for dto in db_dtos:
            signature_dtos.append(signature.from_db_dto(dto))
        return signature_dtos
