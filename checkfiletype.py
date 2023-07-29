import vtk
import tkinter as tk
from tkinter import ttk

def count_cell_types(output):
    cell_type_counts = {}
    result_text = ""

    for i in range(output.GetNumberOfCells()):
        cell_type = output.GetCellType(i)
        cell_type_counts[cell_type] = cell_type_counts.get(cell_type, 0) + 1

    for cell_type, count in cell_type_counts.items():
        result_text += f"Cell type {cell_type}: {vtk.vtkCellTypes.GetClassNameFromTypeId(cell_type)} - {count} cells\n"

    return result_text

def convert(vtk_file, inp_file):
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(vtk_file)
    reader.Update()

    output = reader.GetOutput()
    result_text = ""

    if output.IsA("vtkPolyData"):
        result_text = "The output is of type vtkPolyData.\n"
        result_text += count_cell_types(output)
    elif output.IsA("vtkUnstructuredGrid"):
        result_text = "The output is of type vtkUnstructuredGrid.\n"
        result_text += count_cell_types(output)
    elif output.IsA("vtkStructuredGrid"):
        result_text = "The output is of type vtkStructuredGrid.\n"
        result_text += count_cell_types(output)
    elif output.IsA("vtkRectilinearGrid"):
        result_text = "The output is of type vtkRectilinearGrid.\n"
        result_text += count_cell_types(output)
    else:
        result_text = "The output is not of a recognized type."

    # Create a new tkinter window
    result_window = tk.Toplevel()
    result_window.title("Cell Type Results")

    # Add a label to the window with padding
    result_label = ttk.Label(result_window, text=result_text, padding="20 20")
    result_label.pack()


    # Show the window
    result_window.mainloop()