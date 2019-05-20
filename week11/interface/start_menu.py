import sys

from controllers.main_controller import MainController
from interface.main_menu import MainMenu

class StartMenu:
    # sign in & sign up
    # redirect to Main Menu
    @classmethod
    def run(cls):
        print('Welcome to the Hospital!')
        options = """
            'Do you want to sign in or sign up?
            1 - sign in
            2 - sign up
            3 - exit
        """
        print(options)
        start_option = input()
        # TODO check if the num is ok
        username = input('Username:> ')
        password = input('Password:> ')
        if start_option == '1':
            # TODO hide password
            is_signed = MainController.sign_in(username, password)
            if is_signed:
                MainMenu.show_options(is_signed)
            else:
                print('Wrong username or password!')
                sys.exit(1)
        elif start_option == '2':
            #TODO hide pass
            second_password = input('Second password:> ')
            status = input('Are you a Patient or a Doctor?> ')
            
            try:
                current_user = MainController.sign_up(username, password, second_password, status)
            except UserAlreadyExists:
                print('Sign up failed! User already exists')
                sys.exit(1)
            except DatabaseConnectionError:
                print('Sign up failed! Server error! Try again!')
                sys.exit(1)
            except PasswordsDontMatchError:
                print('Sign up failed! Passwords do not match!')
                sys.exit(1)
            
            MainMenu.show_options(current_user)
        else:
            sys.exit(1)