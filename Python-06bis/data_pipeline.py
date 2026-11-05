#!/usr/bin/env python3

from typing import Any, Protocol
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]):
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]):
        values = [item[1] for item in data]
        print("CSV Output:")
        print(",".join(values))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]):
        pairs = []
        for rank, val in data:
            pairs.append(f'"item_{rank}: "{val}"')
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


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
        print("\n== DataStream statistics ==")
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin):
        for proc in self._processors:
            batch_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    batch_data.append(proc.output())
                except IndexError:
                    break
            if batch_data:
                plugin.process_output(batch_data)


def test():
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    stream_pipeline = DataStream()
    stream_pipeline.print_processors_stats()
    print("\nRegistering Processors\n")
    stream_pipeline.register_processor(NumericProcessor())
    stream_pipeline.register_processor(TextProcessor())
    stream_pipeline.register_processor(LogProcessor())
    first_batch = [
            'Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING', 'log_message':
              'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42,
            ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {first_batch}")
    stream_pipeline.process_stream(first_batch)
    stream_pipeline.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream_pipeline.output_pipeline(3, CSVPlugin())
    stream_pipeline.print_processors_stats()
    another_batch = [
            21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR', 'log_message': '500 server crash'},
             {'log_level': 'NOTICE', 'log_message':
              'Certificate expires in 10 days'}],
            [32, 42, 64, 84, 128, 168], 'World hello'
    ]
    print(f"\nSend another batch of data: {another_batch}")
    stream_pipeline.process_stream(another_batch)
    stream_pipeline.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream_pipeline.output_pipeline(5, JSONPlugin())
    stream_pipeline.print_processors_stats()


if __name__ == "__main__":
    test()
