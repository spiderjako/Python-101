import sqlite3

connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
cursor = connect.cursor()

cursor.execute("""
        SELECT MAX(id) FROM Doctor;
    """)
get_id = cursor.fetchone()[0]
if get_id is None:
    get_id = 1
print(get_id)

connect.commit()
connect.close()