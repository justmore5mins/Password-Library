class NoPassWordError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class EncryptionError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)