#!/usr/bin/env python3

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def print_station(station: SpaceStation):
    if station.is_operational:
        status = "Operational"
    else:
        status = "Not-Operational"
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}\n")


def main():
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        station = SpaceStation(station_id="1df345hsf", name="Jedi",
                               crew_size=15, power_level=79.5,
                               oxygen_level=23.7,
                               last_maintenance=datetime.now(),
                               is_operational=True, notes="Refill Oxygen")
        print("Valid station created:")
        print_station(station)
    except ValidationError as e:
        print("=" * 40)
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])

    try:
        station = SpaceStation(station_id="2gh432kju", name="Overcrowded",
                               crew_size=21, power_level=10.5,
                               oxygen_level=2.0,
                               last_maintenance=datetime.now(),
                               is_operational=True, notes="Expel 1 person")
        print("Valid station created:")
        print_station(station)
    except ValidationError as e:
        print("=" * 40)
        print("Expected validation error:")
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
