from http.client import NOT_FOUND
from typing import ClassVar
from flask import jsonify

class NotFoundException(Exception):
    """404エラーのハンドラー

    Args:
        Exception (_type_): 例外基底クラス

    Returns:
        _type_: エラーレスポンス
    """    
    __FLASK_DEFAULT_MSG: ClassVar[str] = "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    __CUSTOM_DEFAULT_MSG: ClassVar[str] = "指定したリソースが見つかりません。"
    
    @classmethod
    def response(cls, e):
        """エラーレスポンスを返す

        Args:
            e (_type_): エラーオブジェクト

        Returns:
            _type_: レスポンスのjson
        """        
        if str(e.description) == cls.__FLASK_DEFAULT_MSG:
            e.description = cls.__CUSTOM_DEFAULT_MSG
            
        return jsonify({
            'code' : NOT_FOUND,
            'message': e.description
        }), NOT_FOUND