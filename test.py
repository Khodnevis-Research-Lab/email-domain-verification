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


email = Email("hello@gmail.com")
validators = (
    # BlackDomainListValidator(["gmail.com", "yahoo.com", "being.com"]),
    # DomainExtensionValidator([".xyz", ".temp"]),
    # LengthValidator(44),
    # MultiDotValidator(),
    # SafeDomainValidator(["google.com", "yahoo.com"]),
    # SafeDomainValidatorOnline(token="582ade864dd84a61abecc4fc18f61993"),
)

verifier = EmailVerifier(email)
verifier.verify(validators)
