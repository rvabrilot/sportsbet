import email
from sportsbet_server.config import db, ma
from sqlalchemy.dialects.mysql import BINARY, DECIMAL, DATETIME, INTEGER
from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.schema import Column
import uuid


class UUID(types.TypeDecorator):
    impl = MSBinary
    cache_ok=False
    def __init__(self):
        self.impl.length = 16
        types.TypeDecorator.__init__(self,length=self.impl.length)

    def process_bind_param(self,value,dialect=None):
        if value and isinstance(value,uuid.UUID):
            return value.bytes
        elif value and not isinstance(value,uuid.UUID):
            raise ValueError(f"value {value} is not a valid uuid.UUID")
        else:
            return None

    def process_result_value(self,value,dialect=None):
        if value:
            return uuid.UUID(bytes=value)
        else:
            return None

    def is_mutable(self):
        return False

class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(UUID, primary_key=True, default=uuid.uuid1())
    event_start = db.Column(DATETIME)
    event_end = db.Column(DATETIME)
    local_player = db.Column(UUID)
    visitor_player = db.Column(UUID)
    category = db.Column(UUID)
    goals = db.Column(INTEGER)
    result = db.Column(db.String)
    stats_link = db.Column(db.String)

class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(UUID, primary_key=True, default=uuid.uuid1() )
    email = db.Column(db.String)
    nickname = db.Column(db.String)
    credit = db.Column(db.Numeric)
    md5 = db.Column(db.String)
    role = db.Column(db.String)
    login_uuid = db.Column(UUID)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

class Bet(db.Model):
    __tablename__ = "bet"
    id = db.Column(UUID, primary_key=True, default=uuid.uuid1())
    bet_datetime = db.Column(DATETIME)
    goals = db.Column(INTEGER)
    result = db.Column(db.String)
    user_id = db.Column(UUID)
    event_id = db.Column(UUID)
    status = db.Column(db.String)


class BetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bet
        load_instance = True


class EventPlayer(db.Model):
    __tablename__ = "event_player"
    id = db.Column(UUID, primary_key=True, default=uuid.uuid1())
    name = db.Column(db.String)

class EventPlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventPlayer
        load_instance = True

class EventCategory(db.Model):
    __tablename__ = "event_category"
    id = db.Column(UUID, primary_key=True, default=uuid.uuid1())
    name = db.Column(db.String)

class EventCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventCategory
        load_instance = True