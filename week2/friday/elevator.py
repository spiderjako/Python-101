def elevator(people_weight, people_floors, elevator_floors, max_people, max_weight):
    trips = 0
    current_weight = 0
    start = 0
    for index, person in enumerate(people_weight):
        current_weight += person
        if current_weight > max_weight or len(people_weight[start:index])>=max_people:
            trips += len(set(people_floors[start:index])) + 1
            current_weight = person
            start = index
        trips += len(set(people_floors[start:])) + 1
    return trips

print(elevator([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))