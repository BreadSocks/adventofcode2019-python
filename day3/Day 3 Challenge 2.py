import sys

wires = [i.split(",") for i in open("input.txt").read().splitlines()]
paths = dict()
for index, wire in enumerate(wires):
    point = [0, 0]
    points = ["0,0"]
    for movement in wire:
        # print("Running wire: " + str(index) + " Step " + str(wire.index(movement)) + " of " + str(len(wire)))
        direction = movement[0]
        distance = int(movement[1::])
        horizontal_distance = 0
        vertical_distance = 0
        if direction == 'L' or direction == 'R':
            horizontal_distance = distance
        elif direction == 'U' or direction == 'D':
            vertical_distance = distance

        for x in range(1, horizontal_distance + 1):
            if direction == 'L':
                point[0] = point[0] - 1
            elif direction == 'R':
                point[0] = point[0] + 1
            points.append(str(point[0]) + "," + str(point[1]))

        for y in range(1, vertical_distance + 1):
            if direction == 'U':
                point[1] = point[1] + 1
            elif direction == 'D':
                point[1] = point[1] - 1
            points.append(str(point[0]) + "," + str(point[1]))
    paths[index] = points
# print(paths)
intersections = set(paths[0]) & set(paths[1])
intersections.remove("0,0")

intersection_steps = []
for intersection in intersections:
    first_wire_steps = paths[0].index(intersection)
    second_wire_steps = paths[1].index(intersection)
    intersection_steps.append(first_wire_steps + second_wire_steps)
    print("steps: " + str(first_wire_steps + second_wire_steps))
print("smallest: " + str(min(intersection_steps)))
# smallest_distance = sys.maxsize
# for intersection in intersections:
#     translated = [abs(int(x)) for x in intersection.split(",")]
#     manhatten_distance = sum(translated)
#     if manhatten_distance < smallest_distance:
#         smallest_distance = manhatten_distance
# print(intersections)
# print(smallest_distance)
