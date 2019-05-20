from controllers.main_controller import MainController

class MainMenu:

    @classmethod
    def show_options(cls,  current_user):
        OPTION_MENU = ("""
        1: Show members
        2: Available slots
        """)
        print(OPTION_MENU)
        option = input()
        
        

        if option == '1':
            members = MainController.show_members(current_user)
            cls._pretty_print_members(members)

    @classmethod
    def  _pretty_print_members(cls, members):
        if members is None:
            print('Nothing much happens, when there are no slots...')
            return
        for member in members:
            print('{status} {username}'.format(
                status=getattr(member, 'status', ''),
                username=member.username))