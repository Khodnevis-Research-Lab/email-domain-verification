import interfaces
import emails


class EmailVerifier:
    validators: list[interfaces.ValidatorInterface]
    email: emails.Email

    def __init__(self, email: emails.Email) -> None:
        self.email = email

    def verify(self, validators: list[interfaces.ValidatorInterface]) -> bool:
        for validator in validators:
            validator.check(self.email)

        return True
