import connexion
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import EventCategory, EventCategorySchema
import uuid

def get_event_categories():
    all_ecs = EventCategory.query.all()
    ecs_schema = EventCategorySchema(many=True)
    data = ecs_schema.dump(all_ecs)
    return data

def add_event_category(name):
    existing_ep = EventCategory.query.filter(EventCategory.name == name ).one_or_none()

    if existing_ep is None:
        schema = EventCategorySchema()
        new_ep = EventCategory()
        new_ep.name = name
        new_ep.id = uuid.uuid1()
        db.session.add(new_ep)
        db.session.commit()
        data = schema.dump(new_ep)
        return make_response(data, 201)
    else:
        return make_response(f"Event Player: {name} already exists", 409)

def get_event_category_by_id(id_:str):
    ec = EventCategory.query.filter(EventCategory.id == uuid.UUID(id_)).one_or_none()

    if ec is not None:
        data = EventCategorySchema().dump(ec)
        return make_response(data, 200)
    else:
        return make_response(f"EventCategory not found for id: {id_}", 400)

def delete_event_category(id_:str):
    ec = EventCategory.query.filter(EventCategory.id == uuid.UUID(id_)).one_or_none()
    if ec is not None:
        db.session.delete(ec)
        db.session.commit()
        return make_response(f"EventCategory {id_} deleted", 200)
    else:
        return make_response(f"EventCategory not found for id: {id_}", 404)

def update_event_category():
    if connexion.request.is_json:
        body = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)
    
    existing_ec = (
        EventCategory.query.filter(EventCategory.id == uuid.UUID(body["id"]))
        .one_or_none()
    )
    if existing_ec is not None:
        schema = EventCategorySchema()
        existing_ec.name = body["name"]
        db.session.merge(existing_ec)
        db.session.commit()
        data = schema.dump(existing_ec)
        return make_response(data, 200)
    else:
        return make_response("invalid Event Category id", 400)