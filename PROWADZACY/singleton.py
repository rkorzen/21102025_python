class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, *kwargs)
        return cls._instance

    def log(self, message):
        print(f"[LOG] {message}")

    def __str__(self):
        return str(id(self))

logger1 = Logger()
logger2 = Logger()


print(logger1)
print(logger2)

