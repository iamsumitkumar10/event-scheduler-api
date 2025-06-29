import json
import os

# File where we'll store our events
EVENTS_FILE = 'events.json'

def load_events():
    """Load events from the JSON file"""
    # Check if the file exists first
    if not os.path.exists(EVENTS_FILE):
        return []  # Return empty list if no file
    
    try:
        # Open the file for reading
        with open(EVENTS_FILE, 'r') as file:
            events = json.load(file)
            return events
    except:
        # If something goes wrong, return empty list
        return []

def save_events(events):
    """Save events to the JSON file"""
    # Open the file for writing
    with open(EVENTS_FILE, 'w') as file:
        # Save the events with nice formatting
        json.dump(events, file, indent=2)