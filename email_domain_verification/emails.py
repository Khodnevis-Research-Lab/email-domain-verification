class Email:
    __email: str

    def __init__(self, email: str) -> None:
        self.__email = email

    @property
    def value(self) -> str:
        return self.__email

    @value.setter
    def value(self, email: str) -> None:
        self.__email = email
