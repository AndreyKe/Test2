import secrets


class Model:

    def __init__(self):
        self.label = input("Label to replace: ")  # Перемещено в начало
        self._secret_key = ""
        self._set_secret_key()

    def get_secret_key(self):
        return self._secret_key

    def _set_secret_key(self):
        self._secret_key = secrets.token_urlsafe(8)


if __name__ == "__main__":
    m = Model()
    res = m.get_secret_key()

    print(m.label)  # Доступ к label после инициализации
    print(res)
