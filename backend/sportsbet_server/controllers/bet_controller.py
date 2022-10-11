import connexion, uuid
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import Bet, BetSchema


def add_bet(bet=None):

    if connexion.request.is_json:
        bet = connexion.request.get_json()
    else:
        abort(400, "no info provided in json")
    
    existing_bet = (Bet.query.filter(Bet.event_id == bet['event_id'])
    .filter(Bet.user_id == bet["user_id"])
    .one_or_none()
    )

    if existing_bet is None:
        schema = BetSchema()
        new_bet = schema.load(bet, session=db.session)
        db.session.add(new_bet)
        db.session.commit()
    
        return make_response(schema.dump(new_bet), 201)
    else:
        abort(409, f"Bet for user_id: {bet['user_id']} and event_id:{bet['event_id']} already exists")


def delete_bet(id_):
    bet = Bet.query.filter(Bet.id == uuid.UUID(id_)).one_or_none()
    if bet is not None:
        db.session.delete(bet)
        db.session.commit()
    return make_response(f"Bet {id_} deleted", 204)


def get_bet_by_id(id_):
    bet = Bet.query.filter(Bet.id == uuid.UUID(id_)).one_or_none()
    if bet is not None:
        data = BetSchema().dump(bet)
        return make_response(data, 200)
    else:
        abort(404, f"Bet not found for id: {id_}")
