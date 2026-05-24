#!/usr/bin/env python3


import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    plyrs: list[str] = [
                            "Alice",
                            "bob",
                            "Charlie",
                            "dylan",
                            "Emma",
                            "Gregory",
                            "john",
                            "kevin ",
                            "Liam"
                            ]
    print(f"Initial list of players: {plyrs}")
    new_cap: list[str] = [i.capitalize() for i in plyrs]
    print(f"New list with all names capitalized: {new_cap}")
    set_plyrs: set[str] = set(plyrs)
    set_newcap: set[str] = set(new_cap)
    inter_plyrs: set[str] = set_plyrs.intersection(set_newcap)
    print(f"New list of capitalized names only: {inter_plyrs}")
    print()
    score_dict: dict[str, int] = {}
    score_dict = {k: random.randint(0, 1000) for k in new_cap}
    print(f"Score dict: {score_dict}")
    total_score: int = sum(score_dict.values())
    average_score: float = round(total_score / len(score_dict.keys()), 2)
    print(f"Score average is {average_score}")
    comp_dict: dict[str, int] = {}
    comp_dict = {k: score_dict[k] for k in score_dict.keys()
                 if score_dict[k] > average_score}
    print(f"High scores: {comp_dict}")
