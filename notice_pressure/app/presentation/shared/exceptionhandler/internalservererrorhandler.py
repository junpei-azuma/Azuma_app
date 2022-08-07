from http.client import INTERNAL_SERVER_ERROR
import os
import traceback
from flask import jsonify, current_app


class InternalServerErrorHandler(Exception):
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
        return (
            jsonify({"code": INTERNAL_SERVER_ERROR, "msg": e.description["message"]}),
            INTERNAL_SERVER_ERROR,
        )

    @staticmethod
    def handle(e):
        # エラー内容を通知する。
        print(traceback.format_exc())
        # エラーをログに出力する

        # レスポンスを返す

        return (
            jsonify({"code": INTERNAL_SERVER_ERROR, "msg": "内部エラーが発生しました。"}),
            INTERNAL_SERVER_ERROR,
        )
