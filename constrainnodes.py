import math

def read_nodes(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes = []
        for line in lines:
            node_data = line.strip().split(',')
            node_number, x, y, z = int(node_data[0]), float(node_data[1]), float(node_data[2]), float(node_data[3])
            nodes.append((node_number, x, y, z))
    return nodes

def distance(node1, node2):
    return math.sqrt((node1[1] - node2[1])**2 + (node1[2] - node2[2])**2 + (node1[3] - node2[3])**2)

def filter_nodes(nodes, threshold):
    min_z = min(node[3] for node in nodes)
    filtered_nodes = [node for node in nodes if abs(node[3] - min_z) < threshold]
    return filtered_nodes

def filter_nodes_by_axis(nodes, axis, min_max, threshold):
    if axis == 'x':
        coord_idx = 1
    elif axis == 'y':
        coord_idx = 2
    elif axis == 'z':
        coord_idx = 3
    else:
        raise ValueError("Invalid axis selection.")

    if min_max == "min":
        min_max_value = min(node[coord_idx] for node in nodes)
    elif min_max == "max":
        min_max_value = max(node[coord_idx] for node in nodes)
    else:
        raise ValueError("Invalid min_max selection.")

    filtered_nodes = [node for node in nodes if abs(node[coord_idx] - min_max_value) < threshold]
    return filtered_nodes

def write_nodes_to_file(nodes, output_filename):
    with open(output_filename, 'w') as file:
        for node in nodes:
            line = f"{node[0]},{node[1]},{node[2]},{node[3]}\n"
            file.write(line)

def main():
    input_filename = r"C:\Users\mafaz\OneDrive\Desktop\Nodesnoheading.inp"
    output_filename = r"C:\Users\mafaz\OneDrive\Desktop\cnds.inp"

    axis = input("Enter the coordinate axis (x, y, or z): ")
    min_max = input("Enter 'min' for least or 'max' for greatest: ")
    threshold = float(input("Enter the value V (distance threshold): "))

    nodes = read_nodes(input_filename)
    filtered_nodes = filter_nodes_by_axis(nodes, axis, min_max, threshold)
    write_nodes_to_file(filtered_nodes, output_filename)

if __name__ == '__main__':
    main()