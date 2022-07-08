from http.client import BAD_REQUEST
from flask import jsonify

class BadRequestException(Exception):
    """400番エラーハンドリング用クラス

    Args:
        Exception (_type_): _description_

    Returns:
        _type_: _description_
    """    
    @staticmethod
    def response(e):
        """エラーオブジェクトの値をレスポンスとして返す

        Args:
            e (_type_): エラーオブジェクト

        Returns:
            _type_: json
        """        
        return jsonify({
            'code' : BAD_REQUEST,
            'message': str(e.description)
        }), BAD_REQUEST