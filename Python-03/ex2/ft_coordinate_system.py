#!/usr/bin/env python3

import math


def get_player_pos():
    while True:
        raw_coordinates = input("Enter new coordinates "
                                "as floats in format 'x,y,z': ")
        parts = raw_coordinates.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        coordinates = []
        valid = True

        for part in parts:
            clean_part = part.strip()
            try:
                coordinates.append(float(clean_part))
            except ValueError as e:
                print(f"Error on parameter '{clean_part}': {e}")
                valid = False
                break

        if valid:
            return tuple(coordinates)


def calculate_distance(p1, p2):
    distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                         + (p2[2] - p1[2])**2)

    return round(distance, 4)


def main():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    center = (0.0, 0.0, 0.0)
    distance_center = calculate_distance(p1, center)
    print(f"Distance to center: {distance_center}\n")
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    distance_coordinates = calculate_distance(p1, p2)
    print(f"Distance between the 2 sets of "
          f"coordinates: {distance_coordinates}")


if __name__ == "__main__":
    main()
