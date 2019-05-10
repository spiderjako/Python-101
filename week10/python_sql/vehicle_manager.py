import sqlite3

def create_table(table_name, table_info):
    conn = sqlite3.connect('vehicle_manager.db')
    curs = conn.cursor()
    curs.execute(f'DROP TABLE IF EXISTS {table_name}')
    curs.execute(f"""
        CREATE TABLE {table_name}{table_info}""")
    conn.commit()
    conn.close()

def main():
    user_cols = """(
        id INTEGER PRIVATE KEY NOT NULL,
        user_name VARCHAR(90),
        email VARCHAR(55),
        phone_number VARCHAR(15),
        address VARCHAR(100));"""
    client_cols = """(
        base_id INTEGER,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        );"""
    vehicle_cols = """(
        id INTEGER PRIVATE KEY NOT NULL,
        category VARCHAR(55),
        brand VARCHAR(55),
        model VARCHAR(55),
        register_number VARCHAR(15),
        transmission VARCHAR(20),
        owner INTEGER,
        FOREIGN KEY(owner) REFERENCES Client(base_id)
        );"""
    repair_cols = """(
        id INTEGER PRIVATE KEY NOT NULL,
        date VARCHAR(15),
        start_hour VARCHAR(15),
        vehicle INTEGER,
        bill REAL,
        mechanic_service INTEGER,
        FOREIGN KEY(vehicle) REFERENCES Vehicle(id),
        FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id)
        );"""
    mechanic_cols = """(
        base_id INTEGER,
        name VARCHAR(90),
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        );"""
    service_cols = """(
        id INTEGER PRIVATE KEY NOT NULL,
        title VARCHAR(90)
        );"""
    mechanicservice_cols = """(
        id INTEGER PRIVATE KEY NOT NULL,
        mechanic_id INTEGER,
        service_id INTEGER,
        FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id),
        FOREIGN KEY(service_id) REFERENCES Service(id)
        );"""
    create_table('BaseUser', user_cols)
    create_table('Client', client_cols)
    create_table('Mechanic', mechanic_cols)
    create_table('Service', service_cols)
    create_table('Vehicle', vehicle_cols)
    create_table('MechanicService', mechanicservice_cols)
    create_table('RepairHour',repair_cols)



    
if __name__=='__main__':
    main()