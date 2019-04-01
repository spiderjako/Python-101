from fractions import Fraction

def simplify_fraction(fraction: tuple):
    if not isinstance(fraction, tuple):
        raise Exception('ValidationError')

    nominator = fraction[0]
    denominator = fraction[1]
    i = 2
    while i != denominator+1:
        if denominator%i == 0 and nominator%i == 0:
            nominator /= i
            denominator /= i
            i = 2
        else:
            i+=1
    return (int(nominator),int(denominator))

def collect_fractions(fractions):
    final_denominator = 1
    final_nominator = 0
    summ = 0
    for x in fractions:
        final_denominator *= x[1]
    
    for x in fractions:
        final_nominator += x[0]*final_denominator/x[1] 

    tuple_to_be_transformed = (final_nominator, final_denominator)
    return simplify_fraction(tuple_to_be_transformed)

def sort_fractions(fractions):
    i = 0
    while i < len(fractions):
        j = 0
        while j < len(fractions)- i- 1:
            nominator_one = fractions[j][0]
            denominator_one = fractions[j][1]
            result_one = nominator_one/denominator_one

            nominator_two = fractions[j+1][0]
            denominator_two = fractions[j+1][1]
            result_two = nominator_two/denominator_two
            if result_one>result_two:
                    fractions[j], fractions[j+1] = fractions[j+1], fractions[j]
            j += 1 
        i += 1

    return fractions

def main():
    print(simplify_fraction((3,3)))
    print(collect_fractions([(1,7),(2,6)]))
    print(sort_fractions([(2,3),(5,6),(1,2)]))

if __name__ == '__main__':
    main()