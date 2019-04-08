def odd_numbers():
    start = 1
    while start < 19:
        yield start
        start += 2

gen = odd_numbers()
for e in gen:
    print(e)


