from math import dist

def orientation(coordinate_landmark): 
    coordinate = [[0, 0] for _ in range(21)]
    for i in range (21):
        coordinate[i][0] = coordinate_landmark.landmark[i].x
        coordinate[i][1] = coordinate_landmark.landmark[i].y
    return coordinate

ERROR_THRESHOLD = 0.00
def finger_5_open(coordinate):
    d1 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[17][0], coordinate[17][1]])
    d2 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[20][0], coordinate[20][1]])
    
    if d2 > d1 + ERROR_THRESHOLD:  
        return True
    elif d1 > d2 + ERROR_THRESHOLD:  
        return False
    return None 

def finger_4_open(coordinate):
    d1 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[13][0], coordinate[13][1]])
    d2 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[16][0], coordinate[16][1]])
    
    if d2 > d1 + ERROR_THRESHOLD:
        return True
    elif d1 > d2 + ERROR_THRESHOLD:
        return False
    return None  

def finger_3_open(coordinate):
    d1 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[9][0], coordinate[9][1]])
    d2 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[12][0], coordinate[12][1]])
    
    if d2 > d1 + ERROR_THRESHOLD:
        return True
    elif d1 > d2 + ERROR_THRESHOLD:
        return False
    return None  

def finger_2_open(coordinate):
    d1 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[5][0], coordinate[5][1]])
    d2 = dist([coordinate[0][0], coordinate[0][1]], [coordinate[8][0], coordinate[8][1]])
    
    if d2 > d1 + ERROR_THRESHOLD:
        return True
    elif d1 > d2 + ERROR_THRESHOLD:
        return False
    return None 

# def finger_1_open(coordinate, labels):
#     ERROR_THRESHOLD = 0.00  # Define a threshold for error margin
#     x_thumb = coordinate[4][0]
#     y_thumb = coordinate[4][1]
#     x_index = coordinate[5][0]
#     y_index = coordinate[5][1]
    
#     # Check the position of the thumb relative to the index finger
#     if position(coordinate) == "Up":
#         if labels == "Left":
#             # Thumb should be to the right of the index finger when open
#             if (x_thumb + ERROR_THRESHOLD < x_index):
#                 return False  # Thumb is closed
#             else:
#                 return True  # Thumb is open
#         elif labels == "Right":
#             # Thumb should be to the left of the index finger when open
#             if (x_thumb - ERROR_THRESHOLD > x_index):
#                 return False  # Thumb is closed
#             else:
#                 return True  # Thumb is open
#     elif position(coordinate) == "Right" or position(coordinate) == "Left":
#         # Check vertical position of the thumb relative to the index finger
#         if (y_thumb < y_index - ERROR_THRESHOLD):
#             return False  # Thumb is closed
#         else:
#             return True  # Thumb is open

#     return False  # Default case, consider thumb closed if position is not recognized


def finger_1_open(coordinate, labels):
    x_thumb = coordinate[4][0]
    y_thumb = coordinate[4][1]
    x_index = coordinate[5][0]
    y_index = coordinate[5][1]
    # if abs(x_thumb - x0) < 0.05:      
    #     m_thumb = 1000000000
    # else:
    #     m_thumb = abs((y_thumb - y0)/(x_thumb - x0))
    # m_index = abs((y_index - y0)/(x_index - x0))
    if (position(coordinate) == "Up" and labels == "Left"):
        # if (m_thumb > m_index ):
        #     return False
        # else:
        #     return True
        if (x_thumb < x_index):
            return False
        else:
            return True
    elif (position(coordinate) == "Up" and labels == "Right"):
        if (x_thumb > x_index):
            return False
        else:
            return True
    elif(position(coordinate) == "Right" or position(coordinate) == "Left"):
        if (y_thumb < y_index):
            return True
        else:
            return False

    
def position(coordinate):
    x0 = coordinate[0][0]
    y0 = coordinate[0][1]
    x9 = coordinate[9][0]
    y9 = coordinate[9][1]

    if abs(x9 - x0) < 0.05:      
        m = 1000000000
    else:
        m = abs((y9 - y0)/(x9 - x0))       
        
    if m>=0 and m<=1:
        if x9 > x0:
            return "Right"
        else:
            return "Left"
    if m>1:
        if y9 < y0:      
            return "Up"
        else:
            return "Down"
        
def trial(coordinate):
    y_thumb = coordinate[4][1]
    y_index = coordinate[5][1]
    return y_index, y_thumb