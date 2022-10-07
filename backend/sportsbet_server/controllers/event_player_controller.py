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
        ep = connexion.request.get_json()
    
    existing_ep = (
        EventPlayer.query.filter(EventPlayer.name == ep['name'])
        .one_or_more()
    )

    if existing_ep is None:
        schema = EventPlayerSchema()
        new_ep = schema.load(ep, session=db.session)
        db.session.add(new_ep)
        db.session.commit()
        data = schema.dump(new_ep)
        make_response(data, 201)
    else:
        abort(409, f"Event Player {ep['name']} already exists")
    
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
    
def update_event_player(id_:str, name_:str):
    if connexion.request.is_json:
        body = EventPlayer.from_dict(connexion.request.get_json())
    
    existing_ep = (
        EventPlayer.query.filter(EventPlayer.id == id)
        .one_or_none()
    )
    if existing_ep is not None:
        user_schema = EventPlayerSchema()
        update = user_schema.load(existing_ep, session=db.session).data
        update.name = body.name
        db.session.merge(update)
        db.session.commit()

        return make_response("Event Player updated", 200)
    else:
        abort("invalid Event Player id", 400)