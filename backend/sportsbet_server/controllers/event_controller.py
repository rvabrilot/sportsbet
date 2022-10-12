import connexion, uuid
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import Event, EventSchema

def add_event():
    if connexion.request.is_json:
        event = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)

    existing_user = (
        Event.query.filter(Event.local_player == uuid.UUID(event['local_player']))
        .filter(Event.visitor_player == uuid.UUID(event['visitor_player']))
        .filter(Event.event_start == event['event_start'])
        .filter(Event.category == uuid.UUID(event['category']))
        .one_or_none()
    )

    if existing_user is None:
        schema = EventSchema()
        new_event = Event() #schema.load(event, session=db.session)
        new_event.id = uuid.uuid1()
        new_event.category = uuid.UUID(event['category'])
        new_event.local_player = uuid.UUID(event['local_player'])
        new_event.visitor_player = uuid.UUID(event['visitor_player'])
        new_event.event_start = event['event_start']
        new_event.event_end = event['event_end']
        new_event.stats_link = event['stats_link']
        
        db.session.add(new_event)
        db.session.commit()
        data = schema.dump(new_event)
        return make_response( data, 201 )
    else:
        return make_response(f"Event already exists", 409)

def get_event_by_id(id_):
    event = Event.query.filter(Event.id == uuid.UUID(id_)).one_or_none()
    if event is not None:
        data = EventSchema().dump(event)
        return make_response(data, 200)
    else:
        return make_response(f"Event not found for id: {id_}", 404)

def get_events():  
    all = Event.query.all()
    schema = EventSchema(many=True)
    data = schema.dump(all)
    return data

def update_event():
    if connexion.request.is_json:
        event = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)
    
    existing_event = (
        Event.query.filter(Event.id == uuid.UUID(event["id"]))
        .one_or_none()
    )
    if existing_event is not None:
        schema = EventSchema()
        existing_event.category = uuid.UUID(event['category'])
        existing_event.local_player = uuid.UUID(event['local_player'])
        existing_event.visitor_player = uuid.UUID(event['visitor_player'])
        existing_event.event_start = event['event_start']
        existing_event.event_end = event['event_end']
        existing_event.stats_link = event['stats_link']
        existing_event.goals = event["goals"]
        existing_event.result = event["result"]
        db.session.merge(existing_event)
        db.session.commit()
        data = schema.dump(existing_event)
        return make_response(data, 200)
    else:
        return make_response("invalid Event Player id", 400)