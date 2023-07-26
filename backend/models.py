from app import db
from sqlalchemy_serializer import SerializerMixin

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    houses = db.relationship("House", backref="owner")
    
    houses = db.relationship("House", backref= "owner")
    
    def __repr__(self):
        return f'<Owner: {self.first_name} {self.last_name}>'

class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    houses = db.relationship("House", backref="tenant")
    reviews = db.relationship("Review", backref="tenant")
    
    def __repr__(self):
        return f'<Tenant: {self.first_name} {self.last_name}>'

class House(db.Model, SerializerMixin):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    categories = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
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
        return f'<Review: {self.reviews}>'

class Owner_Tenant(db.Model, SerializerMixin):
    __tablename__ = 'owners_tenants'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"))
    
    def __repr__(self):
        return f'<Owner_Tenant: {self.id} tenant: {self.tenant_id} owner: {self.owner_id}>'

class Tenant_House(db.Model, SerializerMixin):
    __tablename__ = 'tenants_houses'
    id = db.Column(db.Integer, primary_key=True)
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"))
    house_id = db.Column(db.Integer, db.ForeignKey("houses.id"))
    
    def __repr__(self):
        return f'<Tenant_House: {self.id} tenant_id={self.tenant_id} house: {self.house_id}>'
