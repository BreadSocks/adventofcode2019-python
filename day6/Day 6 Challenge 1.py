orbit_map = [i.split(")") for i in open("input.txt").read().splitlines()]

relations = {}

for x in orbit_map:
    main = x[0]
    orbiting = x[1]
    if orbiting in relations:
        relations[orbiting] += main
    else:
        relations[orbiting] = main

print(relations)
count = 0
for orbiter, planet in relations.items():
    count += 1  # cos we're orbiting already
    while planet in relations:
        planet = relations[planet]
        count += 1

print(count)
