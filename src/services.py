from fastapi import HTTPException
from typing import Dict
import json

print("services module loaded")
print("get_month_events function loaded")

def get_all_events() -> Dict:
    with open("events.json") as events_file:
        data = json.load(events_file)
    return data

def get_month_events(month: str) -> Dict:
    events = get_all_events()
    try:
        # Ensure the month key exists in the dictionary
        month_events = events[month.lower()]  # Using lower() to handle case-insensitivity
        return month_events
    except KeyError:
        # Raising HTTPException instead of KeyError for proper API error handling
        raise HTTPException(status_code=404, detail=f"No data available for the month: {month}")


