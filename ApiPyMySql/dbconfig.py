import pymysql


class dbconfig:

    @staticmethod
    def open_connection():
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="lingavani",
            db='user_schema',
        )
        return conn

    @staticmethod
    def close_connection(conn):
        conn.close()