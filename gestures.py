from checkFinger import finger
from orientation import position

def gestures(coordinate, labels):
    open = finger(coordinate, labels)

    if "ALL FINGERS ARE CLOSED" in open:
        return "FIST"
    if "finger 1" in open and (position(coordinate) == "Right" or position(coordinate) == "Left"):
        return "LIKE"
    if all(finger in open for finger in ["finger 1", "finger 2", "finger 3", "finger 4", "finger 5"]):
        return "PALM"
    if open == ["finger 2"]:
        print("ONE Gesture Detected")
        return "ONE"
    if "finger 2" in open and "finger 5" in open:
        return "ROCK"
    else:
        return "UNKNOWN"

    # print(f"Detected fingers: {open}")  # Debugging line to see detected fingers
    # print(f"Labels: {labels}")  # Debugging line to see hand labels

    # if "ALL FINGERS ARE CLOSED" in open:
    #     return "FIST"
    # if "finger 1" in open and (position(coordinate) == "Right" or position(coordinate) == "Left"):
    #     return "LIKE"
    # if all(finger in open for finger in ["finger 1", "finger 2", "finger 3", "finger 4", "finger 5"]):
    #     return "PALM"
    # if open == ["finger 2"]:
    #     #print("ONE Gesture Detected")
    #     return "ONE"
    # if "finger 2" in open and "finger 5" in open:
    #     return "ROCK"
    # else:
    #     return "UNKNOWN"
