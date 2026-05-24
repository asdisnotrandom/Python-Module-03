#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    succes: int = 0
    while succes == 0:
        try:
            new_values = input(
                            "Enter new coordinates as "
                            "floats in format 'x,y,z': "
                            ).split(',')
            for i in new_values:
                float(i)
        except SyntaxError:
            print("Invalid syntax")
        except Exception as e:
            print(f"Error on parameter '{i}': {e}")
        else:
            x: float = float(new_values[0])
            y: float = float(new_values[1])
            z: float = float(new_values[2])
            final_values: tuple[float, float, float] = (x, y, z)
            succes = 1
    return final_values


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coord1 = get_player_pos()
    print(f"Got first tuple: {coord1}")
    print(f"It includes: X={coord1[0]}, Y={coord1[1]}, Z={coord1[2]}")
    print()
    print("Get a second set of coordinates")
    coord2 = get_player_pos()
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]
    z1 = coord1[2]
    z2 = coord2[2]
    result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {result}")
