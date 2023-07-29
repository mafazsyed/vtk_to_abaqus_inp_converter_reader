import vtk

def convert(vtk_file, inp_file):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(vtk_file)
    reader.Update()

    polydata = reader.GetOutput()

    with open(inp_file, "w") as f:
        f.write('*Heading\n')
        f.write("Abaqus DataFile Version 6.14\n")
        f.write("written by Mafaz Syed\n")

        f.write('*NODE, NSET=ALL\n')
        for i in range(polydata.GetNumberOfPoints()):
            point = polydata.GetPoint(i)
            f.write("{0}, {1}, {2}, {3}\n".format(i+1, point[0], point[1], point[2]))

        f.write("*ELEMENT, TYPE=CPE3\n")
        for i in range(polydata.GetNumberOfCells()):
            cell = polydata.GetCell(i)
            cell_type = cell.GetCellType()
            if cell_type == vtk.VTK_TRIANGLE:
                f.write("{0}, {1}, {2}, {3}\n".format(i+1, cell.GetPointId(0)+1, cell.GetPointId(1)+1, cell.GetPointId(2)+1))
