#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened

    Args:
        boxes(list): list of lists

    Returns:
        bool: True if all boxes can be opened, else False
    """
    total_boxes = len(boxes)
    keys = {0}
    visited_boxes = set()

    next_box = 0
    while next_box != total_boxes:
        keys.update(boxes[next_box])
        visited_boxes.add(next_box)
        unvisited = keys.difference(visited_boxes)
        # Break the loop when no keys to unlock any box
        if unvisited == set():
            break
        # Get the next box to be visited according to the boxes index
        next_box = min(unvisited)
        # Handle where the key to unknown boxes is found
        if next_box > total_boxes:
            break

    # Check if not all boxes are unlocked
    return len(visited_boxes) == total_boxes
