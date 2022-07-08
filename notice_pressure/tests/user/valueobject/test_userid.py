from time import sleep
from tests.util.factory import create_userid
from app.user.valueobject.userid import UserId

def test_UserID生成インスタンス生成_正常系():
    # 事前条件： なし
    
    # 操作： UserIDインスタンス生成
    userid: UserId = create_userid()
    
    # 想定結果： 1. 正常にインスタンスが生成されている
    assert isinstance(userid, UserId)
    
    # 2. IDの値が正常
    assert isinstance(userid.value , str)

def test_UserIDが一意である():
    # 事前条件：UserIdインスタンスを1つ生成
    userid_1: UserId = create_userid()
    
    # 操作： 別のUserIdインスタンスを1つ生成
    userid_2: UserId = create_userid()
    
    # 想定結果： 2つのIDの値が一致しない(※ インスタンス同士を比較しないように注意)
    assert userid_1.value != userid_2.value

def test_UserIDは生成順にソートされる():
    # 事前条件：UserIdインスタンスを1つ生成後、sleep
    userid_1: UserId = create_userid()
    sleep(0.01)
    # 操作： 別のUserIdインスタンスを1つ生成
    userid_2: UserId = create_userid()
    
    # 想定結果： 後から作られたIDの方が大きい
    assert userid_1.value < userid_2.value