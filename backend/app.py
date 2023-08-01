from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from config import Config
import jwt
import datetime
import logging
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

jwt_manager = JWTManager(app)


from models import User, Payment, Property, MoveAssistance, Review

login_parser = api.parser()
login_parser.add_argument('email', type=str, required=True, help='Email address', location='json')
login_parser.add_argument('password', type=str, required=True, help='Password', location='json')

app.config['SECRET_KEY'] = 'saka-keja-key'

user_model = api.model('User', {
    'id': fields.Integer(readonly=True, description='The user identifier'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'phone_number': fields.String(required=True, description='Phone number'),
    'user_type': fields.String(required=True, description='User type'),
})

property_model = api.model('Property', {
    'id': fields.Integer(readonly=True, description='The property identifier'),
    'owner_id': fields.Integer(required=True, description='Owner ID'),
    'number_of_rooms': fields.Integer(required=True, description='Number of rooms'),
    'categories': fields.String(required=True, description='Categories'),
    'location': fields.String(required=True, description='Location'),
    'price': fields.Float(required=True, description='Price'),
    'description': fields.String(required=True, description='Description'),
    'rating': fields.Float(required=True, description='Rating'),
    'image_urls': fields.List(fields.String, required=True, description='Image URLs'),
})

payment_model = api.model('Payment', {
    'id': fields.Integer(readonly=True, description='The payment identifier'),
    'amount': fields.Float(required=True, description='Amount'),
    'payment_date': fields.DateTime(required=True, description='Payment date'),
    'status': fields.String(required=True, description='Payment status'),
    'tenant_id': fields.Integer(required=True, description='Tenant ID'),
    'property_id': fields.Integer(required=True, description='Property ID'),
})

move_assistance_model = api.model('MoveAssistance', {
    'id': fields.Integer(readonly=True, description='The move assistance identifier'),
    'service_details': fields.String(required=True, description='Service details'),
    'status': fields.String(required=True, description='Move status'),
    'tenant_id': fields.Integer(required=True, description='Tenant ID'),
})

review_model = api.model('Review', {
    'id': fields.Integer(readonly=True, description='The review identifier'),
    'review_text': fields.String(required=True, description='Review text'),
    'rating': fields.Float(required=True, description='Rating'),
    'tenant_id': fields.Integer(required=True, description='Tenant ID'),
    'property_id': fields.Integer(required=True, description='Property ID'),
})

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
        return False, {"error": "Authorization token not provided"}

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        request.user_id = payload['user_id']
        request.user_type = payload['user_type']
    except jwt.ExpiredSignatureError:
        return False, {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return False, {"error": "Invalid token"}

    return True, None


@api.route('/login')
class Login(Resource):
    @api.doc(description='User login and token generation', parser=login_parser)
    def post(self):
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
            token = create_access_token(identity=user.id)
            print(f" token: {token}")
            

            return make_response(jsonify({user.user_type: token}), 200)
    
        print(f"Successful login for user with email: {email}, id: {user.id}")

        token = create_access_token(identity=user.id)

        return make_response(jsonify({"token": token}), 200)


@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    @api.doc(description='Protected resource that requires authentication')
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        return make_response(jsonify({"user": user.to_dict()}), 200)


class IndexResource(Resource):
    def get(self):
        return {'message': 'Karibu sakakeja'}

api.add_resource(IndexResource, '/')

DEFAULT_PAGE_SIZE = 10

@api.route('/users')
class Users(Resource):
    @api.doc(description='Get a list of all users')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', DEFAULT_PAGE_SIZE))

        offset = (page - 1) * per_page

        users = User.query.offset(offset).limit(per_page).all()

        total_items = User.query.count()
        total_pages = (total_items + per_page - 1) // per_page

        response = {
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages,
            'data': [user.to_dict() for user in users],
        }

        return make_response(jsonify(response), 200)

    @api.doc(description='Create a new user', body=user_model)
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

@api.route('/users/<int:id>')

class User_by_Id(Resource):
    @api.doc(description='Get a specific user by ID')
    def get(self, id):
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        response_dict = user.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    @api.doc(description='Update a specific user by ID', body=user_model)
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

    @api.doc(description='Delete a specific user by ID')
    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return make_response(jsonify({"error": "User not found"}), 404)

        db.session.delete(user)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

@api.route('/properties')
class Properties(Resource):
    @api.doc(description='Get a list of all properties')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', DEFAULT_PAGE_SIZE))

        offset = (page - 1) * per_page

        properties = Property.query.offset(offset).limit(per_page).all()

        total_items = Property.query.count()
        total_pages = (total_items + per_page - 1) // per_page

        response = {
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages,
            'data': [property.to_dict() for property in properties],
        }

        return make_response(jsonify(response), 200)

    @api.doc(description='Create a new property', body=property_model)
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

@api.route('/properties/<int:id>')
class Property_by_Id(Resource):
    @api.doc(description='Get a specific property by ID')
    def get(self, id):
        property = Property.query.get(id)
        if not property:
            return make_response(jsonify({"error": "Property not found"}), 404)

        response_dict = property.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response
    
    @api.doc(description='Update a specific property by ID', body=property_model)
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

    @api.doc(description='Delete a specific property by ID')
    def delete(self, id):
        property = Property.query.get(id)
        if not property:
            return make_response(jsonify({"error": "Property not found"}), 404)

        db.session.delete(property)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

@api.route('/payments')
class Payments(Resource):
    @api.doc(description='Get a list of all payments')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', DEFAULT_PAGE_SIZE))

        offset = (page - 1) * per_page

        payments = Payment.query.offset(offset).limit(per_page).all()

        total_items = Payment.query.count()
        total_pages = (total_items + per_page - 1) // per_page

        response = {
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages,
            'data': [payment.to_dict() for payment in payments],
        }

        return make_response(jsonify(response), 200)


    @api.doc(description='Create a new payment', body=payment_model)
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

@api.route('/payments/<int:id>')
class Payment_by_Id(Resource):
    @api.doc(description='Get a specific payment by ID')
    def get(self, id):
        payment = Payment.query.get(id)
        if not payment:
            return make_response(jsonify({"error": "Payment not found"}), 404)

        response_dict = payment.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    @api.doc(description='Update a specific payment by ID', body=payment_model)
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

    @api.doc(description='Delete a specific payment by ID')
    def delete(self, id):
        payment = Payment.query.get(id)
        if not payment:
            return make_response(jsonify({"error": "Payment not found"}), 404)

        db.session.delete(payment)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

@api.route('/move_assistances')
class MoveAssistances(Resource):
    @api.doc(description='Get a list of all move assistances')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', DEFAULT_PAGE_SIZE))

        offset = (page - 1) * per_page

        move_assistances = MoveAssistance.query.offset(offset).limit(per_page).all()

        total_items = MoveAssistance.query.count()
        total_pages = (total_items + per_page - 1) // per_page

        response = {
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages,
            'data': [move.to_dict() for move in move_assistances],
        }

        return make_response(jsonify(response), 200)
    
    @api.doc(description='Create a new move assistance', body=move_assistance_model)
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

@api.route('/move_assistances/<int:id>')
class MoveAssistance_by_Id(Resource):
    @api.doc(description='Get a specific move assistance by ID')
    def get(self, id):
        move = MoveAssistance.query.get(id)
        if not move:
            return make_response(jsonify({"error": "MoveAssistance not found"}), 404)

        response_dict = move.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    @api.doc(description='Update a specific move assistance by ID', body=move_assistance_model)
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

    @api.doc(description='Delete a specific move assistance by ID')
    def delete(self, id):
        move = MoveAssistance.query.get(id)
        if not move:
            return make_response(jsonify({"error": "MoveAssistance not found"}), 404)

        db.session.delete(move)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response

@api.route('/reviews')
class Reviews(Resource):
    @api.doc(description='Get a list of all reviews')
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', DEFAULT_PAGE_SIZE))

        offset = (page - 1) * per_page

        reviews = Review.query.offset(offset).limit(per_page).all()

        total_items = Review.query.count()
        total_pages = (total_items + per_page - 1) // per_page

        response = {
            'page': page,
            'per_page': per_page,
            'total_items': total_items,
            'total_pages': total_pages,
            'data': [review.to_dict() for review in reviews],
        }

        return make_response(jsonify(response), 200)

    @api.doc(description='Create a new review', body=review_model)
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

# Route for getting, updating, and deleting a specific review by ID
@api.route('/reviews/<int:id>')
class Review_by_Id(Resource):
    @api.doc(description='Get a specific review by ID')
    def get(self, id):
        review = Review.query.get(id)
        if not review:
            return make_response(jsonify({"error": "Review not found"}), 404)

        response_dict = review.to_dict()
        response = make_response(jsonify(response_dict), 200)

        return response

    @api.doc(description='Update a specific review by ID', body=review_model)
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

    @api.doc(description='Delete a specific review by ID')
    def delete(self, id):
        review = Review.query.get(id)
        if not review:
            return make_response(jsonify({"error": "Review not found"}), 404)

        db.session.delete(review)
        db.session.commit()

        response_dict = {"message": "Deleted successfully"}
        response = make_response(jsonify(response_dict), 200)

        return response


if __name__ == '__main__':
    app.run(debug=True)