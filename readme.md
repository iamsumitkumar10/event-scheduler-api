# 📅 Event Scheduler API

A simple **Flask-based REST API** for creating, listing, updating, and deleting events.

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/iamsumitkumar10/event-scheduler-api.git
cd event-scheduler-api
```

### 2. Install Dependencies  
Make sure **Python** and **pip** are installed. Then run:
```bash
pip install flask
pip install pytest
```

### 3. Run the Application
```bash
python app.py
```
Expected output:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

## 📌 API Endpoints

| Endpoint         | Method | Description        |
|------------------|--------|--------------------|
| `/`              | GET    | API documentation |
| `/events`        | POST   | Create new event  |
| `/events`        | GET    | List all events   |
| `/events/<id>`   | GET    | Get single event  |
| `/events/<id>`   | DELETE | Delete event      |
| `/events/<id>`   | PUT    | Update event      |

---

## 🔎 Usage Examples

### 1. Check API Documentation
```bash
curl http://localhost:5000/
```
Response:
```json
{
  "message": "Event Scheduler API",
  "endpoints": {
    "create_event": "POST /events",
    "list_events": "GET /events",
    "get_event": "GET /events/<event_id>",
    "delete_event": "DELETE /events/<event_id>"
  }
}
```

---

### 2. Create an Event
```bash
curl -X POST http://localhost:5000/events \
-H "Content-Type: application/json" \
-d '{ "title": "Client Meeting", "start_time": "2025-02-15 Time 13:00:00", "end_time": "2025-02-15 Time 15:00:00" }'
```
Success Response:
```json
{
  "id": "a1b2c3d4-e5f6...",
  "title": "Client Meeting",
  "start_time": "2025-02-15 Time 13:00:00",
  "end_time": "2025-02-15 Time 15:00:00"
}
```

---

### 3. List All Events
```bash
curl http://localhost:5000/events
```
Response:
```json
[
  {
    "id": "a1b2c3d4-e5f6...",
    "title": "Team Meeting",
    "start_time": "2023-12-01T10:00:00",
    "end_time": "2023-12-01T11:00:00"
  }
]
```

---

### 4. Delete an Event
```bash
curl -X DELETE http://localhost:5000/events/a1b2c3d4-e5f6...
```
Response:  
(Empty response with status code **204**)

---

### 5. Update an Event
```bash
curl -X PUT http://localhost:5000/events/c398549c-6b23-49fc-836c-0dbf54657f12 \
-H "Content-Type: application/json" \
-d '{ "title": "Client Meeting", "start_time": "2025-02-15 Time 13:00:00", "end_time": "2025-02-15 Time 15:00:00" }'
```
Response:
```json
{
  "description": "",
  "end_time": "2025-02-15 Time 15:00:00",
  "id": "c398549c-6b23-49fc-836c-0dbf54657f12",
  "start_time": "2025-02-15 Time 13:00:00",
  "title": "Client Meeting"
}
```

---

## 🧪 Running Tests
```bash
pytest test_events.py -v
```
Output:
```
============================= test session starts =============================
collected 5 items

test_events.py::test_home_page PASSED        [ 20%]
test_events.py::test_create_event PASSED     [ 40%]
test_events.py::test_get_all_events PASSED   [ 60%]
test_events.py::test_get_one_event PASSED    [ 80%]
test_events.py::test_delete_event PASSED     [100%]

========================== 5 passed in 0.23s ==========================
```

---

## ✅ Verification
✔️ All functionalities confirmed working via **Postman**
