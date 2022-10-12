import connexion, uuid
from flask import make_response, abort
from sportsbet_server.config import db
from sportsbet_server.models import User, UserSchema


def get_users(body=None):
    all_users = User.query.all()
    users_schema = UserSchema(many=True)
    data = users_schema.dump(all_users)
    return data

def create_user(user=None):  
    
    if connexion.request.is_json:
        user = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)

    existing_user = (
        User.query.filter(User.email == user['email'])
        .one_or_none()
    )

    if existing_user is None:
        schema = UserSchema()
        new_user = schema.load(user, session=db.session)
        new_user.id = uuid.uuid1()
        db.session.add(new_user)
        db.session.commit()
        data = schema.dump(new_user)
        return make_response( data, 201 )
    else:
        return make_response(f"User {user['email']} already exists", 409)

def delete_user(id_):
    user = User.query.filter(User.id == uuid.UUID(id_)).one_or_none()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {id_} deleted", 200)
    else:
        return make_response(f"User not found for id: {id_}", 404)

def get_user_by_id(id_:str):
    user = User.query.filter(User.id == uuid.UUID(id_)).one_or_none()
    if user is not None:
        data = UserSchema().dump(user)
        return make_response(data, 200)
    else:
        return make_response(f"User not found for id: {id_}", 404)

def login_user(email=None, md5=None):
    existing_user = (
        User.query.filter(User.email == email)
        .filter(User.md5 == md5)
        .one_or_none()
    )
    if existing_user is not None:
        login_uuid = uuid.uuid1()
        user_schema = UserSchema()
        update = user_schema.load(existing_user, session=db.session)
        update.login_uuid = login_uuid
        db.session.merge(update)
        db.session.commit()

        return make_response(login_uuid, 200)
    else:
        return make_response("invalid email or md5", 400)

def logout_user(email=None, login_uuid=None):
    existing_user = (
        User.query.filter(User.email == email)
        .filter(User.login_uuid == login_uuid)
        .one_or_none()
    )

    if existing_user is not None:
        
        user_schema = UserSchema()
        update = user_schema.load(existing_user, session=db.session)
        update.login_uuid = ""
        db.session.merge(update)
        db.session.commit()
        
        return make_response("user logged out", 200)
    else:
        return make_response("invalid email or login_uuid", 400)


def update_user(user=None):  

    if connexion.request.is_json:
        user = connexion.request.get_json()
    else:
        return make_response("no info provided in json", 400)
    
    existing_user = User.query.filter(User.id == uuid.UUID(user["id"]) ).one_or_none()
    
    if existing_user is not None:
        user_schema = UserSchema()
        existing_user.email = user["email"]
        existing_user.nickname = user["nickname"]
        existing_user.md5 = user["md5"]
        existing_user.role = user["role"]
        db.session.merge(existing_user)
        db.session.commit()
        data = user_schema.dump(existing_user)
        return make_response(data, 200)
    else:
        return make_response("invalid user id", 400)
