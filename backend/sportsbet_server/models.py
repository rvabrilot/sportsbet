import email
from sportsbet_server.config import db, ma
from sqlalchemy.dialects.mysql import BINARY, DECIMAL, DATETIME, INTEGER, TEXT, VARCHAR
from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.schema import Column
import uuid


class UUID(types.TypeDecorator):
    impl = MSBinary
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
    id = db.Column(UUID, primary_key=True)
    event_start = db.Column(DATETIME)
    event_end = db.Column(DATETIME)
    local_player = db.Column(BINARY(16))
    visitor_player = db.Column(BINARY(16))
    category = db.Column(BINARY(16))
    flv = db.Column(DECIMAL(6,4))
    rfv = db.Column(DECIMAL(6,4))
    ptl = db.Column(DECIMAL(6,4))
    pte = db.Column(DECIMAL(6,4))
    gv0 = db.Column(DECIMAL(6,4))
    gv1 = db.Column(DECIMAL(6,4))
    gv2 = db.Column(DECIMAL(6,4))
    gv3 = db.Column(DECIMAL(6,4))
    minimum_bets = db.Column(INTEGER)
    stats_link = db.Column(TEXT)

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
    id = db.Column(BINARY(16), primary_key=True)

class EventPlayer(db.Model):
    __tablename__ = "event_player"
    id = db.Column(BINARY(16), primary_key=True)

class EventCategory(db.Model):
    __tablename__ = "event_category"
    id = db.Column(BINARY(16), primary_key=True)