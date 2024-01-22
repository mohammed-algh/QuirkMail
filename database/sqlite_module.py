import sqlite3

class SQLiteModule:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, columns))
        self.conn.commit()

    def insert(self, table_name, columns, values):
        query = "INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, values)
        self.cursor.execute(query)
        self.conn.commit()

    def select(self, table_name, columns, where=None):
        if where:
            query = "SELECT {} FROM {} WHERE {}".format(columns, table_name, where)
        else:
            query = "SELECT {} FROM {}".format(columns, table_name)
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update(self, table_name, columns, where=None):
        if where:
            query = "UPDATE {} SET {} WHERE {}".format(table_name, columns, where)
        else:
            query = "UPDATE {} SET {}".format(table_name, columns)
        self.cursor.execute(query)
        self.conn.commit()

    def delete(self, table_name, where=None):
        if where:
            query = "DELETE FROM {} WHERE {}".format(table_name, where)
        else:
            query = "DELETE FROM {}".format(table_name)
        self.cursor.execute(query)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    
    def close(self):
        self.conn.close()
