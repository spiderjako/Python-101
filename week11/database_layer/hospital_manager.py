import sqlite3


def create_table(table_name, table_info):
    conn = sqlite3.connect('hospital_manager.db')
    curs = conn.cursor()
    curs.execute(f'CREATE TABLE IF NOT EXISTS {table_name}{table_info}')
    conn.commit()
    conn.close()

def create_hospital():
    user_cols = """(
        id INTEGER PRIMARY KEY NOT NULL,
        user_name VARCHAR(55),
        password VARCHAR(55),
        status VARCHAR(20),
        full_name VARCHAR(90)
        );"""
    doctor_cols = """(
        id INTEGER, title VARCHAR(55),
        FOREIGN KEY(id) REFERENCES User(id)
        );"""
    patient_cols = """(
        id_patient INTEGER,
        user_name INTEGER,
        address VARCHAR(100),
        status VARCHAR(20),
        age INTEGER,
        unique_number INTEGER,
        FOREIGN KEY(id_patient) REFERENCES User(id)
        );"""
    reserved_slots_cols = """(
        id_patient INTEGER,
        id_slot INTEGER,
        status VARCHAR(20),
        FOREIGN KEY(id_patient) REFERENCES Patient(id_patient)
    );"""
    slots_cols = """(
        id INTEGER,
        id_doctor INTEGER,
        end_hour VARCHAR(10),
        date VARCHAR(10),
        status VARCHAR(20),
        room INTEGER,
        FOREIGN KEY(id) REFERENCES Reserved_slots(id_slot),
        FOREIGN KEY(id_doctor) REFERENCES Doctor(id)
    );"""

    create_table('User', user_cols)
    create_table('Doctor', doctor_cols)
    create_table('Patient', patient_cols)
    create_table('Reserved_slots', reserved_slots_cols)
    create_table('Slots', slots_cols)
def main():
    create_hospital()

if __name__ == '__main__':
    main()