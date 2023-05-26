# VTKtoAbaqusINPConverter-Reader User Guide

# Table of Contents

- [Introduction](#introduction)
  - [About the Application](#about-the-application)
  - [System Requirements](#system-requirements)
  - [Installation Guide](#installation-guide)
  - [Overview of User Interface](#overview-of-user-interface)
- [Features & Functionality](#features--functionality)
  - [Checking VTK File and Cell Type](#checking-vtk-file-and-cell-type)
  - [Converting VTK Files to Abaqus INP Files](#converting-vtk-files-to-abaqus-inp-files)
  - [Node-Identification](#node-identification)
    - [Input Nodal Coordinate Data File Format](#input-nodal-coordinate-data-file-format)
    - [Finding Closest Node to a Reference Node (Coordinate)](#finding-closest-node-to-a-reference-node-coordinate)
    - [Finding Least & Greatest Nodes](#finding-least--greatest-nodes)
    - [Filter Nodes Based on Axis, Min/Max, & Distance Threshold (V)](#filter-nodes-based-on-axis-minmax--distance-threshold-v)
- [Troubleshooting](#troubleshooting)
- [Updates & Version History](#updates--version-history)

# Introduction
## About the Application
The VTK to Abaqus INP Converter and Reader application streamlines and automates the conversion of various VTK files to Abaqus INP files. This includes files such as surface mesh, volume mesh, and volume mesh with material properties VTK files. The application is also capable of identifying relevant node(s) for respective boundary and loading condition applications (or other purposes). The application can also easily determine the element type of the VTK file.

## System Requirements
The latest version of the application supports Windows and Linux operating systems.

## Installation Guide
Download and run the VTKtoAbaqusINPConverter_1.1.0.exe file (or VTKtoAbaqusINPConverter_1.1.0_ubuntu for Linux) from the [GitHub Page](https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader) page. No installation is required.

## Overview of User Interface
Figure 1 shows the user interface of the application with reference to each chapter for the feature’s user guide.

<img src="https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/f4a4d46b-9610-4b57-9241-9c26598af263" width="500">

Figure 1 – User Interface of the VTK to Abaqus INP Converter & Reader Application

# Features & Functionality

## Checking VTK File and Cell Type
To determine the element type of a VTK file, first browse to or specify the file path of the VTK file. Then, select ‘Check Element Type’, as shown by Figure 2.

<img src="https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/5b6b3958-ff83-4f8b-ac2d-9f2098b154d6" width="500">

Figure 2 – Check the File and Element Types Present in the VTK File (Steps in Numbers)

The Cell Type Results window will display the VTK file and cell type(s) and the number of cells (elements) present, as shown by Figure 3.

![Cell Type Results](https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/b89c75df-dc46-4cea-9fba-6d1844ce4d5a)

Figure 3 – Cell Type Results Window Displaying the File and Cell Type

All VTK cell types are supported; refer to the VTK documentation for an up-to-date list here.

## Converting VTK Files to Abaqus INP Files
The following VTK files (either Legacy ASCII or Legacy Binary) could be converted to their corresponding Abaqus INP files:

- Surface Mesh VTK of the Element Type CPE3 (cell type 4)
- Volume Mesh VTK of the Element Type C3D10 (cell type 4)
- Volume Mesh with Material Properties VTK of the Element Type C3D10 (cell type 4)

Other VTK file types have not been tried, however, could be tried, but successful or accurate conversion is not guaranteed.

First, browse to or specify the file path of the VTK file then choose the appropriate conversion depending on the type of the VTK file (surface mesh, volume mesh, or volume mesh with material properties), as shown by Figure 4.

<img src="https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/d1c6ea5d-26c2-475a-bbda-39e94cb839d0" width="500">

Figure 4 – Convert VTK File to Corresponding Abaqus INP File (Steps in Numbers)

Save the generated Abaqus INP file to your desired location.

## Node-Identification
The following node-determining features are available:

- Determine the closest node to a reference node. Note that the closest node is determined in terms of a reference coordinate and not in terms of a node, therefore, more flexibility is provided.
- Determine the least and greatest nodes present within a coordinate axis (x, y, or z).
- Filter and determine nodes based on the coordinate axis, greatest or least, and a distance threshold. The distance threshold is the distance from the greatest or least node on the selected coordinate system.

Figure 5 shows the relevant UI options in the application for each feature.

<img src="https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/a17942fb-11c5-4f2d-aa41-c942b3cb7420" width="500">

Figure 5 – UI Options Highlighted for the Node Identification Features

### Input Nodal Coordinate Data File Format
The input file for the node identification features should contain, on each line, the node number followed by its coordinates, spaced out with delimiters. An example is shown below:

<img src="https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/da37ca60-178f-4768-a4dd-36eebeb28a34" width="500">

Note that a heading should not be included, and the nodes do not have to be in chronological order.

### Finding Closest Node to a Reference Node (Coordinate)
To determine the closest node to a reference node (coordinate), first specify the file path to the input file containing the nodal coordinate data then enter the x, y, and z reference coordinates to which the closest node will be determined. Select ‘Find Closest Node to a Reference Node’ to print the closest node (node ID), its coordinates, and its Euclidean distance to the specified coordinate are printed.

![Closest Node](https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/d2c80911-d1e5-478a-bbd3-0c1e6f7fd197)

Figure 6 – Closest Node to a Reference Coordinate Window

### Finding Least & Greatest Nodes
To determine the least and greatest nodes within a coordinate axis, first specify the file path to the input file containing the nodal coordinate data, then enter the coordinate axis (‘x’, ‘y’, or ‘z’) and select ‘Find Least and Greatest Nodes’.

![Least and Greatest Nodes](https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/5d09ccdc-86fa-40b8-a604-4811da345d69)

Figure 7 – Least and Greatest Nodes Along a Specified Axis Window

### Filter Nodes Based on Axis, Min/Max, & Distance Threshold (V)
To filter nodes based on the coordinate axis, min/mas, and a distance threshold (from the least or max), first specify the file path of the input file containing the nodal coordinate data and the output TXT or INP file (or any other preferred file format). Then, specify the coordinate axis (‘x’, ‘y’, or ‘z’) and ‘min’ or ‘max’ for the least or greatest node in the specified coordinate axis. Enter the distance threshold, V, and select ‘Filter and Save’. All nodes within a distance V of the greatest/least node on the specified axis is saved to the output file path directory.

![Filter Nodes](https://github.com/mafazsyed/VTKtoAbaqusINPConverter-Reader/assets/120568449/58a5753a-09b8-43a8-9161-5908a978b3df)

Figure 8 – Filter Nodes Based on Coordinate Axis, Min/Max, and Distance Threshold Window

# Troubleshooting
The Windows Terminal/Shell window displays any errors encountered and prints relevant information depending on the task performed.

## Updates & Version History

- **Version 1.0.0:** 
  - Initial Release

- **Version 1.1.0:** 
  - Updated graphical user interface to a modern style
  - Other user interface and quality of life updates
  - Added a window pop-up displaying the cell type instead of having to refer to the console
  - Added Linux support/compatibility

- **Version 1.2.0 (In Development / Awaiting Release):** 
  - The closest node could be determined using a node ID as well instead of just coordinates
  - Greatest and least nodes could be determined via a user-defined coordinate axis, instead of just using the existing coordinate axis. (Specifically useful to identify nodes along a specific line)
  - Greatest and least nodes for each coordinate axis printed instead of needing to select one
  - Updated text for each task to better represent the functionality
  - Looking at options to add MacOS compatibility
