def elevator(people_weight, people_floors, elevator_floors, max_people, max_weight):
    trips = 0
    while len(people_weight) > 0:
        current_floors = [people_floors(index) for index, person in enumerate(people_weight) if sum(people_weight[:index+1]) <= max_weight and len(people_weight[:index+1]) ]
        trips += len(set(current_floors)) + 1
        people_weight = people_weight[len(current_floors):]
        people_floors = people_floors[len(current_floors):]


    return trips

print(elevator([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))