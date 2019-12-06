orbit_map = [i.split(")") for i in open("input.txt").read().splitlines()]

relations = {}

for x in orbit_map:
    main = x[0]
    orbiting = x[1]
    if orbiting in relations:
        relations[orbiting] += main
    else:
        relations[orbiting] = main

you_path = []
santa_path = []

for orbiter, planet in relations.items():
    if orbiter == "YOU":
        while planet in relations:
            you_path.append(planet)
            planet = relations[planet]
    if orbiter == "SAN":
        while planet in relations:
            santa_path.append(planet)
            planet = relations[planet]

for step in range(len(you_path)):
    if you_path[step] in santa_path:
        print(step + santa_path.index(you_path[step]))
        break
