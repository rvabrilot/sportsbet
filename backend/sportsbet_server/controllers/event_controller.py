import connexion, uuid
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import Event, EventSchema

def add_event():
    if connexion.request.is_json:
        event = connexion.request.get_json()
    else:
        abort(400, "no info provided in json")

    existing_user = (
        Event.query.filter(Event.local_player == event['local_player'])
        .filter(Event.visitor_player == event['visitor_player'])
        .filter(Event.event_start == event['event_start'])
        .filter(Event.category == event['category'])
        .one_or_none()
    )

    if existing_user is None:
        schema = EventSchema()
        new = schema.load(event, session=db.session)
        db.session.add(new)
        db.session.commit()
        data = schema.dump(new)
        make_response( data, 201 )
    else:
        abort(409, f"Event already exists")

def get_event_by_id(id_):
    event = Event.query.filter(Event.id == uuid.UUID(id_)).one_or_none()
    if event is not None:
        data = EventSchema().dump(event)
        return make_response(data, 200)
    else:
        abort(404, f"Event not found for id: {id_}")

def get_events():  
    all = Event.query.all()
    schema = EventSchema(many=True)
    data = schema.dump(all)
    return data
