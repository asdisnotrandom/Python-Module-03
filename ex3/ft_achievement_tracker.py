#!/usr/bin/env python3

import random


def gen_player_achievements() -> set[str]:
    achs_list: list[str] = ['Crafting Genius', 'Strategist',
                            'World Savior', 'Speed Runner',
                            'Survivor',
                            'Master Explorer', 'Treasure Hunter',
                            'Unstoppable', 'First Steps',
                            'Collector Supreme',
                            'Untouchable', 'Sharp Mind',
                            'Boss Slayer']
    new_achs = set(random.sample(achs_list, random.randint(0, len(achs_list))))
    return new_achs


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all_achs: set[str] = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_achs}")
    print()
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print()
    print(f"Only Alice has: {alice.difference(bob, dylan, charlie)}")
    print(f"Only Bob has: {bob.difference(alice, dylan, charlie)}")
    print(f"Only Charlie has: {alice.difference(bob, dylan, alice)}")
    print(f"Only Dylan has: {alice.difference(bob, alice, charlie)}")
    print()
    print(f"Alice is missing: {all_achs.difference(alice)}")
    print(f"Bob is missing: {all_achs.difference(bob)}")
    print(f"Charlie is missing: {all_achs.difference(charlie)}")
    print(f"Dylan is missing: {all_achs.difference(dylan)}")
