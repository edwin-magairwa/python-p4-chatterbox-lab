from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    serialize_rules = ("-updated_at", )
