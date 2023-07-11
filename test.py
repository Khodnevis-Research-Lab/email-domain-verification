from email_domain_verification import Email, EmailVerifier
from email_domain_verification.validators import (
    BlackDomainListValidator,
    DomainExtensionValidator,
    LengthValidator,
    MultiDotValidator,
    SafeDomainValidator,
    SafeDomainValidatorOnline,
)

email = Email("mmahdiniknejad@gmail.com")
validators = (
    BlackDomainListValidator(["temp.com"]),
    DomainExtensionValidator(".xyz"),
    LengthValidator(10),
    MultiDotValidator(3),
    # SafeDomainValidator(),
    # SafeDomainValidatorOnline,
)

verifier = EmailVerifier(email)
verifier.verify(validators)
