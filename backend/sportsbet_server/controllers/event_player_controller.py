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

def add_event_player():
    if connexion.request.is_json:
        body = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)
    
    existing_ep = EventPlayer.query.filter(EventPlayer.name == body["name"] ).one_or_none()

    if existing_ep is None:
        schema = EventPlayerSchema()
        new_ep = EventPlayer()
        new_ep.name = body["name"]
        new_ep.id = uuid.uuid1()
        db.session.add(new_ep)
        db.session.commit()
        data = schema.dump(new_ep)
        return make_response(data, 201)
    else:
        return make_response(f"Event Player: {body['name']} already exists", 409)
    
def get_event_player_by_id(id_:str):
    ep = EventPlayer.query.filter(EventPlayer.id == uuid.UUID(id_)).one_or_none()

    if ep is not None:
        data = EventPlayerSchema().dump(ep)
        return make_response(data, 200)
    else:
        return make_response(f"EventPlayer not found for id: {id_}", 404)

def delete_event_player(id_:str):
    ep = EventPlayer.query.filter(EventPlayer.id == uuid.UUID(id_)).one_or_none()
    if ep is not None:
        db.session.delete(ep)
        db.session.commit()
        return make_response(f"EventPlayer {id_} deleted", 200)
    else:
        return make_response(f"EventPlayer not found for id: {id_}", 400)
    
def update_event_player():
    if connexion.request.is_json:
        body = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)
    
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
        return make_response("invalid Event Player id", 400)