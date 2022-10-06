import connexion
import six

from sportsbet_server import config
from sportsbet_server.models import (Event)

def add_event():
    return {}

def get_event_by_id():
    return {}

def get_events():  

    events = Event.query.all()
    
    return events
