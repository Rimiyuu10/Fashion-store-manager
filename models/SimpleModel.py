from datetime import datetime
from db import DbConnection


class SimpleModel:
    _table_name = None
    _properties = []

    def __init__(self):
        self.id = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.id}"

    def save(self):
        self.updated_at = datetime.now()
        if self.id is None:
            DbConnection.insert(self)
            self.id = DbConnection.last_insert_id()
        else:
            DbConnection.update(self)
        DbConnection.commit()

    def delete(self):
        if self.id is not None:
            DbConnection.delete(self)
            DbConnection.commit()

    @classmethod
    def fetch_all(cls, where: dict = None, like: dict = None, order_by: str = None, offset: int = None, limit: int = None) -> list:
        return DbConnection.fetch_all(cls, where, order_by, offset, limit, like)

    @classmethod
    def count(cls, where: dict = None, like: dict = None) -> int:
        return DbConnection.count(cls, where, like)
