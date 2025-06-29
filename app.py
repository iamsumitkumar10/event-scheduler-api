from flask import Flask, jsonify, request
import storage  # Assuming this is storage module
import uuid
from datetime import datetime

app = Flask(__name__)

# Store events from storage
events = storage.load_events()

# function to find an event by ID
def find_event(event_id):
    for event in events:
        if event['id'] == event_id:
            return event
    return None

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    
    # Check required fields
    if not data or 'title' not in data or 'start_time' not in data or 'end_time' not in data:
        return jsonify({"error": "Missing title, start_time, or end_time"}), 400
    
    # Check if end time is after start time
    if data['start_time'] >= data['end_time']:
        return jsonify({"error": "End time must be after start time"}), 400
    
    # Create new event
    new_event = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'description': data.get('description', ''),
        'start_time': data['start_time'],
        'end_time': data['end_time']
    }
    
    events.append(new_event)
    storage.save_events(events)
    return jsonify(new_event), 201

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

# Get a single event
@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    event = find_event(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(event)

# Update an event
@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    event = find_event(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    
    data = request.get_json()
    
    # Update fields if they exist in the request
    if 'title' in data:
        event['title'] = data['title']
    if 'description' in data:
        event['description'] = data['description']
    if 'start_time' in data:
        event['start_time'] = data['start_time']
    if 'end_time' in data:
        event['end_time'] = data['end_time']
    
    # Check time validity
    if event['start_time'] >= event['end_time']:
        return jsonify({"error": "End time must be after start time"}), 400
    
    storage.save_events(events)
    return jsonify(event)

# Delete an event
@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    initial_length = len(events)
    events = [e for e in events if e['id'] != event_id]
    
    if len(events) == initial_length:
        return jsonify({"error": "Event not found"}), 404
    
    storage.save_events(events)
    return jsonify({"message": "Event deleted"}), 200

# Home page
@app.route('/')
def home():
    return """
    <h1>Event Scheduler API</h1>
    <p>Endpoints:</p>
    <ul>
        <li>GET /events - List all events</li>
        <li>POST /events - Create new event</li>
        <li>GET /events/[id] - Get specific event</li>
        <li>PUT /events/[id] - Update event</li>
        <li>DELETE /events/[id] - Delete event</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)