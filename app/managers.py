import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema_db.db")
        self.table_name = "actors"

    def create_table(self) -> None:
        self._connection.execute(
            f"CREATE TABLE IF NOT EXISTS '{self.table_name}' ("
            "id INTEGER PRIMARY KEY,"
            "first_name TEXT,"
            "last_name TEXT)"
        )
        self._connection.commit()

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) "
            "VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_cursor]

    def update(self,
               id_update: int,
               new_first_name: str,
               new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, id_update)
        )
        self._connection.commit()

    def delete(self, id_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_delete,)
        )
        self._connection.commit()