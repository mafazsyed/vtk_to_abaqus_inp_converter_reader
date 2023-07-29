import math

def find_closest_node(input_file, K1):
    def euclidean_distance(coord1, coord2):
        return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2)

    closest_node = None
    min_distance = float('inf')

    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            node_data = line.strip().split(',')
            node_number, x, y, z = int(node_data[0]), float(node_data[1]), float(node_data[2]), float(node_data[3])

            current_coordinate = (x, y, z)
            distance = euclidean_distance(K1, current_coordinate)

            if distance < min_distance:
                min_distance = distance
                closest_node = (node_number, x, y, z)

    return closest_node, min_distance

def main():
    x1, y1, z1 = map(float, input("Enter the x, y, and z coordinates of K1: ").split())
    K1 = (x1, y1, z1)
    input_file = input("Enter the path to the INP file: ")
    closest_node, min_distance = find_closest_node(input_file, K1)
    print(f"The closest node is: {closest_node[0]} with coordinates ({closest_node[1]}, {closest_node[2]}, {closest_node[3]}) and distance {min_distance}")

if __name__ == "__main__":
    main()
