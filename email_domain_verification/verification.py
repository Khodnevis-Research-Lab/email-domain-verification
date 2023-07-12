from .interfaces import ValidatorInterface
from .emails import Email


class EmailVerifier:
    validators: list[ValidatorInterface]
    email: Email

    def __init__(self, email: Email) -> None:
        self.email = email

    def verify(
        self, validators: list[ValidatorInterface], raise_exception=True
    ) -> bool:
        for validator in validators:
            try:
                validator.is_validator()
            except AttributeError as attr_error:
                raise Exception(
                    "Please Use ValidatorInterface As Parent Class For Your Validator"
                ).with_traceback(attr_error.__traceback__)

            try:
                validator.check(self.email)
            except ValueError as value_error:
                if raise_exception:
                    raise value_error

                return False

        return True
