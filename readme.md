
#### Setup & Installation

1. Clone the Repository
> git clone https://github.com/iamsumitkumar10/event-scheduler-api.git
> cd event-scheduler-api

2. Install Dependencies
> First install Python and pip 
> pip install flask
> pip insatll pytest

3. Run the Application
> python app.py
Output: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


### API Endpoints

Endpoint	    Method	      Description

/	              GET	        API documentation
/events	        POST	      Create new event
/events	        GET	        List all events
/events/<id>	  GET	        Get single event
/events/<id>	  DELETE	    Delete event

1. Check API Documentation
> curl http://localhost:5000/

Output:
{
  "message": "Event Scheduler API",
  "endpoints": {
    "create_event": "POST /events",
    "list_events": "GET /events",
    "get_event": "GET /events/<event_id>",
    "delete_event": "DELETE /events/<event_id>"
  }
}

2. Create an Event
> curl -X POST http://localhost:5000/events \
-H "Content-Type: application/json" \
-d '{
    "title": "Client Meating",
    "start_time": "2025-02-15 Time 13:00:00",
    "end_time": "2025-2-15 Time 15:00:00"
}'

Output (Success):
{
  "id": "a1b2c3d4-e5f6...",
  "title": "Team Meeting",
  "start_time": "2025-02-15 Time 13:00:00",
  "end_time": "2025-2-15 Time 15:00:00"
}

3. List All Events
> curl http://localhost:5000/events

Output:
[
  {
    "id": "a1b2c3d4-e5f6...",
    "title": "Team Meeting",
    "start_time": "2023-12-01T10:00:00",
    "end_time": "2023-12-01T11:00:00"
  }
]


4. Delete an Event
> curl -X DELETE http://localhost:5000/events/a1b2c3d4-e5f6...

Output:
(Empty response with status code 204)


5. Update an Event
> curl -X PUT http://localhost:5000/events/c398549c-6b23-49fc-836c-0dbf54657f12 \
-H "Content-Type: application/json" \
-d '{
    "title": "Client Meating",
    "start_time": "2025-02-15 Time 13:00:00",
    "end_time": "2025-02-15 Time 15:00:00"
}'
output:
{
  "description": "",
  "end_time": "2025-02-15 Time 15:00:00",
  "id": "c398549c-6b23-49fc-836c-0dbf54657f12",
  "start_time": "2025-02-15 Time 13:00:00",
  "title": "Client Meating"
}


### Running Tests

> pytest test_events.py -v

output:
============================= test session starts ==============================
collected 5 items                                                    

test_events.py::test_home_page PASSED                          [ 20%]
test_events.py::test_create_event PASSED                       [ 40%]
test_events.py::test_get_all_events PASSED                     [ 60%]
test_events.py::test_get_one_event PASSED                      [ 80%]
test_events.py::test_delete_event PASSED                       [100%]

========================= 5 passed in 0.23s ==========================

## Verification
✔️ All functionalities confirmed working via Postman



