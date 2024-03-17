from re import X
import secrets


class SecretModel:
    def __init__(self):
        self._secret_key = ""
        self._set_secret_key()

    @property
    def secret_key(self) -> str:
        print(self._secret_key)
        return self._secret_key

    def _set_secret_key(self) -> None:
        self._secret_key = secrets.token_urlsafe(8)
