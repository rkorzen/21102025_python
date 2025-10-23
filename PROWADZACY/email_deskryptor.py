import re

EMAIL_PATTERN = re.compile(r"^[\w\.]+@\w+.\w+$")

class EmailField:
    def __init__(self, name: str):
        self.name = name

    def __set_name__(self, owner, name):
        self.priv_name = f"_{name}"
        self.public_name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not EMAIL_PATTERN.match(value):
            raise ValueError(f"Niepoprawny email w polu {self.name}")
        instance.__dict__[self.name] = value


class User:
    email = EmailField("email")

    def __init__(self, email):
        self.email = email

u = User("adam@example.com")
u.email = "xxx"