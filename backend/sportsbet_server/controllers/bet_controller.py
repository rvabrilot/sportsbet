import connexion, uuid
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import Bet, BetSchema, Event, EventSchema
from datetime import datetime

def add_bet(bet=None):

    if connexion.request.is_json:
        bet = connexion.request.get_json()
    else:
        return make_response(400, "no info provided in json")
    
    existing_bet = (Bet.query.filter(Bet.event_id == uuid.UUID(bet['event_id']))
    .filter(Bet.user_id == uuid.UUID(bet["user_id"]))
    .one_or_none()
    )
    existing_event = (Event.query.filter(Event.id == uuid.UUID(bet['event_id']))
    .one_or_none()
    )

    if existing_event is None:
        return make_response("invalid event id", 400)
    else:
        if existing_event.event_start <= datetime.now():
            return make_response("cannot create bet if event has started", 400)

    if int(bet["goals"]) < 0 :
        return make_response("goals cant be less than cero", 400)
    
    if bet["result"] not in ['l','e','v']:
        return make_response("invalid result, has to be l, e or v", 400)

    if existing_bet is None:
        schema = BetSchema()
        new_bet = Bet()
        new_bet.event_id = uuid.UUID(bet['event_id'])
        new_bet.user_id = uuid.UUID(bet["user_id"])
        new_bet.goals = bet["goals"]
        new_bet.result = bet["result"]
        new_bet.status = "created"
        new_bet.id = uuid.uuid1()
        db.session.add(new_bet)
        db.session.commit()
    
        return make_response(schema.dump(new_bet), 201)
    else:
        return make_response(409, f"Bet for user_id: {bet['user_id']} and event_id:{bet['event_id']} already exists")

def update_bet(bet=None):

    if connexion.request.is_json:
        bet = connexion.request.get_json()
    else:
        return make_response(400, "no info provided in json")
    
    existing_bet = (Bet.query.filter(Bet.id == uuid.UUID(bet['id']))
        .one_or_none()
    )
    try:
       int(bet["goals"])
    except Exception as e:
        return make_response(str(e), 400) 

    existing_event = (Event.query.filter(Event.id == uuid.UUID(bet['event_id']))
    .one_or_none()
    )

    if existing_event is None:
        return make_response("invalid event id", 400)
    else:
        if existing_event.event_start <= datetime.now():
            return make_response("cannot update bet if event has started", 400)

    if int(bet["goals"]) < 0 :
        return make_response("goals cant be less than cero", 400)
    
    if bet["result"] not in ['l','e','v']:
        return make_response("invalid result, has to be l, e or v", 400)
    
    if existing_bet is not None:
        schema = BetSchema()
        existing_bet.event_id = uuid.UUID(bet['event_id'])
        existing_bet.user_id = uuid.UUID(bet["user_id"])
        existing_bet.goals = bet["goals"]
        existing_bet.result = bet["result"]
        existing_bet.status = "updated"
        db.session.merge(existing_bet)
        db.session.commit()
    
        return make_response(schema.dump(existing_bet), 201)
    else:
        return make_response(409, f"Bet for user_id: {bet['user_id']} and event_id:{bet['event_id']} already exists")


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
        return make_response(404, f"Bet not found for id: {id_}")

def get_bets():
    all_bets = Bet.query.all()
    bet_schema = BetSchema(many=True)
    data = bet_schema.dump(all_bets)
    return data
