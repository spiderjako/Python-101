import sqlite3

def create_table(database):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute('CREATE TABLE user (id INTEGER PRIMARY KEY NOT NULL, full_name VARCHAR(100) NOT NULL, email VARCHAR(55) NOT NULL, age INTEGER NOT NULL, phone VARCHAR(15) NOT NULL, additional_info TEXT);')
    conn.commit()
    conn.close()

def add():
    conn = sqlite3.connect('business.db')
    curs = conn.cursor()
    id = input('Insert the ID: ')
    full_name = input('Insert the Full Name: ')
    email = input('Insert the email: ')
    age = input('Insert your age: ')
    phone = input('Insert your phone number: ')    
    add_info = input('Insert additional info (optional):')
    values_to_be_added=(id,full_name,email,age,phone,add_info)
    curs.execute('INSERT INTO user(id, full_name, email, age,phone,additional_info) VALUES(?,?,?,?,?,?)', values_to_be_added)
    conn.commit()
    conn.close()

def list():
    conn = sqlite3.connect('business.db')
    curs = conn.cursor()

    for row in curs.execute('SELECT * FROM user;'):
        print('ID:{}, FULL NAME: {}, EMAIL:{}, AGE:{}, PHONE:{}, ADDITIONAL_INFO:{}'.format(row[0],row[1],row[2],row[3],row[4],row[5]))

    conn.commit()
    conn.close()

def get():
    conn = sqlite3.connect('business.db')
    curs = conn.cursor()
    getting_id = (input('Type in the ID of the Client, whose Info you want to get: '),)

    curs.execute('SELECT * FROM user WHERE id==?',getting_id)
    row = curs.fetchone()
    print('ID:' + str(row[0]))
    print('FULL NAME:' + str(row[1]))
    print('EMAIL:'+str(row[2]))
    print('AGE:' + str(row[3]))
    print('PHONE:' + str(row[4]))
    print('ADDITIONAL_INFO:' + str(row[5]))
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('business.db')
    curs = conn.cursor()
    contact_to_be_deleted = (input('Input the ID of the To-Be-Deleted Client: '),)
    curs.execute('DELETE FROM user WHERE id == ?', contact_to_be_deleted)

    conn.commit()
    conn.close()


def main():
    print('Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)')
    command = input('Enter what you want to do:')
    while command != 'exit':
        if command == 'add':
            add()
        elif command == 'list':
            list()
        elif command == 'get':
            get()
        elif command == 'delete':
            delete()
        elif command == 'help':
            print('1. `add` - insert new business card \n2. `list` - list all business cards \n3. `delete` - delete a certain business card (`ID` is required) \n4. `get` - display full information for a certain business card (`ID` is required)\n5. `help` - list all available options)')
        command = input('Enter what else you want to do:')
if __name__ == '__main__':
    main()
