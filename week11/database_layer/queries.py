import sqlite3

class Database:
    def find_user(self, username, password):
        connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
        cursor = connect.cursor()
        tuple_to_be_checked = (username, password)
        cursor.execute("""
            SELECT * FROM User 
            WHERE ? == User.user_name AND ? == User.password;
        """, tuple_to_be_checked)
        row = cursor.fetchone()
        connect.commit()
        connect.close()
        if row != []:
            return row
        return False

    def create_user(self, username, password, status):
        connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
        cursor = connect.cursor()
        cursor.execute("""
            SELECT MAX(id) FROM User;
        """)
        get_id = cursor.fetchone()[0]
        if get_id is None:
            get_id = 1
        else:
            get_id += 1 

        to_be_added_in_User = (get_id, username, password, status)
        cursor.execute("""
            INSERT INTO User(id, user_name, password, status)
            VALUES(?,?,?,?);
        """, to_be_added_in_User)

        connect.commit()
        connect.close()

    def create_doctor(self, title):
        connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
        cursor = connect.cursor()
        cursor.execute("""
            SELECT MAX(id) FROM Doctor;
        """)
        get_id = cursor.fetchone()[0]
        if get_id is None:
            get_id = 1
        else:
            get_id += 1
        
        id_and_title_to_add = (get_id, title)
        cursor.execute("""
            INSERT INTO Doctor
            VALUES(?,?);
        """, id_and_title_to_add)

        connect.commit()
        connect.close()
        return True
    def create_patient(self, user_name, address, status, age, unique_number):
        connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
        cursor = connect.cursor()
        cursor.execute("""
            SELECT MAX(id_patient) FROM Patient;
        """)
        get_id = cursor.fetchone()[0]
        if get_id is None:
            get_id = 1
        else:
            get_id += 1
        
        id_and_title_to_add = (get_id, user_name, address, status, age, unique_number)
        cursor.execute("""
            INSERT INTO Patient
            VALUES(?,?,?,?,?,?);
        """, id_and_title_to_add)

        connect.commit()
        connect.close()
        return True
    
    def show_patients_query(self, username):
        connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
        cursor = connect.cursor()
        to_be_checked = (username,)
        print(to_be_checked)
        cursor.execute("""
            SELECT *
            FROM Patient INNER JOIN Reserved_slots ON Patient.id_patient == Reserved_slots.id_patient
            INNER JOIN Slots ON Reserved_slots.id_slot == Slots.id
            INNER JOIN Doctor ON Slots.id_doctor == Doctor.id
            INNER JOIN User ON User.id == Doctor.id
            WHERE ? == User.user_name;""", to_be_checked)

        connect.commit()
        connect.close()


    def show_doctors_query(username):
        connect = sqlite3.connect('/root/Python-101/week11/database_layer/hospital_manager.db')
        cursor = connect.cursor()
        # TODO CHANGE QUERY SO THAT IT FINDS THE PATIENT'S DOCTORS
        to_check = (username,)
        cursor.execute("""
            SELECT *
            FROM Patient INNER JOIN Reserved_slots ON Patient.id_patient == Reserved_slots.id_patient
            INNER JOIN Slots ON Reserved_slots.id_slot == Slots.id
            INNER JOIN Doctor ON Slots.id_doctor == Doctor.id
            INNER JOIN User ON User.id == Doctor.id
            WHERE ? == User.user_name;""")

        connect.commit()
        connect.close()