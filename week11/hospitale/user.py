from database_layer.queries import Database

class User:
    db = Database()

    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self._status = status

    @classmethod
    def find(cls, username, password):
        result = cls.db.find_user(username, password)
        if result:
            print('Login succesful!')
            return cls(username, password, result[3])

    @classmethod
    def create_new_user(cls, username, password, new_status):
        if new_status.upper() == 'DOCTOR':
            title = input('Input your title:>')
            try:
                doctor = cls.db.create_doctor(title)
            except DatabaseConnectionError:
                sys.exit(1)
        if new_status.upper() == 'PATIENT':
            address = input('Input your address:>')
            status = input('Input your status:>')
            age = input('Tell us your age:>')
            unique_number = input('Tell us your unique 6 digit number:>')
            try:
                cls.db.create_patient(username, address, status, age, unique_number)
            except DatabaseConnectionError:
                sys.exit(1)
        cls.db.create_user(username, password, new_status)
        return cls(username, password, new_status)
    @property
    def status():
        return self._status

    @classmethod
    def show_patients(cls, username):
        return cls.db.show_patients_query(username)

    def is_doctor(self):
        if self._status == 'Doctor':
            return True
        return False