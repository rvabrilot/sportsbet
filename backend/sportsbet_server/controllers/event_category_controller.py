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

def add_event_category():
    if connexion.request.is_json:
        ec = connexion.request.get_json()
    
    existing_ec = (
        EventCategory.query.filter(EventCategory.name == ec['name'])
        .one_or_more()
    )

    if existing_ec is None:
        schema = EventCategorySchema()
        new_ec = schema.load(ec, session=db.session)
        db.session.add(new_ec)
        db.session.commit()
        data = schema.dump(new_ec)
        make_response(data, 201)
    else:
        abort(409, f"Event Category {ec['name']} already exists")

def get_event_category_by_id(id_:str):
    ec = EventCategory.query.filter(EventCategory.id == uuid.UUID(id_)).one_or_none()

    if ec is not None:
        data = EventCategorySchema().dump(ec)
        return make_response(data, 200)
    else:
        abort(404, f"EventCategory not found for id: {id_}")

def delete_event_category(id_:str):
    ec = EventCategory.query.filter(EventCategory.id == uuid.UUID(id_)).one_or_none()
    if ec is not None:
        db.session.delete(ec)
        db.session.commit()
        return make_response(f"EventCategory {id_} deleted", 200)
    else:
        abort(404, f"EventCategory not found for id: {id_}")

def update_event_category(id_:str, name):
    if connexion.request.is_json:
        body = EventCategory.from_dict(connexion.request.get_json())
    
    existing_ec = (
        EventCategory.query.filter(EventCategory.id == id)
        .one_or_none()
    )
    if existing_ec is not None:
        user_schema = EventCategorySchema()
        update = user_schema.load(existing_ec, session=db.session)
        update.name = body.name
        db.session.merge(update)
        db.session.commit()

        return make_response("Event Category updated", 200)
    else:
        abort("invalid Event Category id", 400)