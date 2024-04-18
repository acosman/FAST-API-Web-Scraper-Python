Historical Events API
Introduction
The Historical Events API provides access to significant historical events by date. It allows users to retrieve events for any given month, enhancing educational applications, trivia games, and more. Built using FastAPI, this project showcases a straightforward API that is easy to navigate and integrate into various applications.
Prerequisites
Before you begin, ensure you have the following installed:
Python 3.8 or newer
pip (Python package installer)
Installation
To set up the Historical Events API on your local machine, follow these steps:
Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/historical-events-api.git
cd historical-events-api
Install Dependencies:
bash
Copy code
pip install fastapi[all] uvicorn
Run the Application:
bash
Copy code
uvicorn main:app --reload
This command starts the server on http://127.0.0.1:8000. The --reload flag enables auto-reloading so the server will restart after code changes.
Usage
Once the API is running, you can interact with it using the following endpoints:
Root Endpoint:
GET /: Returns a welcome message.
All Events:
GET /events: Retrieves all historical events organized by month.
Events by Month:
GET /events/{month}: Retrieves events for a specific month. Replace {month} with the month name (e.g., january, february, etc.).
Example Requests
Welcome Message:
arduino
Copy code
curl http://localhost:8000/
Retrieve Events for January:
bash
Copy code
curl http://localhost:8000/events/january

License
Distributed under the MIT License. See LICENSE for more information.

