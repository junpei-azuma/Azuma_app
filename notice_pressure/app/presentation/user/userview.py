from http.client import BAD_REQUEST, OK
from flask import (request, abort, jsonify, Blueprint)
from cerberus import Validator
from app.presentation.shared.japaneseerrorhandler import JapaneseErrorHandler
from app.configration.dependency import Dependency
from app.user.usecase.createuser import CreateUser
from app.presentation.user.rule.create_rule import schema

class UserView():
    
    user = Blueprint('user' , __name__)
    
    @user.route('', methods=['POST'])
    def create():
        # パラメータ： メールアドレスとパラメータ(いずれも必須)
        param: dict = request.json
        
        # リクエストパラメータのチェック
        # 必須項目がない場合エラー
        # パラメータが文字列ではない場合エラー
        v = Validator(schema, error_handler = JapaneseErrorHandler)
        if not v.validate(param):
            return jsonify({
                'code' : BAD_REQUEST,
                'message' : v.errors
            }), BAD_REQUEST
        
        # ユースケースのインスタンス生成
        dependency: Dependency = Dependency()
        createuser: CreateUser = dependency.resolve(CreateUser)
        
        # ユースケース実行(try/exceptする)
        try:
            createuser.create_user(param)
        except ValueError as e:
            abort(BAD_REQUEST, description=e)
        
        return jsonify({
            'code' : OK,
            'message' : 'ユーザを仮登録しました。'
        }), OK