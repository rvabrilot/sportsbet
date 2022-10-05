import email
from sportsbet_server.config import db, ma
from marshmallow import fields
from sqlalchemy.dialects.mysql import BINARY, DECIMAL, DATETIME, INTEGER, TEXT, VARCHAR

class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(BINARY(16), primary_key=True)
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
    id = db.Column(BINARY(16), primary_key=True)
    email = db.Column(VARCHAR)
    nickname = db.Column(VARCHAR)
    credit = db.Column(DECIMAL(10,10))
    md5 = db.Column(VARCHAR)
    role = db.Column(VARCHAR)

class Bet(db.Model):
    __tablename__ = "bet"
    id = db.Column(BINARY(16), primary_key=True)

class EventPlayer(db.Model):
    __tablename__ = "event_player"
    id = db.Column(BINARY(16), primary_key=True)

class EventCategory(db.Model):
    __tablename__ = "event_category"
    id = db.Column(BINARY(16), primary_key=True)