def chain(iterable_one, iterable_two):
    for i in iterable_one:
        yield i
    for j in iterable_two:
        yield j

def compress(iterable, mask):
    for i, bo in zip(iterable, mask):
        if bo:
            yield i

def cycle(iterable):
    i = 0
    boly = True
    while boly:
        yield iterable[i]
        iterable.append(iterable[i])
        i += 1



def main():
    for x in cycle([1,2,3]):
        print(x)
    
if __name__ == '__main__':
    main()