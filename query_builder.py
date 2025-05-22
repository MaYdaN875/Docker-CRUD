# query_builder.py

class SQLQueryBuilder:
    def __init__(self, table):
        self.table = table
        self.columns = "*"
        self.conditions = []
        self.order = ""

    def select(self, columns):
        if isinstance(columns, list):
            self.columns = ", ".join(columns)
        else:
            self.columns = columns
        return self

    def where(self, condition):
        self.conditions.append(condition)
        return self

    def order_by(self, column, direction="ASC"):
        self.order = f"ORDER BY {column} {direction}"
        return self

    def build(self):
        query = f"SELECT {self.columns} FROM {self.table}"
        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)
        if self.order:
            query += " " + self.order
        return query + ";"
