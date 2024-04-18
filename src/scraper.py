from typing import List
import requests as _requests
import bs4 as _bs4

def _generate_url(month: str, day: int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    print(f"Generated URL: {url}")  # Debug print
    return url

def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    if page.status_code == 200:
        print("Page fetched successfully")
    else:
        print(f"Failed to fetch page, status code: {page.status_code}")
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    url = _generate_url(month, day)
    page = _get_page(url)
    raw_events = page.find_all(class_="event")
    print(f"Found {len(raw_events)} events")  # Debug print
    events = [event.get_text(strip=True) for event in raw_events]
    return events

events = events_of_the_day("february", 23)
print(events)
