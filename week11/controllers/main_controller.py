import re

from hospitale.user import User

class MainController:
    @classmethod
    def sign_in(cls, username, password):
        # cls._validate_password(password)
        # password = cls._hash_password(password)
        current_user = User.find(username, password)
        return current_user

    @classmethod
    def sign_up(cls, username, password, second_password, status):
        if password == second_password:
            cls._validate_password(password)
        else:
            print('Passwords do not match')
            sys.exit(1)
        #hashed_pass1 = cls._hash_password(password)
        #hashed_pass2 = cls._hash_password(second_password)
        
        if User.find(username, password):
            raise UserAlreadyExistsError

        return User.create_new_user(username, password, status)

    @classmethod
    def show_members(cls, current_user):
        if current_user.is_doctor:
            return current_user.show_patients(current_user.username)
        else:
            return current_user.show_doctors()

    @classmethod
    def _validate_password(cls, password):
        while True:
            if len(password)<8:
                print('Make sure that your password is at least 8 characters long!\n')
            elif re.search('[0-9]', password) is None:
                print('Make sure that your password has at least one digit in it!\n')
            elif re.search('[A-Z]', password) is None:
                print('Make sure that your password has at least one capital letter in it!\n')
            else:
                break
            password = input('Enter password:>')

    @classmethod
    def show_doctors(cls, current_user):
        pass