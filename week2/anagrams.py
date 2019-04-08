def anagrams(first, second):
    if sorted(first.upper()) == sorted(second.upper()):
        return True
    else:
        return False

print(anagrams('kliata', 'kilata'))

