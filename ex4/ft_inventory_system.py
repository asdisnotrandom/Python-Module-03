#!/usr/bin/env python3

import sys


class ParamError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def sep_arg() -> dict[str, int]:
    main_dict: dict[str, int] = {}
    sep_list: list[str] = []
    for i in sys.argv[1:]:
        if len(i.split(':')) == 2:
            sep_list = i.split(':')
            try:
                if sep_list[0] in main_dict:
                    raise ParamError(
                        f"Redundant item {sep_list[0]} - discarding")
                if int(sep_list[1]) < 1:
                    raise ParamError(f"Error - invalid parameter '{i}'")
                main_dict[sep_list[0]] = int(sep_list[1])
            except ParamError as e:
                print(f"{e}")
            except ValueError as e:
                print(f"Quantity error for {sep_list[0]}: {e}")
        else:
            try:
                raise ParamError(f"Error - invalid parameter {i}")
            except ParamError as e:
                print(f"{e}")
    return main_dict


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main_inv: dict[str, int] = sep_arg()
    if len(main_inv) < 1:
        print(
            "No scores provided.",
            "Usage: python3 ft_inventory_system.py <item_name>:<quantity> ..."
            )
    else:
        sum_vals = sum(main_inv.values())
        print(f"Got inventory: {main_inv}")
        print(f"Item list: {list(main_inv.keys())}")
        print(f"Total quantity of the {len(main_inv.keys())}",
              f"items: {sum_vals}")
        for k in main_inv:
            print(f"Item {k} represents",
                  f"{round(main_inv[k] * 100 / sum_vals, 1)}")
        dict_keys: list[str] = list(main_inv.keys())
        dict_vals: list[int] = list(main_inv.values())
        max_dict: int = dict_vals[0]
        cnt_max: int = 0
        min_dict: int = dict_vals[0]
        cnt_min: int = 0
        j: int = 0
        for i in main_inv.values():
            if max_dict < i:
                max_dict = i
                cnt_max = j
            if min_dict > i:
                min_dict = i
                cnt_min = j
            j = j + 1
        print(f"Item most abundant: {dict_keys[cnt_max]}",
              f"with {dict_vals[cnt_max]}")
        print(f"Item least abundant: {dict_keys[cnt_min]}",
              f"with {dict_vals[cnt_min]}")
        main_inv.update({"magic_item": 1})
        print(f"Updated inventory: {main_inv}")
