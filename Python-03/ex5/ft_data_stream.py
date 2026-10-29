#!/usr/bin/env python3

import typing
import random


ACTIONS: tuple[str, ...] = (
    "run",
    "eat",
    "sleep",
    "climb",
    "move",
    "swim",
    "grab",
    "use",
    "release",
    "craft",
    "hit",
    "tame",
)


NAMES: tuple[str, ...] = (
    "alice",
    "bob",
    "dylan",
    "charlie",
    "alara",
)


def gen_event(
    names: tuple[str, ...],
    actions: tuple[str, ...],
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(names)
        action = random.choice(actions)

        yield (name, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        chosen_int = random.randrange(len(events))
        chosen = events.pop(chosen_int)
        yield chosen


def main():
    print("=== Game Data Stream Processor ===\n")
    stream = gen_event(NAMES, ACTIONS)
    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")
    events_list = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")
    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
