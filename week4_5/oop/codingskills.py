import json

def parse_json(file_name):
    f = open(file_name, 'r')
    array = json.loads(f)
    print(array)


    f.close()





def main():
    parse_json('data.json')


if __name__ == '__main__':
    main()
