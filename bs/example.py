#03.04
def quadra(a,b,c):
    def calc(x):
        return (a * x**2) + b * x + c
    return calc
func = quadra(1, 2, 3)
print(func)