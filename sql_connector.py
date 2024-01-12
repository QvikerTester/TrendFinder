import mysql.connector

def connect_sql():
    global conn 
    conn = mysql.connector.connect(host='localhost', password='Duta1234.', user = 'root', database='TikTok')
    global cursor
    cursor = conn.cursor()
  
def insert_values_accounts(table_name, name):
    insert_query = f"INSERT INTO {table_name} (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    conn.commit()

def insert_multiple_columns(table_name, values):
    insert_query = f'''
        INSERT INTO tiktok.{table_name} (video_id, music_name, description, play_count)
        SELECT %s, %s, %s, %s
        FROM dual
        WHERE NOT EXISTS (SELECT 1 FROM tiktok.{table_name} WHERE video_id = %s)
    '''
    cursor.execute(insert_query, (*values, values[0]))
    conn.commit()

def get_all_user_names():
    get_users_query = "SELECT name FROM tiktok.accounts"
    cursor.execute(get_users_query)
    values_list = [row[0] for row in cursor.fetchall()]
    return values_list

def create_table_if_not_existed(user_name):
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {user_name} (
        video_id VARCHAR(255) PRIMARY KEY,
        music_name VARCHAR(255),
        description VARCHAR(255),
        play_count VARCHAR(255)
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

def delete_all_rows(user_name):
    delete_all_rows_query = f"DELETE FROM tiktok.{user_name};"
    cursor.execute(delete_all_rows_query)
    conn.commit()