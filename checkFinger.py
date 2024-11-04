from orientation import *

def finger(coordinate, labels):
    open = []
    if (finger_1_open(coordinate, labels) or finger_2_open(coordinate) or finger_3_open(coordinate) or finger_4_open(coordinate) or finger_5_open(coordinate)):
        if (finger_1_open(coordinate, labels)):
            open.append("finger 1")
        if (finger_2_open(coordinate)):
            open.append("finger 2")
        if (finger_3_open(coordinate)):
            open.append("finger 3")
        if (finger_4_open(coordinate)):
            open.append("finger 4")
        if (finger_5_open(coordinate)):
            open.append("finger 5")
    else:
        open.append("ALL FINGERS ARE CLOSED")

    return open