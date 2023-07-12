import requests
import json


class EmailSplitter:
    @classmethod
    def find_email_prefix(cls, email_value: str):
        return email_value.split("@")[0]

    @classmethod
    def find_email_postfix(cls, email_value: str):
        return email_value.split("@")[1]


class VerifyEmailOnline:
    __domain: str
    __token: str

    def __init__(self, domain: str, token: str) -> None:
        self.__domain = domain
        self.__token = token
        self.__verifymail = (
            f"https://verifymail.io/api/{self.__domain}?key={self.__token}"
        )

    def verify(self, raise_exception=False):
        response = requests.get(self.__verifymail)
        data = json.loads(response.content.decode())
        if data.get("disposable", True) == False:
            return True

        if raise_exception:
            raise ValueError("The Domain Is Unsafe")

        return False
