from http.client import INTERNAL_SERVER_ERROR
from flask import jsonify

class InternalServerErrorException(Exception):
    """内部エラーのハンドラー

    Args:
        Exception (_type_): 例外基底クラス

    Returns:
        _type_: エラーレスポンス
    """    
    @staticmethod
    def response(e):
        """エラーレスポンスを返す

        Args:
            e (_type_): エラーオブジェクト

        Returns:
            _type_: レスポンスのjson
        """        
        return jsonify({
            'code' : INTERNAL_SERVER_ERROR,
            'msg': e.description
        }), INTERNAL_SERVER_ERROR