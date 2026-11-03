#!/usr/bin/env Python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available for output.")

        data = self._storage.pop(0)
        current_rank = self._rank
        self._rank += 1

        return (current_rank, data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                    isinstance(x, (int, float))
                    and not isinstance(x, bool) for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]):
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(
                    isinstance(x, str) for x in data
            )
        return False

    def ingest(self, data: str | list[str]):
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                    isinstance(item, dict) and
                    all(isinstance(k, str) and
                        isinstance(v, str) for k, v in item.items())
                    for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]):
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                formatted_log = ": ".join(item.values())
                self._storage.append(formatted_log)
        else:
            formatted_log = ": ".join(data.values())
            self._storage.append(formatted_log)


def test_numeric():
    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")

    print(" Processing data: [1, 2, 3, 4, 5]")
    num_proc.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for i in range(3):
        rank, val = num_proc.output()
        print(f" Numeric value {rank}: {val}")


def test_text_log():
    print("Testing Text Processor...")
    text_proc = TextProcessor()
    print(f" Trying to validate input '42': {text_proc.validate(42)}")
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    text_proc.ingest(["Hello", "Nexus", "World"])
    print(" Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}\n")

    print("Testing Log Processor...")
    log_proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {logs}")
    log_proc.ingest(logs)
    print(" Extracting 2 values...")
    for i in range(2):
        rank, val = log_proc.output()
        print(f" Log entry {rank}: {val}")


def main():
    print("=== Code Nexus - Data Processor ===\n")

    test_numeric()
    print("\n")
    test_text_log()


if __name__ == "__main__":
    main()
