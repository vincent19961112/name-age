from __future__ import annotations


class User(object):

    # 物件基礎建構式
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # source的欄位係以 資料庫欄位做為預設命名

    @staticmethod
    def from_dict(source: dict) -> User:
        user = User(
            name=source.get(u'name'),
            age=source.get(u'age'),
        )

        return user

    def to_dict(self):
        user_dict = {
            "name": self.name,
            "age": self.age,
        }
        return user_dict
