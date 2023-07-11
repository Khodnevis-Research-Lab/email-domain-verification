import abc
from typing import Type, TypeVar
from .emails import Email


T = TypeVar("T")


class ValidatorInterface(abc.ABC):
    __criterion: Type[T]

    @abc.abstractmethod
    def validate_criterion(self) -> None:
        pass

    @abc.abstractmethod
    def check(self, email: Email) -> bool:
        pass


class VerificationInterface(abc.ABC):
    @abc.abstractmethod
    def validation(self, validators: list[ValidatorInterface]) -> bool:
        pass
