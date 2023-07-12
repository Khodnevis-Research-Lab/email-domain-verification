from .interfaces import ValidatorInterface
from .emails import Email


class EmailVerifier:
    validators: list[ValidatorInterface]
    email: Email

    def __init__(self, email: Email) -> None:
        self.email = email

    def verify(self, validators: list[ValidatorInterface]) -> bool:
        for validator in validators:
            try:
                validator.is_validator()
            except AttributeError as attr_error:
                raise Exception(
                    "Please Use ValidatorInterface As Parent Class For Your Validator"
                ).with_traceback(attr_error.__traceback__)

            validator.check(self.email)

        return True
