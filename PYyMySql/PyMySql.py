import pymysql

class Users:
    id = 0
    email = ''
    password = ''
    user_name = ''

    def __init__(self, id, email, password, user_name):
        self.id = id
        self.email = email
        self.password = password
        self.user_name = user_name

    def __str__(self) -> str:
        return f"{self.id} - {self.email} - {self.password} - {self.user_name}"

def open_connection():
    conn = pymysql.connect(
        host='localhost',  # Use 'localhost' instead of 'local'
        user='root',
        password='lingavani',
        db='user_schema'
    )
    return conn

def close_connection(conn):
    conn.close()

# Select query
def get_users():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    output = cur.fetchall()

    for i in output:
        print("select query output", i)

    close_connection(conn)

def get_user(users_id):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (users_id,))
    output = cur.fetchall()

    for i in output:
        print("select query output", i)

    close_connection(conn)

def insert_static_value():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (email, password, user_name) 
        VALUES (%s, %s, %s)
    """, ('test@test.com', 'password', 'test'))
    print(conn.insert_id())
    conn.commit()
    close_connection(conn)

def insert_dynamic_value(users_list):
    conn = open_connection()
    cur = conn.cursor()
    for user in users_list:
        cur.execute("""
            INSERT INTO users (email, password, user_name) 
            VALUES (%s, %s, %s)
        """, (user.email, user.password, user.user_name))
    print("----------->",conn.insert_id())
    conn.commit()
    close_connection(conn)

def delete_user(users_id):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (users_id,))
    conn.commit()
    close_connection(conn)

def update_user(user):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users SET email = %s, password = %s, user_name = %s WHERE id = %s
    """, (user.email, user.password, user.user_name, user.id))
    conn.commit()
    close_connection(conn)

# Test the functions

get_users()
get_user('1')

users1 = Users(5, 'sandeep@test.com', 'password', 'test')
print("users", users1)
users_list = [users1]
insert_dynamic_value(users_list)
get_user('2')  # Assuming the newly inserted user gets id 2, adjust accordingly

update_user_data = Users(3334, 'update@gmail.com', 'new', 'testt')
update_user(update_user_data)
get_user('2')

delete_user('2')
get_users()
