from httplib2 import Response


class PressureDto:
    """openweatherAPIから取得したjsonを
    ドメイン層で扱えるオブジェクトに加工する
    ※ オブジェクトからjsonへの加工は不要
    """
    @staticmethod
    def to_entity(response: Response) -> 