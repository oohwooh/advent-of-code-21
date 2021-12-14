def lynne(lines):
    points, instructions = lines[:lines.index("")], lines[lines.index("")+1:]
    points = [[int(a), int(b)] for (a, b) in [c.split(",") for c in points]]
    for instruction in instructions:
        axis, line = instruction.split(" ")[-1].split("=")
        axis = 0 if axis == "x" else 1
        line = int(line)
        for point in points:
            if point[axis] > line:
                point[axis] = 2*line - point[axis]