import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
import webbrowser
import surface_mesh_vtk_to_inp
import volume_mesh_vtk_to_inp
import volume_mesh_with_material_properties_vtk_to_inp
import checkfiletype
from userinputk1 import find_closest_node
from singlelargestandsmallestnode import find_least_and_greatest_coordinates
from constrainnodes import read_nodes, filter_nodes_by_axis, write_nodes_to_file

def open_linkedin():
    webbrowser.open_new(r"https://www.linkedin.com/in/mafazsyed")

def open_github():
    webbrowser.open_new(r"https://www.github.com/mafazsyed")

def open_portfolio():
    webbrowser.open_new(r"https://www.mafazsyed.com")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("VTK files", "*.vtk")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def filter_nodes_window():
    def browse_input_file():
        file_path = filedialog.askopenfilename(filetypes=[("INP and TXT files", "*.inp;*.txt")])
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, file_path)

    def browse_output_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".inp", filetypes=[("INP and TXT files", "*.inp;*.txt")])
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, file_path)

    def filter_and_save():
        input_file = input_file_entry.get()
        output_file = output_file_entry.get()
        axis = axis_entry.get()
        min_max = min_max_entry.get()
        threshold = float(threshold_entry.get())

        nodes = read_nodes(input_file)
        filtered_nodes = filter_nodes_by_axis(nodes, axis, min_max, threshold)
        write_nodes_to_file(filtered_nodes, output_file)

    filter_window = tk.Toplevel(app)
    filter_window.title("Filter Nodes (Axis, Min/Max, Inter-Element Spacing (V))")

    filter_frame = ttk.Frame(filter_window, padding="20 20 20 20")
    filter_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    filter_label = ttk.Label(filter_frame, text="Filter Nodes", font=("Calibri", 12, "bold"), justify=tk.CENTER)
    filter_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    description_label = ttk.Label(filter_frame, text="Filter nodes based on position along a coordinate axis and a distance threshold (V). Choose axis, min/max, value of V, and the input and output files.", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

    input_file_label = ttk.Label(filter_frame, text="Input INP or TXT file:")
    input_file_label.grid(row=2, column=0)
    input_file_entry = ttk.Entry(filter_frame, width=40)
    input_file_entry.grid(row=2, column=1)
    browse_input_file_button = ttk.Button(filter_frame, text="Browse", command=browse_input_file) # Add your command here
    browse_input_file_button.grid(row=2, column=2)

    output_file_label = ttk.Label(filter_frame, text="Output INP or TXT file:")
    output_file_label.grid(row=3, column=0)
    output_file_entry = ttk.Entry(filter_frame, width=40)
    output_file_entry.grid(row=3, column=1)
    browse_output_file_button = ttk.Button(filter_frame, text="Browse", command=browse_output_file) # Add your command here
    browse_output_file_button.grid(row=3, column=2)

    axis_label = ttk.Label(filter_frame, text="Coordinate axis (x, y, or z):")
    axis_label.grid(row=4, column=0)
    axis_entry = ttk.Entry(filter_frame)
    axis_entry.grid(row=4, column=1)

    min_max_label = ttk.Label(filter_frame, text="Enter 'min' for least or 'max' for greatest:")
    min_max_label.grid(row=5, column=0)
    min_max_entry = ttk.Entry(filter_frame)
    min_max_entry.grid(row=5, column=1)

    threshold_label = ttk.Label(filter_frame, text="Enter the value V (distance threshold):")
    threshold_label.grid(row=6, column=0)
    threshold_entry = ttk.Entry(filter_frame)
    threshold_entry.grid(row=6, column=1)

    filter_and_save_button = ttk.Button(filter_frame, text="Filter and Save", command=filter_and_save) # Add your command here
    filter_and_save_button.grid(row=7, column=1)

def input_axis_and_find_least_greatest_nodes():
    def browse_input_file():
        file_path = filedialog.askopenfilename(filetypes=[("INP and TXT files", "*.inp;*.txt")])
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, file_path)

    def find_least_greatest_nodes_and_display():
        axis = axis_entry.get()
        input_file = input_file_entry.get()
        axis, least_node, greatest_node = find_least_and_greatest_coordinates(input_file, axis)

        result_label.config(text=f"Node with the least {axis}-coordinate: {least_node}\nNode with the greatest {axis}-coordinate: {greatest_node}")

    least_greatest_window = tk.Toplevel(app)
    least_greatest_window.title("Find Least and Greatest Nodes")

    least_greatest_frame = ttk.Frame(least_greatest_window, padding="20 20 20 20")
    least_greatest_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    least_greatest_label = ttk.Label(least_greatest_frame, text="Least & Greatest Nodes", font=("Calibri", 12, "bold"), justify=tk.CENTER)
    least_greatest_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    description_label = ttk.Label(least_greatest_frame, text=" Select an input file (.inp or .txt), with just the nodes, and specify the axis to find the greatest and least nodes on that respective coordinate axis.", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

    input_file_label = ttk.Label(least_greatest_frame, text="Input INP or TXT file:")
    input_file_label.grid(row=2, column=0)
    input_file_entry = ttk.Entry(least_greatest_frame, width=40)
    input_file_entry.grid(row=2, column=1)
    browse_input_file_button = ttk.Button(least_greatest_frame, text="Browse", command=browse_input_file) # Add your command here
    browse_input_file_button.grid(row=2, column=2)

    axis_label = ttk.Label(least_greatest_frame, text="Coordinate axis (x, y, or z):")
    axis_label.grid(row=3, column=0)
    axis_entry = ttk.Entry(least_greatest_frame)
    axis_entry.grid(row=3, column=1)

    find_least_greatest_nodes_button = ttk.Button(least_greatest_frame, text="Find Least and Greatest Nodes", command=find_least_greatest_nodes_and_display) # Add your command here
    find_least_greatest_nodes_button.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    result_label = ttk.Label(least_greatest_frame, text="")
    result_label.grid(row=5, column=0, columnspan=3, pady=(10, 0))

def input_k1_coordinates_and_find_closest_node():
    def browse_input_file():
        file_path = filedialog.askopenfilename(filetypes=[("INP and TXT files", "*.inp;*.txt")])
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, file_path)

    def find_closest_node_and_display():
        x1 = float(x_entry.get())
        y1 = float(y_entry.get())
        z1 = float(z_entry.get())
        K1 = (x1, y1, z1)

        input_file = input_file_entry.get()
        closest_node, min_distance = find_closest_node(input_file, K1)

        result_label.config(text=f"The closest node is: {closest_node[0]} with coordinates ({closest_node[1]}, {closest_node[2]}, {closest_node[3]}) and distance {min_distance}")

    k1_coordinates_window = tk.Toplevel(app)
    k1_coordinates_window.title("Find Closest Node to a Reference Node")

    k1_coordinates_frame = ttk.Frame(k1_coordinates_window, padding="20 20 20 20")
    k1_coordinates_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    k1_coordinates_label = ttk.Label(k1_coordinates_frame, text="Closest Node to Reference Node", font=("Calibri", 12, "bold"), justify=tk.CENTER)
    k1_coordinates_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    description_label = ttk.Label(k1_coordinates_frame, text=" Select an input file (.inp or .txt), with just the nodes, and enter a reference node's coordinates to find the closest node.", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

    input_file_label = ttk.Label(k1_coordinates_frame, text="Input INP or TXT file:")
    input_file_label.grid(row=2, column=0)
    input_file_entry = ttk.Entry(k1_coordinates_frame, width=40)
    input_file_entry.grid(row=2, column=1)
    browse_input_file_button = ttk.Button(k1_coordinates_frame, text="Browse", command=browse_input_file) # Add your command here
    browse_input_file_button.grid(row=2, column=2)

    x_label = ttk.Label(k1_coordinates_frame, text="X:")
    x_label.grid(row=3, column=0)
    x_entry = ttk.Entry(k1_coordinates_frame)
    x_entry.grid(row=3, column=1)

    y_label = ttk.Label(k1_coordinates_frame, text="Y:")
    y_label.grid(row=4, column=0)
    y_entry = ttk.Entry(k1_coordinates_frame)
    y_entry.grid(row=4, column=1)

    z_label = ttk.Label(k1_coordinates_frame, text="Z:")
    z_label.grid(row=5, column=0)
    z_entry = ttk.Entry(k1_coordinates_frame)
    z_entry.grid(row=5, column=1)

    find_closest_node_button = ttk.Button(k1_coordinates_frame, text="Find Closest Node to a Reference Node", command=find_closest_node_and_display) # Add your command here
    find_closest_node_button.grid(row=6, column=0, columnspan=3, pady=(10, 0))

    result_label = ttk.Label(k1_coordinates_frame, text="")
    result_label.grid(row=7, column=0, columnspan=3, pady=(10, 0))

def convert_checkfiletype():
    vtk_file = file_entry.get()
    checkfiletype.convert(vtk_file, None)

def convert_surface_mesh_vtk():
    file_path = file_entry.get()
    inp_file = filedialog.asksaveasfilename(defaultextension=".inp", filetypes=[("Abaqus INP files", "*.inp")])
    if inp_file:
        surface_mesh_vtk_to_inp.convert(file_path, inp_file)
        os.startfile(inp_file)

def convert_volume_mesh():
    file_path = file_entry.get()
    inp_file = filedialog.asksaveasfilename(defaultextension=".inp", filetypes=[("Abaqus INP files", "*.inp")])
    if inp_file:
        volume_mesh_vtk_to_inp.convert(file_path, inp_file)
        os.startfile(inp_file)

def convert_volume_mesh_with_material_properties():
    file_path = file_entry.get()
    inp_file = filedialog.asksaveasfilename(defaultextension=".inp", filetypes=[("Abaqus INP files", "*.inp")])
    if inp_file:
        volume_mesh_with_material_properties_vtk_to_inp.convert(file_path, inp_file)
        os.startfile(inp_file)

def convert_selected():
    selected_option = conversion_option.get()
    if selected_option == "surface":
        convert_surface_mesh_vtk()
    elif selected_option == "volume":
        convert_volume_mesh()
    elif selected_option == "volume_with_material_properties":
        convert_volume_mesh_with_material_properties()

def about_window():
    about_win = tk.Toplevel(app)
    about_win.title("About")

    about_frame = ttk.Frame(about_win, padding="20 20 20 20")
    about_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    about_label = ttk.Label(about_frame, text="VTK to Abaqus INP Converter & Reader", font=("Calibri", 12, "bold"))
    about_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

    description_label = ttk.Label(about_frame, text="This application:\n" "Identifies Element Types & Converts Surface Mesh VTK (CPE3), Volume Mesh VTK (C3D10), & Volume Mesh with Material Properties VTK (C3D10), to their corresponding Abaqus INP Files;\n Identifies the closest node to a given reference node;\n Identifies the nodes with the least and gretest coordinates in a certain coordinate axis;\n Filters nodes based on their coordinate axis, least or greatest values, & inter-element spacing, V.", wraplength=450, justify=tk.CENTER)
    description_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

    version_label = ttk.Label(about_frame, text="Version: 1.2.0", font=('Calibri', 9, 'italic'))
    version_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))

    created_by_label = ttk.Label(about_frame, text="Created by Mafaz Syed", font=('Calibri', 9, 'italic'))
    created_by_label.grid(row=3, column=0, columnspan=3, pady=(0, 10))

    linkedin_logo = PhotoImage(file=r"C:\Users\mafaz\OneDrive\Desktop\Cell Type, K1, Single Node, Constrain Nodes 7\linkedin_logo.png.png")
    linkedin_logo = linkedin_logo.subsample(3)  # Make the image 2 times smaller
    linkedin_button = tk.Button(about_frame, image=linkedin_logo, command=open_linkedin, bd=0) # borderwidth set to 0
    linkedin_button.image = linkedin_logo  # keep a reference
    linkedin_button.grid(row=4, column=0, sticky='e')

    github_logo = PhotoImage(file=r"C:\Users\mafaz\OneDrive\Desktop\Cell Type, K1, Single Node, Constrain Nodes 7\github_logo.png.png")
    github_logo = github_logo.subsample(3)  # Make the image 2 times smaller
    github_button = tk.Button(about_frame, image=github_logo, command=open_github, bd=0) # borderwidth set to 0
    github_button.image = github_logo  # keep a reference
    github_button.grid(row=4, column=1)

    portfolio_logo = PhotoImage(file=r"C:\Users\mafaz\OneDrive\Desktop\Cell Type, K1, Single Node, Constrain Nodes 7\Favicon(3).png")
    portfolio_logo = portfolio_logo.subsample(20)  # Make the image 2 times smaller
    portfolio_button = tk.Button(about_frame, image=portfolio_logo, command=open_portfolio, bd=0) # borderwidth set to 0
    portfolio_button.image = portfolio_logo  # keep a reference
    portfolio_button.grid(row=4, column=2, sticky='w')

    close_button = ttk.Button(about_frame, text="Close", command=about_win.destroy)
    close_button.grid(row=5, column=0, columnspan=3, pady=(10, 0))

