#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """ Determine if all the boxes can be opened """
    total_boxes = len(boxes)
    keys = {0}
    visited_boxes = set()

    next_box = 0
    while next_box != total_boxes:
        # Keep track of the encountered keys
        keys.update(boxes[next_box])
        # Keep track of the visited boxes
        visited_boxes.add(next_box)
        # Get the current unvisited boxes
        unvisited = keys.difference(visited_boxes)
        # Confirm that not all boxes have been visited
        if unvisited == set():
            break
        # Get the next box to be visited according to the boxes index
        next_box = min(unvisited)
        # Handle where the key to unknown boxes is found
        if next_box > total_boxes:
            break

    # Check if not all boxes are unlocked
    if ((unvisited == set() and len(visited_boxes) < total_boxes)
            or next_box > total_boxes):
        return False

    return True
