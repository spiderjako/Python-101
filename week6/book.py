import sys
import time
import pprint

def my_pretty_print(listy):
    for line in listy:
        print(line.replace('\n',''))

def reader(file_name):
    f = open(file_name, 'r')
    st = []
    first_line = True
    for line in f:
        if first_line:
            first_line = False
            st.append(line)
            continue
        if line[0] == '#':
            yield st
            my_pretty_print(st)
            while input('Press space to continue') != ' ':
                time.sleep(1)
            st = []
        st.append(line)
    f.close()

def main():
    list(reader(sys.argv[1]))


if __name__ == '__main__':
    main()