def sum_of_digits(n):
    n = abs(n)
    digits = [int(ch) for ch in str(n)]
    return sum(digits)

def to_digits(n):
    a = []
    while n!=0:
        a.append(n%10)
        n=n//10
    return sorted(a)

def to_number(digits):
    size = len(digits)-1
    number = 0
    i=0
    while size>=0:
        number += digits[i] * (10 ** size)
        size-=1
        i+=1
    return number

def fact(n):
    if n == 1:
        return 1
    return n*fact_digits(n-1)

def fact_digits(n):
    sum = 0
    while n!=0:
        digit = n%10
        sum+= fact(digit)
        n=n//10
    return sum

def reverse_string(string):
    result = ''
    n = len(string)

    for i in range(n):
        result += string[n - i - 1]

    return result

def palindrome(n):
    m = str(n)
    if m!=reverse_string(m):
        return False
    return True

def count_vowels(st):
    i=0
    count=0
    while i<len(st):
        if st[i] in 'aoueiyAOUEIY':
            count+=1
        i+=1
    return count

def count_consonants(st):
    i=0
    count=0
    while i<len(st):
        if st[i] in 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ':
            count+=1
        i+=1
    return count

def char_histogram(st):
    i = 0
    dict = {}
    for ch in st:
        if ch in dict:
            dict[ch]+=1
        else:
            dict[ch]=1

    return dict

def sum_matrix(matrix):
    sumMatrix = 0
    for x in matrix:
        sumMatrix+=sum(x)
    return sumMatrix

# def nan_expand(n):
#     nany = ''
#     if n == 0:
#         return nany
#     while n>0:
#         nany+='Not a '
#         n-=1
#     nany+='NaN'
#     return nany

def nan_expand(n):
    nany = ''
    if n == 0:
        return nany
    while n>0:
        nany+='Not a '
        n-=1
    nany+='NaN'
    return nany

def char_2(string):
    result={}

    for ch in string:

        result[ch]=result.get(ch,0)+1
    return result

def prime_factorization(n):
    i=2
    list_of_factors = []
    while i<=n:
        count=0
        while n%i==0:
            n = n//i
            count+=1
        if count!=0:
            tuply = (i,count)
            list_of_factors.append(tuply)
        i+=1
    return list_of_factors

def max_consecutive(items):
    i=0
    max_count=0
    count=1
    while i<len(items)-1:
        if items[i]==items[i+1]:
            count+=1
            if count>=max_count:
                max_count=count
        else:
            count=1
        i+=1
    return max_count

def word_counter(word,rows,cols, table):
    i=0
    j=0
    count=0
    proto_word=''
    while i<rows:
        while j<cols:
            proto_word.append(table[i][j])
            if proto_word==word:
                count+=1
                proto_word=''
            j+=1
        j=0
        while j<rows:
            ##proto_word.append(table[i][j])
            if proto_word==word:
                count+=1
                proto_word=''
            i+=1

def main():
    m = [[1,2,3],[4,5,6],[7,8,9]]
    num = 1000
    list1= [1,2,3,3,3,3,4,5,5,5,5,5]
    print(sum_of_digits(num))
    print(to_digits(num))
    print(to_number(list1))
    print(fact_digits(3))
    print(fact_digits(999))
    print(palindrome(123))
    print(count_consonants('Github is the second best thing that happend to programmers, after the keyboard!'))
    print(char_histogram('Python'))
    print(sum_matrix(m))
    print(nan_expand(2))
    print(char_2('baba'))
    print(prime_factorization(num))
    print(max_consecutive(list1))
if __name__ == "__main__":
    main()