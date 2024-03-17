from model.secret_model import SecretModel

class SecretController:
    def __init__(self, model: SecretModel) -> None:
        self.model = model

    def validate_intput(self, input: str) -> bool:
        if input == self.model.secret_key[-2:]:
            return True

        return False

    def show_key_fragment(self) -> str:
        secret_key = self.model.secret_key
        return secret_key[:-2]
