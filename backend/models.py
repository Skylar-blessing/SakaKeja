from flask import Flask
from sqlalchemy_serializer import SerializerMixin
from app import db

class Owner(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    password = db.Column(db.String)
    
    def __repr__(self):
        return f'<Owner: {self.first_name} {self.last_name}>'
    
