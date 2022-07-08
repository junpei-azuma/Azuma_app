from dataclasses import dataclass

@dataclass(frozen=True)
class UserId():
    """ユーザIDの値を保持するクラス

    Returns:
        _type_: UserId
    """    
    _value: str 
    
    def __init__(self, value: str) -> None:
        """オブジェクト初期化

        Args:
            value (str): IDの値
        """        
        object.__setattr__(self, "_value" , value)
    
    @property
    def value(self):
        """インスタンス変数を隠蔽

        Returns:
            _type_: IDの値
        """        
        return self._value
        
        
    