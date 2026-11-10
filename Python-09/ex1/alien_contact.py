#!/usr/bin/env python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_contact_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at"
                             " least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received"
                             " messages")
        return self


def print_contact(Alien: AlienContact):
    print("Alien Contact Log Validation")
    print("=" * 40)
    print("Valid contact report:")
    print(f"ID: {Alien.contact_id}")
    print(f"Type: {Alien.contact_type}")
    print(f"Location: {Alien.location}")
    print(f"Signal: {Alien.signal_strength}/10")
    print(f"Duration: {Alien.duration_minutes} minutes")
    print(f"Witnesses: {Alien.witness_count}")
    print(f"Message: '{Alien.message_received}'\n")


def main():
    try:
        contact = AlienContact(
                contact_id="AC_2024_001",
                timestamp=datetime.now(),
                location="Area 51, Nevada",
                contact_type=ContactType.radio,
                signal_strength=8.5,
                duration_minutes=45,
                witness_count=5,
                message_received="Greetings from Zeta Reticuli",
                is_verified=True
        )
        print_contact(contact)
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Moon Base Alpha",
            contact_type=ContactType.telepathic,
            signal_strength=6.0,
            duration_minutes=30,
            witness_count=1,
            message_received="Hello",
            is_verified=False
        )
    except ValidationError as e:
        print("=" * 40)
        print("Expected validation error:")
        for err in e.errors():
            msg = err["msg"].removeprefix("Value error, ")
            print(msg)


if __name__ == "__main__":
    main()
