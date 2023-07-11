import typing
import emails
import interfaces
import utils
import random


class SafeDomainValidator(interfaces.ValidatorInterface):
    __criterion: typing.Iterable

    def __init__(self, criterion: typing.Iterable) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        if type(self.__criterion) not in (list, tuple):
            raise ValueError("Criterion Is Not Iterable")

    def check(self, email: emails.Email) -> bool:
        # self.validate_criterion()
        email_postfix = utils.EmailSplitter.find_email_postfix(email.value)
        if email_postfix not in self.__criterion:
            raise ValueError(
                "The Email Domain Is Not Accepted {}".format(email_postfix)
            )
        return True


class SafeDomainValidatorOnline(interfaces.ValidatorInterface):
    __tokens: typing.Iterable = None
    __token: str = None

    def __init__(self, tokens: typing.Iterable) -> None:
        self.__tokens = tokens

    def __init__(self, token: str) -> None:
        self.__token = token

    def validate_criterion(self) -> None:
        pass

    def check(self, email: emails.Email) -> bool:
        email_postfix = utils.EmailSplitter.find_email_postfix(email.value)
        if self.tokens:
            token = random.choice(self.__tokens)
        if self.token:
            token = self.__token

        verifier = utils.VerifyEmailOnline(email_postfix, token)
        verifier.verify(raise_exception=True)
        return True


class LengthValidator(interfaces.ValidatorInterface):
    __criterion: int

    def __init__(self, criterion: int = 5) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        if self.__criterion < 1:
            raise ValueError("Criterion Is Lower Than 1")

    def check(self, email: emails.Email) -> bool:
        self.validate_criterion()
        email_prefix = utils.EmailSplitter.find_email_prefix(email.value)
        if len(email_prefix) < self.__criterion:
            raise ValueError(
                "The Email Length Is Lower Than {}".format(self.__criterion)
            )

        return True


class MultiDotValidator(interfaces.ValidatorInterface):
    __criterion: int

    def __init__(self, criterion: int = 2) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        if self.__criterion < 1:
            raise ValueError("Criterion Is Lower Than 1")

    def check(self, email: emails.Email) -> bool:
        self.validate_criterion()
        email_postfix = utils.EmailSplitter.find_email_postfix(email.value)
        if email_postfix.count(".") >= self.__criterion:
            raise ValueError(
                "The Email Domain Has More than Than {} Dot '.' ".format(
                    self.__criterion
                )
            )

        return True


class BlackDomainListValidator(interfaces.ValidatorInterface):
    __criterion: typing.Iterable

    def __init__(self, criterion: typing.Iterable) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        if type(self.__criterion) not in (list, tuple):
            raise ValueError("Criterion Is Not Iterable")

    def check(self, email: emails.Email) -> bool:
        # self.validate_criterion()
        for domain in self.__criterion:
            if domain in email.value:
                raise ValueError(
                    "The Email Contains Blocked Domain '{}'".format(domain)
                )

        return True


class DomainExtensionValidator(interfaces.ValidatorInterface):
    __criterion: typing.Iterable

    def __init__(self, criterion: typing.Iterable) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        if type(self.__criterion) not in (list, tuple):
            raise ValueError("Criterion Is Not Iterable")

    def check(self, email: emails.Email) -> bool:
        # self.validate_criterion()
        for extension in self.__criterion:
            if extension in email.value:
                raise ValueError(
                    "The Email Contains Blocked Extension '{}'".format(extension)
                )

        return True