import connexion
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import User, UserSchema
import uuid

def get_users(body=None):
    all_users = User.query.all()
    users_schema = UserSchema(many=True)
    data = users_schema.dump(all_users)
    return data

def create_user(user=None):  
    
    if connexion.request.is_json:
        user = connexion.request.get_json()

    existing_user = (
        User.query.filter(User.email == user['email'])
        .one_or_none()
    )

    if existing_user is None:
        schema = UserSchema()
        new_user = schema.load(user, session=db.session) #.data
        db.session.add(new_user)
        db.session.commit()
        data = schema.dump(new_user)
        return data, 201
    else:
        abort(409, f"User {user['email']} already exists")

def delete_user(user_id):

    user = User.query.filter(User.id == user_id).one_or_none()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {user_id} deleted", 200)
    else:
        abort(404, f"User not found for id: {user_id}")

def get_user_by_id(user_id):
    user = User.query.filter(User.id == user_id).one_or_none()
    if user is not None:
        data = UserSchema().dump(user)
        return make_response(data, 200)
    else:
        abort(404, f"User not found for id: {user_id}")

def login_user(email=None, md5=None):
    existing_user = (
        User.query.filter(User.email == email)
        .filter(User.md5 == md5)
        .one_or_none()
    )
    if existing_user is not None:
        login_uuid = uuid()
        user_schema = UserSchema()
        update = user_schema.load(existing_user, session=db.session).data
        update.login_uuid = login_uuid
        db.session.merge(update)
        db.session.commit()

        return make_response(login_uuid, 200)
    else:
        abort("invalid email or md5", 400)

def logout_user(email=None, login_uuid=None):
    existing_user = (
        User.query.filter(User.email == email)
        .filter(User.login_uuid == login_uuid)
        .one_or_none()
    )

    if existing_user is not None:
        
        user_schema = UserSchema()
        update = user_schema.load(existing_user, session=db.session).data
        update.login_uuid = ""
        db.session.merge(update)
        db.session.commit()
        
        return make_response("user logged out", 200)
    else:
        abort("invalid email or login_uuid", 400)


def update_user(id, body=None):  

    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())
    
    existing_user = (
        User.query.filter(User.id == id)
        .one_or_none()
    )
    if existing_user is not None:
        user_schema = UserSchema()
        update = user_schema.load(existing_user, session=db.session).data
        update.email = body.email
        update.nickname = body.nickname
        update.credit = body.credit
        update.md5 = body.md5
        update.role = body.role
        db.session.merge(update)
        db.session.commit()

        return make_response("user updated", 200)
    else:
        abort("invalid user id", 400)
