#!/usr/bin/env python3

import sys


def process_scores(args):
    scores = []
    for arg in args:
        try:
            scores = scores + [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return (scores)


def main():
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    scores = process_scores(args) if args else []
    if scores:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
