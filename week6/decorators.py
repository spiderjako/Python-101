import datetime
import time
import timeit
import functools

def accepts(typ):
    def accepter(func):
        def decorated(*args):
            for a in args:
                if not isinstance(a, typ):
                    raise TypeError(':Argument {} is not a {}'.format(args.index(a)+1,typ))
            return func(*args)

        return decorated
    return accepter

@accepts(int)
def say_my_name(name):
    return '{}'.format(name)

def encrypt(counter):
    def accepter(func):
        @functools.wraps(func)
        def decorated():
            sentence = func()
            sentence_2 = ''
            for i in sentence:
                if i ==' ':
                    sentence_2 += ' '
                    continue
                if (ord(i) + counter) > 122:
                    i = chr(ord(i)-26 + counter)
                else:
                    i = chr(ord(i) + counter)
                sentence_2 += i
            return sentence_2
        return decorated
    return accepter

def log(file_name):
    def accepter(func):
        @functools.wraps(func)
        def decorated():
            f = open(file_name, 'a')
            sentence = func.__name__
            print(sentence)
            f.write(sentence)
            f.write(' was called at ')
            f.write(str(datetime.datetime.now()))
            f.write('\n')

            f.close()
            return func()
        return decorated
    return accepter

def performance(file_name):
    def accepter(func):
        startTime = time.ctime()
        def decorator():
            return func()
        f = open(file_name, 'a')
        sentence = func.__name__
        f.write(sentence)
        f.write(' was called and took ')
        timeNow = time.ctime()
        print(startTime)
        print(timeNow)
        f.write(str(timeNow - startTime))
        f.write(' seconds to complete \n')
        f.close()
        return decorator
    return accepter

@performance('log.txt')
@log('log.txt')
@encrypt(5)
def get_string():
    return 'aloha'

@performance('log.txt')
def something():
    time.sleep(2)
    return 'Yes'

def main():
    print(get_string())
    print(something())

if __name__ == '__main__':
    main()