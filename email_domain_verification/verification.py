from .interfaces import ValidatorInterface
from .emails import Email


class EmailVerifier:
    validators: list[ValidatorInterface]
    email: Email

    def __init__(self, email: Email) -> None:
        self.email = email

    def verify(self, validators: list[ValidatorInterface]) -> bool:
        for validator in validators:
            validator.check(self.email)

        return True
