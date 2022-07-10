from datetime import date, datetime
from typing import ClassVar, Final, Type



class Pressure():
    
    # 観測史上の日本海面気圧最低値(更新されたら変更する)
    __MIN_VALUE: ClassVar[int] = 967
    # 観測史上の日本海面気圧最高値(更新されたら変更する)
    __MAX_VALUE: ClassVar[int] = 1039
    
    def __init__(self, target_datetime: datetime, value: int) -> None:
        """インスタンス初期化。 日時で気圧データは一意のため、IDは不要

        Args:
            target_datetime (datetime): 日時()
            value (int): 気圧の値


        Raises:
            ValueError: 値が観測史上最低値を下回っている場合
            ValueError: 値が観測史上最大値を上回っている場合
        """        
        if value < self.__MIN_VALUE:
            raise ValueError("気圧の値が観測史上最低値未満です。")
        
        if value > self.__MAX_VALUE:
            raise ValueError("気圧の値が観測史上最高値を超過しています。")
        
        self.__datetime: Final[datetime] = target_datetime
        self.__value: Final[int] = value
        
    
    @property
    def datetime(self) -> datetime:
        return self.__datetime
    
    @property
    def value(self) -> int:
        return self.__value