import sys
import os
from random import randint

def cat(some_file):
    f = open(some_file, 'r')
    print(f.readlines())
    f.close()
    return

def cat2(random_arguments):
    for i in range(len(random_arguments)):
        if i!=0:
            f = open(random_arguments[i], 'r')
            print(f.readlines())
            f.close
            if i<len(random_arguments)-1:
                print()
    return

def generate_numbers(filename, numbers):
    f = open(filename,'w')
    for i in range(int(numbers)):
        f.write(str(randint(1,1000)))
        if i<int(numbers)-1:
            f.write(' ')
    f.close()
    return

def sum_numbers(filename):
    f = open(filename, 'r')
    numbers = f.readlines()
    list_numbers = list(numbers[0].split(' '))
    sum=0
    for item in list_numbers:
        sum+=int(item)
    f.close()
    return sum

def main():
    file = sys.argv
    generate_numbers(file[1],file[2])
    cat(file[1])
    print(sum_numbers(file[1]))

if __name__ == '__main__':
    main()