import vtk

def convert(vtk_file, inp_file):
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(vtk_file)
    reader.Update()

    mesh = reader.GetOutput()

    points = mesh.GetPoints()
    cells = mesh.GetCells()

    ugrid = reader.GetOutput()

    with open(inp_file, 'w') as f:
        f.write("*HEADING\n")
        f.write("Abaqus DataFile Version 6.14\n")
        f.write("written by Mafaz Syed\n")
        f.write('*NODE, NSET=ALL\n')
        for i in range(points.GetNumberOfPoints()):
            x, y, z = points.GetPoint(i)
            f.write(f'{i+1}, {x}, {y}, {z}\n')

        f.write("*ELEMENT, TYPE=C3D10MH\n")
        for i in range(ugrid.GetNumberOfCells()):
            cell = ugrid.GetCell(i)
            f.write("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}\n".format(i+1, cell.GetPointId(0)+1, cell.GetPointId(1)+1, cell.GetPointId(2)+1, cell.GetPointId(3)+1, cell.GetPointId(4)+1, cell.GetPointId(5)+1, cell.GetPointId(6)+1, cell.GetPointId(7)+1, cell.GetPointId(8)+1, cell.GetPointId(9)+1))