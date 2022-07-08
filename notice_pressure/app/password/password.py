from ast import Pass
from typing import ClassVar, Final
from app.user.valueobject.userid import UserId
import re


class Password():

    # 入力ルール：
    # 1. 使用できる文字： 数字・英語大文字小文字・記号(_@-%&#+)
    # 2. 上記の文字を最低1回使う
    # 3. 文字数制限： 10文字以上20文字以内
    __MIN_RENGTH:    Final[int] = 10
    __MAX_RENGTH:    Final[int] = 20
    __REGEX_PATTERN: Final[str] = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[_@\\-%&#+])[a-zA-z\\d_@\\-%&#+]{10,20}$"


    def __init__(self, user_id: UserId, value: str) -> None:
        """インスタンス生成

        Args:
            user_id (UserId): ユーザID
            value (str): パスワード文字列

        Raises:
            ValueError: 入力値エラー
        """
        if len(value) < self.__MIN_RENGTH:
            raise ValueError(f'パスワードは{self.__MIN_RENGTH}文字以上で入力してください。')
        
        if len(value) > self.__MAX_RENGTH:
            raise ValueError(f'パスワードは{self.__MAX_RENGTH}文字以下で入力してください。')
        
        if not re.fullmatch(self.__REGEX_PATTERN, value):
            raise ValueError("パスワードの形式が不正です。")

        self.__user_id: Final[UserId] = user_id
        self.__value: Final[str] = value

    @property
    def user_id(self) -> UserId:
        return self.__user_id

    @property
    def value(self) -> str:
        return self.__value
    
    def change(self, after_value) -> 'Password':
        """パスワードを変更する

        Args:
            after_value (_type_): 変更後の値

        Returns:
            Password: 変更後のPasswordインスタンス
        """
        changed_password: Password = Password(self.user_id, after_value)
        return changed_password
    
