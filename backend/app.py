from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from config import Config
import jwt
import datetime
import logging
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from models import User, Payment, Property, MoveAssistance, Review

app.config['SECRET_KEY'] = 'saka-keja-key'

def create_token(user_id, user_type):
    payload = {
        'user_id': user_id,
        'user_type': user_type,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1) 
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def verify_token():
    token = request.headers.get('Authorization')

    if not token:
        return make_response(jsonify({"error": "Authorization token not provided"}), 401)

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        request.user_id = payload['user_id']
        request.user_type = payload['user_type']
    except jwt.ExpiredSignatureError:
        return make_response(jsonify({"error": "Token has expired"}), 401)
    except jwt.InvalidTokenError:
        return make_response(jsonify({"error": "Invalid token"}), 401)

    return None

class IndexResource(Resource):
    def get(self):
        return {'message': 'Karibu sakakeja'}

api.add_resource(IndexResource, '/')

class Login(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        email = data['email']
        password = data['password']

        print(f"Received login request for email: {email}")

        user = User.query.filter_by(email=email).first()

        if user is None:
            print(f"No user found with email: {email}")
            return make_response(jsonify({"error": "Invalid email or password"}), 401)

        print(f"Found user with email: {email}, id: {user.id}")

        try:
            User.validate_password(password)
        except ValueError as e:
            print(f"Invalid password format for user with email: {email}, id: {user.id}")
            return make_response(jsonify({"error": str(e)}), 401)

        if not check_password_hash(user.password, password):
            print(f"Invalid password for user with email: {email}, id: {user.id}")
            return make_response(jsonify({"error": "Invalid email or password"}), 401)

        print(f"Successful login for user with email: {email}, id: {user.id}")

        token = create_token(user.id, user.user_type)

        return make_response(jsonify({"token": token}), 200)

api.add_resource(Login, "/login")

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

    def post(self):
        data = request.get_json()
        email = data['email']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return make_response(jsonify({"error": "Email already exists"}), 400)

        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=email,
            phone_number=data['phone_number'],
            password=data['password'],
            user_type=data['user_type']
        )

        hashed_password = generate_password_hash(data['password'])
        print(f"Hashed password: {hashed_password}")

        db.session.add(new_user)
        db.session.commit()

        response_dict = new_user.to_dict()
        response = make_response(jsonify(response_dict), 201)

        return response
api.add_resource(Users, "/users")

class User_by_Id(Resource):
    def get(self, id):
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        response_dict = user.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def patch(self, id):
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        data = request.get_json()
        for attr, value in data.items():
            setattr(user, attr, value)

        db.session.commit()
        response_dict = user.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        db.session.delete(user)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

api.add_resource(User_by_Id, "/users/<int:id>")

class Properties(Resource):
    def get(self):
        properties = [property.to_dict() for property in Property.query.all()]
        return make_response(jsonify(properties), 200)

    def post(self):
        data = request.get_json()
        new_property = Property(
            owner_id=data['owner_id'],
            number_of_rooms=data['number_of_rooms'],
            categories=data['categories'],
            location=data['location'],
            price=data['price'],
            description=data['description'],
            rating=data['rating'],
            image_urls=data['image_urls']
        )
        db.session.add(new_property)
        db.session.commit()

        response_dict = new_property.to_dict()
        response = make_response(jsonify(response_dict), 201)

        return response

api.add_resource(Properties, "/properties")

class Property_by_Id(Resource):
    def get(self, id):
        property = Property.query.get(id)
        if not property:
            return make_response(jsonify({"error": "Property not found"}), 404)

        response_dict = property.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def patch(self, id):
        property = Property.query.get(id)
        if not property:
            return make_response(jsonify({"error": "Property not found"}), 404)

        data = request.get_json()
        for attr, value in data.items():
            setattr(property, attr, value)

        db.session.commit()
        response_dict = property.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def delete(self, id):
        property = Property.query.get(id)
        if not property:
            return make_response(jsonify({"error": "Property not found"}), 404)

        db.session.delete(property)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

