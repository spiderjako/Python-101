def is_credit_card_valid(number):
    number_string = str(number)
    if len(number_string)%2 == 0:
        return False
    summ = 0
    for i in range(len(number_string)-1, 0 - 1, -1):
        if i % 2 == 0:
            print(number_string[i])
            summ += int(number_string[i])
        else:
            summ += 2*int(number_string[i])
            print(2*int(number_string[i]))
    print(summ)
    if summ % 10 == 0:
        return True
    else:
        return False

print(is_credit_card_valid(79927398713))
