class Fib:
    def __init__(self):
        self.state = [1,1]

    def __call__(self):
        current_number = self.state[-1] + self.state[-2]
        self.state.append(current_number)
        return current_number


feel = Fib()
print(feel())
print(feel())
print(feel())
print(feel())