api.add_resource(Property_by_Id, "/properties/<int:id>")

class Payments(Resource):
    def get(self):
        payments = [payment.to_dict() for payment in Payment.query.all()]
        return make_response(jsonify(payments), 200)

    def post(self):
        data = request.get_json()
        new_payment = Payment(
            amount=data['amount'],
            payment_date=data['payment_date'],
            status=data['status'],
            tenant_id=data['tenant_id'],
            property_id=data['property_id']
        )
        db.session.add(new_payment)
        db.session.commit()

        response_dict = new_payment.to_dict()
        response = make_response(jsonify(response_dict), 201)

        return response

api.add_resource(Payments, "/payments")

class Payment_by_Id(Resource):
    def get(self, id):
        payment = Payment.query.get(id)
        if not payment:
            return make_response(jsonify({"error": "Payment not found"}), 404)

        response_dict = payment.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def patch(self, id):
        payment = Payment.query.get(id)
        if not payment:
            return make_response(jsonify({"error": "Payment not found"}), 404)

        data = request.get_json()
        for attr, value in data.items():
            setattr(payment, attr, value)

        db.session.commit()
        response_dict = payment.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def delete(self, id):
        payment = Payment.query.get(id)
        if not payment:
            return make_response(jsonify({"error": "Payment not found"}), 404)

        db.session.delete(payment)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

api.add_resource(Payment_by_Id, "/payments/<int:id>")

class MoveAssistances(Resource):
    def get(self):
        move_assistances = [move.to_dict() for move in MoveAssistance.query.all()]
        return make_response(jsonify(move_assistances), 200)

    def post(self):
        data = request.get_json()
        new_move = MoveAssistance(
            service_details=data['service_details'],
            status=data['status'],
            tenant_id=data['tenant_id']
        )
        db.session.add(new_move)
        db.session.commit()

        response_dict = new_move.to_dict()
        response = make_response(jsonify(response_dict), 201)

        return response

api.add_resource(MoveAssistances, "/move_assistances")

class MoveAssistance_by_Id(Resource):
    def get(self, id):
        move = MoveAssistance.query.get(id)
        if not move:
            return make_response(jsonify({"error": "MoveAssistance not found"}), 404)

        response_dict = move.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def patch(self, id):
        move = MoveAssistance.query.get(id)
        if not move:
            return make_response(jsonify({"error": "MoveAssistance not found"}), 404)

        data = request.get_json()
        for attr, value in data.items():
            setattr(move, attr, value)

        db.session.commit()
        response_dict = move.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def delete(self, id):
        move = MoveAssistance.query.get(id)
        if not move:
            return make_response(jsonify({"error": "MoveAssistance not found"}), 404)

        db.session.delete(move)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

api.add_resource(MoveAssistance_by_Id, "/move_assistances/<int:id>")

class Reviews(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Review.query.all()]
        return make_response(jsonify(reviews), 200)

    def post(self):
        data = request.get_json()
        new_review = Review(
            review_text=data['review_text'],
            rating=data['rating'],
            tenant_id=data['tenant_id'],
            property_id=data['property_id']
        )
        db.session.add(new_review)
        db.session.commit()

        response_dict = new_review.to_dict()
        response = make_response(jsonify(response_dict), 201)

        return response

api.add_resource(Reviews, "/reviews")

class Review_by_Id(Resource):
    def get(self, id):
        review = Review.query.get(id)
        if not review:
            return make_response(jsonify({"error": "Review not found"}), 404)

        response_dict = review.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def patch(self, id):
        review = Review.query.get(id)
        if not review:
            return make_response(jsonify({"error": "Review not found"}), 404)

        data = request.get_json()
        for attr, value in data.items():
            setattr(review, attr, value)

        db.session.commit()
        response_dict = review.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    def delete(self, id):
        review = Review.query.get(id)
        if not review:
            return make_response(jsonify({"error": "Review not found"}), 404)

        db.session.delete(review)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

api.add_resource(Review_by_Id, "/reviews/<int:id>")


if __name__ == '__main__':
    app.run(debug=True)

