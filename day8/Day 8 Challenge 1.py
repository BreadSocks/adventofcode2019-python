image = [int(i) for i in open("input.txt").read()]
size = 25 * 6
layers = []

for i in range(0, len(image), size):
    layers.append(image[i:i + size])

num_of_zeros = 25 * 6
lowest_index = None
for index, layer in enumerate(layers):
    num = layer.count(0)
    if num < num_of_zeros:
        lowest_index = index
        num_of_zeros = num

print(lowest_index)

layer = layers[lowest_index]

print(layer.count(1) * layer.count(2))