app = tk.Tk()
app.title("VTK to Abaqus INP Converter & Reader")

# Configure the root window to expand
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Use ttk style
style = ttk.Style()
style.theme_use("xpnative") # choose a modern theme
style.configure("TButton", padding=4, relief="flat",)

conversion_option = tk.StringVar(value="volume_with_material_properties")

frame = ttk.Frame(app, padding="20 20 20 20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configure the frame to expand
for i in range(12): # number of rows
    frame.grid_rowconfigure(i, weight=1)
for i in range(2): # number of columns
    frame.grid_columnconfigure(i, weight=1)

# Add a heading to the application
heading_label = ttk.Label(frame, text="VTK to Abaqus INP Converter & Reader", font=("Calibri", 12, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

description_text = ("This application determines element types of VTK mesh files converts them to Abaqus INP files, identifies closest and extreme nodes, and filters nodes based on coordinates and spacing.")
description_label = ttk.Label(frame, text=description_text, wraplength=500, justify=tk.CENTER)
description_label.grid(row=1, column=0, columnspan=2)

file_entry = ttk.Entry(frame, width=60)
file_entry.grid(row=2, column=0)

browse_button = ttk.Button(frame, text="Browse", command=browse_file) # Add your command here
browse_button.grid(row=2, column=1)

checkfiletype_button = ttk.Button(frame, text="Check Element Type(s)", command=convert_checkfiletype) # Add your command here
checkfiletype_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

surface_mesh_radiobutton = ttk.Radiobutton(frame, text="Convert Surface Mesh VTK", variable=conversion_option, value="surface")
surface_mesh_radiobutton.grid(row=4, column=0, columnspan=2, pady=(10, 0))

volume_mesh_radiobutton = ttk.Radiobutton(frame, text="Convert Volume Mesh VTK", variable=conversion_option, value="volume")
volume_mesh_radiobutton.grid(row=5, column=0, columnspan=2, pady=(10, 0))

volume_mesh_with_material_properties_radiobutton = ttk.Radiobutton(frame, text="Convert Volume Mesh with Material Properties VTK", variable=conversion_option, value="volume_with_material_properties")
volume_mesh_with_material_properties_radiobutton.grid(row=6, column=0, columnspan=2, pady=(10, 0))

convert_button = ttk.Button(frame, text="Convert", command=convert_selected) # Add your command here
convert_button.grid(row=7, column=0, columnspan=2, pady=(10, 0))

find_closest_node_button = ttk.Button(frame, text="Find Closest Node to a Reference Node", command=input_k1_coordinates_and_find_closest_node) # Add your command here
find_closest_node_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

find_least_greatest_nodes_button = ttk.Button(frame, text="Find Least and Greatest Nodes", command=input_axis_and_find_least_greatest_nodes) # Add your command here
find_least_greatest_nodes_button.grid(row=9, column=0, columnspan=2, pady=(10, 0))

filter_nodes_button = ttk.Button(frame, text="Filter Nodes (Axis, Min/Max, Inter-Element Spacing (V))", command=filter_nodes_window) # Add your command here
filter_nodes_button.grid(row=10, column=0, columnspan=2, pady=(10, 0))

about_button = ttk.Button(frame, text="About", command=about_window) # Add your command here
about_button.grid(row=11, column=1, columnspan=2, pady=(10, 0))

description_text2 = ("Version 1.2.0")
description_label2 = ttk.Label(frame, text=description_text2, font=('Calibri', 9, "italic"), wraplength=500, justify=tk.CENTER)
description_label2.grid(row=11, column=0, columnspan=2)

app.mainloop()