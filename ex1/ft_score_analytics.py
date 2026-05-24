#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    final_list: list[int] = []
    index: int = 1
    while index < len(sys.argv):
        try:
            final_list += [int(sys.argv[index])]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[index]}'")
        index = index + 1
    if len(final_list) < 1:
        print(
            "No scores provided.",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
    else:
        print(f"Scores processed: {final_list}")
        print(f"Total players: {len(final_list)}")
        print(f"Total score: {sum(final_list)}")
        print(f"Average score: {sum(final_list) / len(final_list)}")
        print(f"High score: {max(final_list)}")
        print(f"Low score: {min(final_list)}")
        print(f"Score range: {max(final_list) - min(final_list)}")
