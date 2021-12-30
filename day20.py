from point import Point

with open('input\\day20') as f:
    algo, _, *image = f.read().splitlines()

values = {'#': '1', '.': '0'}
image_mapping = {Point(x, y): values[v] for y, row in enumerate(image) for x, v in enumerate(row)}
algo = [values[v] for v in algo]

def get_edges(curr_image):
    xx = [px.x for px in curr_image.keys()]
    yy = [px.y for px in curr_image.keys()]
    return (min(xx), max(xx), min(yy), max(yy))

def calc_out(curr_image, pixel, i):
    if i: default = "1" if i % 2 != 0 else "0"
    else: default = "0"
    return int(''.join(curr_image.get(pixel+o, default) for o in (-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j)), 2)

def enhance(image, algo, i):
    new_map = {}
    minx, maxx, miny, maxy = get_edges(image)
    for x in range(minx-1, maxx+2):
        for y in range(miny-1, maxy+2):
            pixel = Point(x, y)
            new_map[pixel] = algo[calc_out(image, pixel, i)]
    return new_map

for i in range(50):
    image_mapping = enhance(image_mapping, algo, i)
    if i+1 == 2:
        print('Part 1', len([v for v in image_mapping.values() if v == '1']))
    elif i+1 == 50:
        print('Part 2', len([v for v in image_mapping.values() if v == '1']))
