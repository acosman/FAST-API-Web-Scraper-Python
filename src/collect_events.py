from typing import Iterator, Dict  # Added Dict to the import from typing
import datetime as _dt
import json as _json

import scraper as _scraper  # Corrected the import name

def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    for n in range((end_date - start_date).days):  # Simplified the range calculation
        yield start_date + _dt.timedelta(n)

def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2020, 1, 5)

    for date in _date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:  # Corrected the syntax here
            events[month] = dict()
        
        # Ensure the day's events are captured under the correct month and day
        events[month][date.day] = _scraper.events_of_the_day(month, date.day)

    return events

if __name__ == '__main__':
    events = create_events_dict()
    with open("events.json", "w") as events_file:
        _json.dump(events, events_file, ensure_ascii=False, indent=4)  # Adding indent for better readability
