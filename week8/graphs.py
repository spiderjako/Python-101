def deep_find(data, key, list_of_parents =[]):
    path += [curr_vert]

def deep_find_BFS(data, key, list_vertices=[]):
     for vertex in data:
        if key == vertex:
            return data[vertex]
        else:
            list_vertices.append(vertex)
        if isinstance(data[vertex], dict) and vertex in list_vertices:
            return deep_find(data[vertex], key)
def deep_find_all(data, key, array=[]):
    for vertex in data:
        print(data[vertex])
        if key == vertex:
            array.append(data[vertex])
        if isinstance(data[vertex], dict):
            return deep_find_all(data[vertex], key, array)
def deep_update(data, key, val):
    for vertex in data:
        if key == vertex:
            data[vertex] = val
        if isinstance(data[vertex],dict):
            return deep_update(data[vertex],key,val)
def deep_apply(func, data):
    for vertex in data:
        func(vertex)
        if isinstance(data[vertex],dict):
            return deep_apply(func, data[vertex])
def deep_compare(obj1, obj2,list1=[],list2=[], isEqual=1):
    for vertex1, vertex2 in zip(obj1, obj2):
        if type(vertex1)==type(vertex2):
            if type(vertex1)==dict:
                print('is here')
                return deep_compare(obj1[vertex1],obj2[vertex2])
            else:
                if vertex1!=vertex2 or obj1[vertex1]!=obj2[vertex2]:
                    isEqual = 0
                    return False
        else:
            return False
    if isEqual:
        return True
def main():
    example_dict2 = {
        'a':{
        'a1':3,
        'a2':5,
        'a3':6
        },
        'c':{
        'a':{
        'a4':'woohoo',
        'a5':'C'
        }
        }
    }
    print(deep_find(example_dict2,'c'))
    deep_update(example_dict2,'a',3)
    print(example_dict2)

if __name__=='__main__':
    main()