import sys

def cat(some_file):
    f = open(some_file, 'r')
    print(f.readlines())
    f.close()
    return

def list_user_data(all_user_data):
    f = open(all_user_data, 'r')
    cat(all_user_data)
    f.close()
    return
def show_user_incomes(all_user_data):
    


def show_user_savings(all_user_data):
    pass


def show_user_deposits(all_user_data):
    pass


def show_user_expenses(all_user_data):
    pass


def list_user_expenses_ordered_by_categories(all_user_data):
    pass


def show_user_data_per_date(date, all_user_data):
    pass


def list_income_categories(all_user_data):
    pass


def list_expense_categories(all_user_data):
    pass


def add_income(income_category, money, date, all_user_data):
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass



def main():
    things = sys.argv
    list_user_data(things)
    cat()

if __name__ == '__main__':
    main()
