from re import I
from sqlalchemy import Column, ForeignKey, String
from app.configration.database.initdb import db
from app.password.password import Password
from app.password.hashedpassword import HashedPassword
from app.user.valueobject.userid import UserId

class PasswordDto(db.Model):
    """ドメインオブジェクトとリポジトリ間でデータを変換するクラス

    Args:
        Base (_type_): SQLAlchemy

    Returns:
        _type_: 
    """    
    __tablename__ = "passwords"
    user_id = db.Column(String, ForeignKey('users.id' , ondelete='CASCADE'), primary_key=True, unique=True)
    value = db.Column(String, nullable=False)
    
    
    ## Passwordクラスのエンティティを再構成使用とすると
    ## バリデーションに引っかかる
    def to_hashed_entity(self) -> HashedPassword:
        """ハッシュ化パスワードのエンティティに変換

        Returns:
            HashedPassword: ハッシュ化パスワードインスタンス
        """        
        return HashedPassword(
            UserId(self.user_id),
            self.value
        )
    
    @staticmethod
    def from_entity(password: Password) -> 'PasswordDto':
        """パスワードエンティティから変換

        Args:
            password (Password): パスワードエンティティ

        Returns:
            PasswordDto: DTOインスタンス
        """        
        return PasswordDto(
            user_id = password.user_id.value,
            value = password.value
        )