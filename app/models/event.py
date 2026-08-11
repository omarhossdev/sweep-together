from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from pydantic import validator
from datetime import datetime
from app.constants import COUNTRIES


class Participant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    event_id: int = Field(foreign_key="event.id")
    joined_at: datetime = Field(default_factory=datetime.utcnow)

    event: "Event" = Relationship(back_populates="participants")
    user: "User" = Relationship(back_populates="participants")


class Verifier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    event_id: int = Field(foreign_key="event.id")
    verified_at: datetime = Field(default_factory=datetime.utcnow)
    is_location_cleaned: bool = False

    event: "Event" = Relationship(back_populates="verifiers")
    user: "User" = Relationship(back_populates="verifiers")


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(...,max_length=255)
    description: str = Field(...)
    organizer_id: int = Field(foreign_key="user.id")
    country: str = Field(...)
    city: str = Field(...)
    google_place_id: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    duration_in_hours: int = Field(...)
    is_finished: bool = False
    verifiers: list['Verifier'] = Relationship(back_populates="event")
    participants: list['Participant'] = Relationship(back_populates="event")

    @validator('country')
    def validate_country(cls, v):
        if v not in COUNTRIES:
            raise ValueError(f"Country must be one of: {COUNTRIES}")
        return v
