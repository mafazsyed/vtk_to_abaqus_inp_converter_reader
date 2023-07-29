def find_least_and_greatest_coordinates(file_path, axis):
    least_coordinate = None
    greatest_coordinate = None
    node_with_least = None
    node_with_greatest = None

    with open(file_path, 'r') as file:
        for line in file:
            node_data = line.strip().split(',')
            node_number = int(node_data[0])
            x_coordinate = float(node_data[1])
            y_coordinate = float(node_data[2])
            z_coordinate = float(node_data[3])

            if axis == 'x':
                coordinate = x_coordinate
            elif axis == 'y':
                coordinate = y_coordinate
            elif axis == 'z':
                coordinate = z_coordinate
            else:
                print("Invalid axis selection.")
                return

            if least_coordinate is None or coordinate < least_coordinate:
                least_coordinate = coordinate
                node_with_least = (node_number, x_coordinate, y_coordinate, z_coordinate)

            if greatest_coordinate is None or coordinate > greatest_coordinate:
                greatest_coordinate = coordinate
                node_with_greatest = (node_number, x_coordinate, y_coordinate, z_coordinate)

    return axis, node_with_least, node_with_greatest
