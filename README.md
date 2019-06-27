# Axes-of-Merit
Code related to the 9 Axes of Merit for Technosignatures (Sheikh 2019, in prep)

Documentation for the axes_figure figure creation function (from AOM.py) shown below:

axes_figure(axes_array, filename)
Creates a figure that shows the Nine Axes of Merit for Technosignatures with user-defined slider positions along each axis.

Inputs:  
- axes_array: An array of 9 integers each from 0-100, corresponding to slider positions on the Axes of Merit (in vertical order, top to bottom, from the base figure)
- filename: A string that will become the name of the output file

Outputs:
- None - the function immediately saves a .jpeg from your inputs

Assumptions:
- AOM.py and axes_of_merit_base.jpeg are in the directory you're running the code from

Usage Example:  
import AOM  
AOM.axes_figure([40,100,20,8,45,95,80,0,10], 'test')   
(see test.jpeg for output)
