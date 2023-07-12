from email_domain_verification import Email, EmailVerifier
from email_domain_verification.interfaces import ValidatorInterface
from email_domain_verification.validators import (
    BlackDomainListValidator,
    DomainExtensionValidator,
    LengthValidator,
    MultiDotValidator,
    SafeDomainValidator,
    SafeDomainValidatorOnline,
)


class CustomValidator:
    __criterion: int

    def __init__(self, criterion: int = 5) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        if self.__criterion < 1:
            raise ValueError("Criterion Is Lower Than 1")

    def check(self, email: Email) -> bool:
        return True


email = Email("mmahdi@google.com")
validators = (
    # BlackDomainListValidator(["gmail.com", "yahoo.com", "being.com"]),
    # DomainExtensionValidator([".xyz", ".temp"]),
    # LengthValidator(44),
    # MultiDotValidator(),
    # SafeDomainValidator(["google.com", "yahoo.com"]),
    # SafeDomainValidatorOnline(token="582ade864dd84a61abecc4fc18f61993"),
    CustomValidator(),
)

verifier = EmailVerifier(email)
verifier.verify(validators)
