def find_neighbours(tuple, lst):
    i = 0
    summ = 0
    j = 0
    while i<len(lst):
        while j < len(lst[1]):
            try:
                if (abs(tuple[0]-i)== 1 and abs(tuple[1] - j)==1) or (tuple[0]==i and abs(tuple[1] - j)==1) or (tuple[1] == j and abs(tuple[0] - i)==1):
                    if lst[i][j]<lst[tuple[0]][tuple[1]]:
                        summ+=0
                    else:
                        summ += lst[i][j] - lst[tuple[0]][tuple[1]]
                elif i==tuple[0] and j == tuple[1]:
                    summ+= lst[i][j]
                else:
                    summ += lst[i][j]
            except IndexError:
                continue

            j+=1
        j=0
        i+=1
    return summ


def matrix_bombing_plan(lst):
    i = 0
    j = 0

    while i < len(lst):
        while j < len(lst[1]):
            touple = (i, j)
            summ = find_neighbours(touple, lst)
            print(str(touple) + ' ' + str(summ))
            j+=1
        j=0
        i+=1
    return

matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]])

