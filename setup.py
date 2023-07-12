import textwrap
import setuptools

long_description = textwrap.dedent(
    """
# Email Domain Verification Package
this package can provide some email validators with which users can validate their project emails far easily

## Installation
<p>your module will be installed by PYPI</p>

```
pip install email-domain-verification
```

## Usage

```
from email_domain_verification import Email, EmailVerifier
from email_domain_verification.validators import BlackDomainListValidator

# you can import any of these validators or write your own validator
# (
#     BlackDomainListValidator,
#     DomainExtensionValidator,
#     LengthValidator,
#     MultiDotValidator,
#     SafeDomainValidator,
#     SafeDomainValidatorOnline,
# )

email = Email("hello@gmail.com")
black_email_list = [
    "xyz-mail.com",
    "tempmail.com",
    "temp.com",
    "mail-temp.org",
    # ...
]
validators = [
    BlackDomainListValidator(black_email_list),
]

verifier = EmailVerifier(email)
verifier.verify(validators)
```

### prevent raise exception

```
from email_domain_verification import Email, EmailVerifier
from email_domain_verification.validators import BlackDomainListValidator

email = Email("hello@gmail.com")
black_email_list = [
    "xyz-mail.com",
    "tempmail.com",
    # ...
]
validators = [
    BlackDomainListValidator(black_email_list),
]

verifier = EmailVerifier(email)
validated: bool = verifier.verify(validators, raise_exception=False)
# validated == True => email is safe | validated == False => email is unsafe
```


## Create Custom Validator

```
from email_domain_verification import Email, EmailVerifier
from email_domain_verification.interfaces import ValidatorInterface
from email_domain_verification.validators import LengthValidator


class CustomValidator(ValidatorInterface):
    __criterion: typing.Type

    def __init__(self, criterion: typing.Type) -> None:
        self.__criterion = criterion

    def validate_criterion(self) -> None:
        # validate __criterion
        pass

    def check(self, email: Email) -> bool:
        self.validate_criterion()

        # check email.value
        # example: len(email.value) > self.__criterion: return True
        validate = True
        if not validate:
            raise ValueError("The Error Message")

        return True


email = Email("hello@gmail.com")
validators = [
    BlackDomainListValidator(black_email_list),
    CustomValidator(10),
]

verifier = EmailVerifier(email)
verifier.verify(validators)


```

#### Copyright (c) 2023, Khodnevisai.com (Mahdi Niknejad).

"""
)

if __name__ == "__main__":
    setuptools.setup(
        name="email_domain_verification",
        version="1.0.2",
        description="Can Verify All The Email Forms And Domains",
        author="Mahdi Niknejad",
        author_email="mmahdiniknejad@gmail.com",
        url="https://github.com/khodnevis-app/development_tools",
        project_urls={
            "Documentation": "https://github.com/khodnevis-app/development_tools",
            "Source": "https://github.com/khodnevis-app/development_tools",
            "Tracker": "https://github.com/khodnevis-app/development_tools/issues",
        },
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=["email_domain_verification"],
        package_data={"email_domain_verification": ["py.typed", "*.pyi"]},
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Software Development",
        ],
        python_requires=">=3.10",
        install_requires=[
            "requests",
        ],
    )
