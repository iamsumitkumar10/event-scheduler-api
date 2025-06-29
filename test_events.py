from app import app, events
import pytest

# This makes test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

# Test if home page works
def test_home_page(client):
    response = client.get('/')
    assert b"Event Scheduler API" in response.data

# Test creating an event
def test_create_event(client):
    # Good event data
    good_event = {
        "title": "Birthday Party",
        "start_time": "2023-12-25T14:00:00",
        "end_time": "2023-12-25T16:00:00"
    }
    response = client.post('/events', json=good_event)
    assert response.status_code == 201
    assert b"Birthday Party" in response.data

    # Bad event data (missing title)
    bad_event = {
        "start_time": "2023-12-25T14:00:00",
        "end_time": "2023-12-25T16:00:00"
    }
    response = client.post('/events', json=bad_event)
    assert response.status_code == 400

# Test getting all events
def test_get_all_events(client):
    # First add an event
    client.post('/events', json={
        "title": "Test Event",
        "start_time": "2023-01-01T10:00:00",
        "end_time": "2023-01-01T11:00:00"
    })
    
    response = client.get('/events')
    assert response.status_code == 200
    assert len(response.json) > 0

# Test getting one event
def test_get_one_event(client):
    # Add an event first
    new_event = client.post('/events', json={
        "title": "Find This",
        "start_time": "2023-01-01T10:00:00",
        "end_time": "2023-01-01T11:00:00"
    }).json
    
    # Get the event we just made
    response = client.get(f'/events/{new_event["id"]}')
    assert response.status_code == 200
    assert response.json["title"] == "Find This"

# Test deleting an event
def test_delete_event(client):
    # Add an event first
    new_event = client.post('/events', json={
        "title": "Delete Me",
        "start_time": "2023-01-01T10:00:00",
        "end_time": "2023-01-01T11:00:00"
    }).json
    
    # Delete it
    response = client.delete(f'/events/{new_event["id"]}')
    assert response.status_code == 200
    
    # Check it's really gone
    response = client.get(f'/events/{new_event["id"]}')
    assert response.status_code == 404