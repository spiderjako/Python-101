import sys

class Monom:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power

    def get_coeff(self, monom):
        if monom.find("*") == -1:
            return 1

        n = monom.find('*') -1
        int_coeff = 0
        for i in range(0,monom.find('*')):
            int_coeff += int(monom[i])*(10**n)
            n-=1
        if int_coeff == 1:
            return ''

        self.coeff=int_coeff
        return self.coeff

    def get_power(self, monom):
        if monom.find('^') == -1:
            return 1

        int_power = 0
        n = len(monom) - monom.find('^') - 2
        for i in range(monom.find('^')+1,len(monom)):
            int_power += int(float(monom[i])) * (10**n)

        self.power = int_power
        return self.power

    def find_const(self, lst):
        for j, i in enumerate(lst):
            if i[0] in '1234567890' and i.find('*') == -1 and i.find('^') == -1:
                lst.pop(j)
        return lst

    def differentiate(self, polinomial):
        to_string = ''
        index = 0
        split_polinom = polinomial.split('+')
        self.find_const(split_polinom)
        for i in split_polinom:
            poli_power = int(float(self.get_power(i)))
            poli_coeff = int(self.get_coeff(i))
            
            to_string += str(poli_power*poli_coeff)
            if i.find('*') != -1 and poli_power != 1:
                to_string += i[i.find('*')+1]
            elif poli_power == 1:
                to_string +=''
            else:
                to_string += i[0]
            if poli_power != 2 and poli_power != 1:
                to_string += '^' + str(poli_power - 1)
            else:
                to_string += ''

            if index != len(split_polinom) - 1:
                to_string += '+'
            index += 1
        return to_string

class Polinom(Monom):
    def __init__(self, pol):
        self.pol = pol
    
    def derivative(self):
        polinomial = self.pol
        return self.differentiate(polinomial)

                


def main():
    f = sys.argv
    polinomial = Polinom(f[1])
    print(polinomial.pol.split('+'))
    print(polinomial.derivative())



if __name__ == '__main__':
    main()