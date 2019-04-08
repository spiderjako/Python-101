import sys
import time
from datetime import datetime
from contextlib import contextmanager

# @contextmanager
# def performance(file_name):
#     opened_file = open(file_name, 'w')
#     start_time = time.clock()
#     try:
#         yield 
#     end_time = time.clock()
#     opened_file.close()

# class Performance:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.opened_file = None
#     def __enter__(self):
#         self.start_time = datetime.now()
#         self.opened_file = open(self.file_name, 'w')
#         return self
#     def __exit__(self, *args):
#         end_time = datetime.now()
#         self.opened_file.write(str(end_time - self.start_time))
#         self.opened_file.close()
@contextmanager
def assertRaises(exception, msg = None):
    try:
        yield
        raise Exception('Not found')
    except exception as exc:
        if type(exc) == exception:
            if message is not None and message == str(exc):
                return True
            else:
                raise Exception('Message is wrong')
            raise Exception('Found but not the same')

def huhu(num1, num2):
    if num1<0 and num2 <0:
        raise ValueError
    return num1+num2

def main():
    # p = sys.argv
    # with Performance(p[1]) as f:
    #     time.sleep(5)

    with assertRaises('ZeroDivisonError'):
        huhu(-1,-2)


if __name__ == '__main__':
    main()