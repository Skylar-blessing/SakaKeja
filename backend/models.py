from sqlalchemy_serializer import SerializerMixin
from app import db
from sqlalchemy.orm import validates
import re
from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(50))
    password = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)

    properties_owned = db.relationship("Property", backref="owner", lazy="select")
    payments_made = db.relationship("Payment", backref="tenant", lazy="select")
    move_assistance_requests = db.relationship("MoveAssistance", backref="tenant", lazy="select")
    reviews_written = db.relationship("Review", backref="tenant", lazy="select")

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'password': self.password,
            'user_type': self.user_type
        }

    def __repr__(self):
        return f'<User: {self.first_name} {self.last_name}>'
    
    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter.")

        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit.")

        if not any(char in '!@#$%^&*()-=_+[]{}|;:,.<>?' for char in password):
            raise ValueError("Password must contain at least one special character.")

        return True

    @classmethod
    def create(cls, first_name, last_name, email, phone_number, password, user_type):
        if not cls.validate_password(password):
            raise ValueError("Invalid password format")

        hashed_password = generate_password_hash(password)
        print(f"Hashed password: {hashed_password}") 

        new_user = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=hashed_password,
            user_type=user_type
        )
        db.session.add(new_user)
        db.session.commit()

        return new_user

class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    number_of_rooms = db.Column(db.Integer)
    categories = db.Column(db.String)
    location = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    image_urls = db.Column(db.ARRAY(db.String))

    payments_received = db.relationship("Payment", backref="property", lazy="select")
    reviews_received = db.relationship("Review", backref="property", lazy="select")

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'number_of_rooms': self.number_of_rooms,
            'categories': self.categories,
            'location': self.location,
            'price': self.price,
            'description': self.description,
            'rating': self.rating,
            'image_urls': self.image_urls,
        }

    def __repr__(self):
        return f'<Property: {self.number_of_rooms} {self.description}>'

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    payment_date = db.Column(db.Date)
    status = db.Column(db.String(20)) 
    
    tenant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'payment_date': str(self.payment_date),  
            'status': self.status,
            'tenant_id': self.tenant_id,
            'property_id': self.property_id,
        }

    def __repr__(self):
        return f'<Payment: {self.id}>'

class MoveAssistance(db.Model, SerializerMixin):
    __tablename__ = 'move_assistance'
    id = db.Column(db.Integer, primary_key=True)
    service_details = db.Column(db.String)
    status = db.Column(db.String(20))
    
    tenant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'service_details': self.service_details,
            'status': self.status,
            'tenant_id': self.tenant_id,
        }

    def __repr__(self):
        return f'<MoveAssistance: {self.id}>'

class Review(db.Model, SerializerMixin): 
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String)
    rating = db.Column(db.Integer)
    
    tenant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'review_text': self.review_text,
            'rating': self.rating,
            'tenant_id': self.tenant_id,
            'property_id': self.property_id,
        }

    def __repr__(self):
        return f'<Review: {self.id}>'