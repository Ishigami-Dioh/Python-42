#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._rank: int = 0
        self.total_processed: int = 0

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
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
            self.total_processed += len(data)
        else:
            self._storage.append(str(data))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
            self.total_processed += len(data)
        else:
            self._storage.append(data)
            self.total_processed += 1


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
                all(isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items())
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                formatted_log = (f"{item.get('log_level', '')}:"
                                 f" {item.get('log_message', '')}")
                self._storage.append(formatted_log)
            self.total_processed += len(data)
        else:
            formatted_log = (f"{data.get('log_level', '')}: "
                             f"{data.get('log_message', '')}")
            self._storage.append(formatted_log)
            self.total_processed += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process element in "
                      f"stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors or all(p.total_processed == 0
                                       for p in self._processors):
            print("No processor found, no data")
            return

        for proc in self._processors:
            if proc.total_processed > 0:
                name = proc.__class__.__name__.replace("Processor",
                                                       " Processor")
                print(f"{name}: total {proc.total_processed} items processed,"
                      f" remaining {len(proc._storage)} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream_pipeline = DataStream()
    stream_pipeline.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    stream_pipeline.register_processor(NumericProcessor())

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO',
             'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream_pipeline.process_stream(batch)
    stream_pipeline.print_processors_stats()
    print("\nRegistering other data processors")
    stream_pipeline.register_processor(TextProcessor())
    stream_pipeline.register_processor(LogProcessor())
    print("Send the same batch again")
    stream_pipeline.process_stream(batch)
    stream_pipeline.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for _ in range(3):
        stream_pipeline._processors[0].output()
    for _ in range(2):
        stream_pipeline._processors[1].output()
    for _ in range(1):
        stream_pipeline._processors[2].output()
    stream_pipeline.print_processors_stats()
