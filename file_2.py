def tuple_concat2(t):
    return 'File 2 + ' + str(t[0]) + str(t[1])

def print_list_concat(lst):
    from file_1 import list_concat
    return list_concat(lst[:3],lst[3:])