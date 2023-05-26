import vtk

def convert(vtk_file, inp_file):
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(vtk_file)
    reader.Update()

    mesh = reader.GetOutput()

    points = mesh.GetPoints()
    cells = mesh.GetCells()

    ugrid = reader.GetOutput()

    field_data = mesh.GetFieldData()

    ex_array = field_data.GetArray("EX")
    nu_array = field_data.GetArray("NUXY")
    dens_array = field_data.GetArray("DENS")

    materials = {}

    cell_data = mesh.GetCellData()
    cell_data_array = cell_data.GetArray(0)
    for i in range(cell_data_array.GetNumberOfTuples()):
        material_index = int(cell_data_array.GetValue(i))
        if material_index not in materials:
            materials[material_index] = []
        materials[material_index].append(i+1)

    with open(inp_file, 'w') as f:
        f.write("*HEADING\n")
        f.write("Abaqus DataFile Version 6.14\n")
        f.write("Legacy ASCII C3D10MH VTK to INP conversion\n")

        for material_index in range(1, len(materials)+1):
            material_name = "MAT-" + str(material_index)
            f.write("*MATERIAL, NAME=" + material_name + "\n")
            f.write("*DENSITY\n")
            f.write(str(dens_array.GetValue(material_index-1)) + "\n")
            f.write("*ELASTIC\n")
            f.write(str(ex_array.GetValue(material_index-1)) + ", " + str(nu_array.GetValue(material_index-1)) + "\n")

        f.write("*PART, NAME=Part-1\n")

        f.write('*NODE\n')
        for i in range(points.GetNumberOfPoints()):
            x, y, z = points.GetPoint(i)
            f.write(f'{i+1}, {x}, {y}, {z}\n')

        for material_index in range(1, len(materials)+1):
            elset_name = "ELSET-MATERIAL-" + str(material_index)
            f.write(f"*ELEMENT, TYPE=C3D10MH, ELSET={elset_name}\n")
            element_indices = materials[material_index]
            for i in element_indices:
                cell = ugrid.GetCell(i - 1)
                node_ids = [cell.GetPointId(j) + 1 for j in range(10)]
                f.write("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}\n".format(i, *node_ids))

        for material_index in range(1, len(materials)+1):
            elset_name = "ELSET-MATERIAL-" + str(material_index)
            material_name = "MAT-" + str(material_index)
            f.write("*SOLID SECTION, ELSET=" + elset_name + ", MATERIAL=" + material_name + "\n")
            f.write(",\n")
        f.write("*END PART\n")