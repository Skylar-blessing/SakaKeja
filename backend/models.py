from flask import Flask
from sqlalchemy_serializer import SerializerMixin
from app import db
from flask_sqlalchemy import sqlalchemy

db  = sqlalchemy()

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String),
    last_name = db.Column(db.String),
    email = db.Column(db.String),
    phone_number = db.Column(db.Integer),
    password = db.Column(db.String)
    
    houses = db.relationship("House", backref= "owner")
    
    def __repr__(self):
        return f'<Owner: {self.first_name} {self.last_name}>'
    
class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String),
    last_name = db.Column(db.String),
    email = db.Column(db.String),
    phone_number = db.Column(db.Integer),
    password = db.Column(db.String)
    
    houses = db.relationship("House", backref="tenant")
    reviews = db.relationship("Review", backref="tenant")
    
    
    
    
    def __repr__(self):
        return f'<Tenants: {self.first_name} {self.last_name}>'
    
class House(db.Model, SerializerMixin):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    number_of_rooms = db.Column(db.Integer),
    categories = db.Column(db.String),
    location = db.Column(db.String),
    price = db.Column(db.Integer),
    description = db.Column(db.String),
    Rating = db.Column(db.Float),
    image_urls = db.Column(db.ARRAY(db.String))
    
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    reviews = db.relationship("Review", backref="house")
    
    
    def __repr__(self):
        return f'<House: {self.number_of_rooms} {self.description}>'
    
class Review(db.Model, SerializerMixin): 
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    reviews = db.Column(db.String)
    
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    
    def __repr__(self):
        return f'<Reviews: {self.reviews}>'
    

class Owner_Tenant(db.Model, SerializerMixin):
    __tablename__ = 'owners_tenants'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"))
    
    
    def __repr__(self):
        return f'<owner_tenant: {self.id} tenant:{self.tenant_id} owner:{self.owner_id}>'
    
    
class Tenant_House(db.Model, SerializerMixin):
    __tablename__ = 'tenants_houses'
    id = db.Column(db.Integer, primary_key = True)
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"))
    house_id = db.Column(db.Integer, db.ForeignKey("houses.id"))
    
    def __repr__(self):
        return f'<tenant_house: {self.id}  tenant_id={self.tenant_id} house: {self.house_id}>'
    
    