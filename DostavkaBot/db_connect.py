import sqlite3


def create_id(message_id):
    connect = sqlite3.connect('message_id.db')
    cursor = connect.cursor()

    query = """"""

    cursor.execute(f"""INSERT INTO msg_id (id)
    VALUES({message_id})""")
    connect.commit()
    connect.close()



