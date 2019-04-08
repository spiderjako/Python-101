import json
from pprint import pprint
def parse_json(file_name):
    f = open(file_name, 'r')
    array = json.load(f)
    for person in array['people']:
        programming_skill = ''
        for item in person['skills']:
            max = 0
            if item['level'] >= max:
                max = item['level']
                programming_skill = item['name']
        print(programming_skill + ' ' + person['first_name'] + ' ' + person['last_name'])

    
    f.close()





def main():
    parse_json('data.json')


if __name__ == '__main__':
    main()
