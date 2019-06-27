"""
axes_figure(axes_array, filename)

Creates a figure that shows the Nine Axes of Merit for Technosignatures with user-defined slider positions along each axis.

# Inputs:  
- axes_array: An array of 9 integers each from 0-100, corresponding to slider positions on the Axes of Merit (in vertical order, top to bottom, from the base figure)
- filename: A string that will become the name of the output file

# Outputs:
- None - the function immediately saves a .jpeg from your inputs

# Assumptions:
- AOM.py and axes_of_merit_base.jpeg are in the directory you're running the code from
- You have installed the opencv and PIL packages

#Usage Example:

import AOM
AOM.axes_figure([40,100,20,8,45,95,80,0,10], 'test')

(see test.jpeg for output)

"""

import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2

def axes_figure(axes_array, filename):
    assert len(axes_array) == 9, "You have greater than or fewer than 9 axes!"
    for axis in axes_array:
        assert isinstance(axis, int), "Axis value must be an integer"
        assert axis >= 0, "Axis value is negative :("
        assert axis <= 100, "Axis value is greater than 100 :("
    assert type(filename) == str

    im = np.array(Image.open('axes_of_merit_base.jpeg'))
    min_pix = 125
    max_pix = 875
    diff_pix = max_pix - min_pix
    start_pos_2_array = [160, 300, 440, 610, 760, 910, 1055, 1225, 1370]
    for i in range(0, len(axes_array)):
        normalized = axes_array[i] / 100
        start_pos = int(diff_pix * normalized + min_pix)
        end_pos = start_pos + 25
        start_pos_2 = start_pos_2_array[i]
        end_pos_2 = start_pos_2 + 50
        cv2.rectangle(im,(start_pos,start_pos_2),(end_pos,end_pos_2),(0,0,0), -1)
    cv2.imwrite(filename + '.jpeg', im)
