import abc
import emails as emails
from typing import Type, TypeVar


T = TypeVar("T")


class ValidatorInterface(abc.ABC):
    __criterion: Type[T]

    @abc.abstractmethod
    def validate_criterion(self) -> None:
        pass

    @abc.abstractmethod
    def check(self, email: emails.Email) -> bool:
        pass


class VerificationInterface(abc.ABC):
    @abc.abstractmethod
    def validation(self, validators: list[ValidatorInterface]) -> bool:
        pass
