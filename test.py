from email_domain_verification import Email, EmailVerifier
from email_domain_verification.validators import (
    BlackDomainListValidator,
    DomainExtensionValidator,
    LengthValidator,
    MultiDotValidator,
    SafeDomainValidator,
    SafeDomainValidatorOnline,
)

email = Email("mmahdi@yahoo.temp")
validators = (
    # BlackDomainListValidator(["gmail.com", "yahoo.com", "being.com"]),
    # DomainExtensionValidator([".xyz", ".temp"]),
    # LengthValidator(44),
    # MultiDotValidator(),
    # SafeDomainValidator(),
    # SafeDomainValidatorOnline,
)

verifier = EmailVerifier(email)
verifier.verify(validators)
