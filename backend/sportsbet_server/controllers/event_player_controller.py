import connexion
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import EventPlayer, EventPlayerSchema
import uuid


def get_event_players():
    all_eps = EventPlayer.query.all()
    eps_schema = EventPlayerSchema(many=True)
    data = eps_schema.dump(all_eps)
    return data

def add_event_player(name = None):
    
    existing_ep = EventPlayer.query.filter(EventPlayer.name == name ).one_or_none()

    if existing_ep is None:
        schema = EventPlayerSchema()
        new_ep = EventPlayer()
        new_ep.name = name
        new_ep.id = uuid.uuid1()
        db.session.add(new_ep)
        db.session.commit()
        data = schema.dump(new_ep)
        return make_response(data, 201)
    else:
        abort(409, f"Event Player: {name} already exists")
    
def get_event_player_by_id(id_:str):
    ep = EventPlayer.query.filter(EventPlayer.id == uuid.UUID(id_)).one_or_none()

    if ep is not None:
        data = EventPlayerSchema().dump(ep)
        return make_response(data, 200)
    else:
        abort(404, f"EventPlayer not found for id: {id_}")

def delete_event_player(id_:str):
    ep = EventPlayer.query.filter(EventPlayer.id == uuid.UUID(id_)).one_or_none()
    if ep is not None:
        db.session.delete(ep)
        db.session.commit()
        return make_response(f"EventPlayer {id_} deleted", 200)
    else:
        abort(404, f"EventPlayer not found for id: {id_}")
    
def update_event_player():
    if connexion.request.is_json:
        body = connexion.request.get_json()
    else:
        abort(400, "no info provided in json")
    
    existing_ec = (
        EventPlayer.query.filter(EventPlayer.id == uuid.UUID(body["id"]))
        .one_or_none()
    )
    if existing_ec is not None:
        schema = EventPlayerSchema()
        existing_ec.name = body["name"]
        db.session.merge(existing_ec)
        db.session.commit()
        data = schema.dump(existing_ec)
        return make_response(data, 200)
    else:
        abort("invalid Event Player id", 400)