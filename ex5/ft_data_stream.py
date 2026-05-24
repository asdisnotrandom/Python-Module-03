#!/usr/bin/env python3

import typing
import random


def get_event() -> typing.Generator[tuple[str, str]]:
    actions: list[str] = ["run", "eat", "sleep", "grab", "move",
                          "climb", "swim", "release", "use"]
    players: list[str] = ["alice", "bob", "dylan", "charlie"]
    yield random.choice(players), random.choice(actions)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(0, 1000):
        store_gen: tuple[str, str] = next(get_event())
        print(f"Event {i}: Player {store_gen[0]} did action {store_gen[1]}")
    store_ten: list[tuple[str, str]] = []
    for _ in range(0, 10):
        temp_tup: tuple[str, str] = next(get_event())
        print(temp_tup)
        store_ten += [(temp_tup[0], temp_tup[1])]
    print(f"Built list of 10 events: {store_ten}")
    while len(store_ten) > 0:
        temp_index: int = random.randint(0, len(store_ten) - 1)
        print(f"Got event from list: {store_ten[temp_index]}")
        del store_ten[temp_index]
        print(f"Remains in list: {store_ten}")
