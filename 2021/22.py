
# Online Python - IDE, Editor, Compiler, Interpreter

def test():
    lines = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10""".split("\n")
    return lines
    
def points_in_range(xmin, xmax, ymin, ymax, zmin, zmax):
    points = []
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            for z in range(zmin,zmax + 1):
                points.append((x, y, z))
    return points
lines = test()

grid = {}

for line in lines:
    onoff, coords = line.split()
    x,y,z = coords.split(",")
    xmin, xmax = x.split("=")[1].split("..")
    ymin, ymax = y.split("=")[1].split("..")
    zmin, zmax = z.split("=")[1].split("..")
    points = points_in_range(int(xmin), int(xmax), int(ymin),
                             int(ymax), int(zmin), int(zmax))
    if onoff=="on":
        action = 1
    else:
        action = 0
    for point in points:
        grid[point] = action

print (grid)
    # print (onoff, xmin, ymin, zmin)
count = 0
for point in grid:
    count += grid[point]
print (count)
    
