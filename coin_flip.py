#!/usr/bin/env python3
"""Flip a virtual coin: Heads or Tails."""

import argparse
import random


def flip_once() -> str:
    return random.choice(["Heads", "Tails"])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Simulate coin flips. Each flip is 50% Heads, 50% Tails."
    )
    parser.add_argument(
        "-n",
        "--times",
        type=int,
        default=1,
        metavar="N",
        help="how many flips to do (default: 1)",
    )
    args = parser.parse_args()
    if args.times < 1:
        print("Use a positive number for --times.")
        return 1

    heads = tails = 0
    for i in range(args.times):
        outcome = flip_once()
        if outcome == "Heads":
            heads += 1
        else:
            tails += 1
        if args.times == 1:
            print(outcome)
        else:
            print(f"{i + 1}. {outcome}")

    if args.times > 1:
        print(f"Summary: {heads} Heads, {tails} Tails")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
