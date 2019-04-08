from contextlib import ContextDecorator, contextmanager

@contextmanager
def context():
    print('enter')
    yield 'hoho'
    print ('exit')


def generate():
    with context() as cm:
        res = 42
        print('CM instance: ', cm)
    return res


generate()