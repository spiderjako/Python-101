def gas_stations(distance, tank_size, stations):
    shortest_list=[]
    i=0
    current_tank=tank_size
    current_station=0
    while i< len(stations):
        if current_tank-(stations[i]-current_station)<=0:
            shortest_list.append(stations[i-1])
            current_tank=tank_size
            current_station=stations[i-1]
            i-=1
        i+=1
    if i==len(stations):
            if current_tank-(distance-current_station)<=0:
                shortest_list.append(stations[i-1])
                i+=1
    return shortest_list

def is_number_balanced(number):
    i=0
    first_half=0
    second_half=0
    digit_size=len(str(number))
    is_Even=digit_size%2==0
    while number!=0:
        if is_Even:
            if len(str(number))>digit_size//2:
                second_half+=number%10
            elif len(str(number))<=digit_size//2:
                first_half+=number%10                
        else:
            if len(str(number))>digit_size//2+1:
                second_half+=number%10
            elif len(str(number))<=digit_size//2:
                first_half+=number%10
        number//=10
    if first_half==second_half:
        return True
    return False

def increasing_or_decreasing(seq):
    i = 0
    type=''
    countUp=0
    countDown=0
    while i<len(seq)-1:
        if seq[i]<seq[i+1]:
            countUp+=1
        elif seq[i]>seq[i+1]:
            countDown+=1
        i+=1
    if (countUp!=0 and countDown ==0):
        type='Up!'
    elif (countUp==0 and countDown!=0):
        type='Down!'
    else:
        return False
    return type

def sum_of_numbers(input_string):
    i=len(input_string)-1
    number=0
    power=0
    sum=0
    while i>=0:
        if input_string[i] in '1234567890':
            number+=int(input_string[i])*(10**power)
            power+=1
        else:
            sum+=number
            number=0
            power=0
        if i==0:
            sum+=number
        i-=1
    return sum

def numbers_to_message(pressed_sequence):
    keyboard ={
        '-1':[''],
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z'],
        '0': [' ']
    }
    pressed_key=''
    phrase=''
    i = 0
    count=0
    char=''
    is_One = 0
    while i<len(pressed_sequence)-1:
        i+=1
        pressed_key=str(pressed_sequence[i-1])
        if pressed_sequence[i-1]==pressed_sequence[i]:
            count+=1
        else:
            if pressed_key=='1':
                is_One=1
                continue
            place_in_keyboard=count%(len(keyboard[pressed_key]))
            char=keyboard[pressed_key][place_in_keyboard]
            if is_One:
                char=char.upper()
                is_One=0
            phrase+=char
            count=0
        # if i==len(pressed_sequence)-1:
        #     phrase+=char
    pressed_key=str(pressed_sequence[i])
    place_in_keyboard=count%(len(keyboard[pressed_key]))
    char=keyboard[pressed_key][place_in_keyboard]
    if is_One:
        char=char.upper()
    phrase+=char

    return phrase

stats = [70,90,140,210,240,280,350]
print(gas_stations(390,80, stats))
print(is_number_balanced(1238033))
print(increasing_or_decreasing([1,1,1,1]))
print(sum_of_numbers('ab12'))
print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))