from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(frozen=True)
class Email():
    """ユーザのメールアドレスを保持する

    Returns:
        _type_: Email
    """    
    _value: str
    # とりあえずHTMLのinput type=email の入力規則に合わせます。
    __REGEX_PATTERN: ClassVar[str] = "^[a-zA-Z0-9.!#$%&'*+ \\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    __EMPTY_ERROR: ClassVar[str] = "メールアドレスを入力してください。"
    __TYPE_ERROR: ClassVar[str] = "メールアドレスを正しく入力してください。"
    __INVALID_VALUE_ERROR: ClassVar[str] = "メールアドレスが不正な形式です。"
    
    def __init__(self, value: str) -> None:
        """インスタンス初期化

        Args:
            value (str): メールアドレスの値
        """       
        if not value:
            raise ValueError(self.__EMPTY_ERROR)
        
        if not isinstance(value, str):
            raise ValueError(self.__TYPE_ERROR)
        
        if not re.fullmatch(self.__REGEX_PATTERN, value):
            raise ValueError(self.__INVALID_VALUE_ERROR)
        
        object.__setattr__(self, "_value" , value)
        
    
    @property
    def value(self) -> str:
        """変数を隠蔽する

        Returns:
            str: メールアドレスの値
        """        
        return self._value
    
    def is_valid_pattern(self, value: str) -> bool:
        """不正な形式をチェック

        Args:
            value (str): 入力値

        Returns:
            bool: 形式が不正か
        """        
        if re.fullmatch(self.__REGEX_PATTERN, value):
            return True
        else:
            return False