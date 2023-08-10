from flask import Flask, jsonify, make_response, request, g, url_for
import os
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api, Resource, fields, reqparse, Namespace
from flask_cors import CORS
from config import Config
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token
from werkzeug.security import check_password_hash, generate_password_hash
import cloudinary
import cloudinary.uploader
from flask_mail import Mail, Message
from secrets import token_urlsafe
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest
import secrets

client_id = os.environ.get('PAYPAL_CLIENT_ID')
client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

cloudinary.config(
    cloud_name=Config.CLOUDINARY_CLOUD_NAME,
    api_key=Config.CLOUDINARY_API_KEY,
    api_secret=Config.CLOUDINARY_API_SECRET
)


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

jwt_manager = JWTManager(app)

mail = Mail(app)

from models import User, Payment, Property, MoveAssistance, Review

app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)

def send_verification_email(user_email, token):
    verification_link = url_for('email_verify_email', token=token, _external=True)

    subject = 'Please verify your email'
    body = f'Click the following link to verify your email: {verification_link}'
    sender = app.config['MAIL_DEFAULT_SENDER']
    recipients = [user_email]

    message = Message(subject=subject, body=body, sender=sender, recipients=recipients)
    mail.send(message)

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
    access_payload = {
        'sub': user_id,
        'user_id': user_id,
        'user_type': user_type,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    access_token = create_access_token(identity=access_payload)

    refresh_payload = {
        'sub': user_id,
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=30)
    }
    refresh_token = create_refresh_token(identity=refresh_payload)

    return access_token, refresh_token

def verify_token():
    access_token = request.headers.get('Authorization')

    if not access_token:
        return False, {"error": "Authorization token not provided"}

    try:
        access_payload = jwt.decode(access_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        g.user_id = access_payload['user_id']
        g.user_type = access_payload['user_type']
    except jwt.ExpiredSignatureError:
        return False, {"error": "Access token has expired"}
    except jwt.InvalidTokenError:
        return False, {"error": "Invalid access token"}

    return True, None


def user_type_required(required_types):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            current_user_type = get_jwt_identity()['user_type']
            if current_user_type not in required_types:
                return make_response(jsonify({"error": "You are not authorized to access this resource"}), 403)
            return fn(*args, **kwargs)
        return wrapper
    return decorator

def get_owner_phone_number(owner_id):
    user = User.query.filter_by(id=owner_id).first()
    if user:
        owner_phone_number = user.phone_number
        return owner_phone_number
    else:
        return None


login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, required=True, help='Email address')
login_parser.add_argument('password', type=str, required=True, help='Password')

email_namespace = Namespace('email', description='Email verification related operations')
@email_namespace.route('/verify_email/<token>', methods=['GET'])
class RefreshToken(Resource):
    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return jsonify({"error": "User not found"}), 404

        user_type = user.user_type

        access_token, refresh_token = create_token(user_id, user_type)
        return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

class VerifyEmail(Resource):
    def get(self, token):
        user = User.query.filter_by(verification_token=token).first()
        if user:
            user.email_verified = True
            db.session.commit()
            return 'Email verified successfully!'
        return 'Email verification failed!'

email_namespace = api.namespace('email', description='Email verification related operations')
email_namespace.add_resource(VerifyEmail, '/verify_email/<token>')

email_namespace.add_resource(RefreshToken, '/refresh_token')

@api.route('/login')
class Login(Resource):
    @api.doc(description='User login and token generation', parser=login_parser)
    def post(self):
        data = login_parser.parse_args()
        email = data['email']
        password = data['password']

        print(f"Received login request for email: {email}")

        user = User.query.filter_by(email=email).first()

        if user is None or not check_password_hash(user.password, password):
            print(f"Invalid email or password for user with email: {email}")
            return make_response(jsonify({"error": "Invalid email or password"}), 401)

        if not user.email_verified:
            print(f"User with email {email} tried to log in without verifying email.")
            return make_response(jsonify({"error": "Please verify your email first."}), 401)

        print(f"Successful login")
        access_token, refresh_token = create_token(user.id, user.user_type)
        return make_response(jsonify({
            "user_id": user.id,
            user.user_type: access_token,
            "refresh_token": refresh_token
        }), 200)
    
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

DEFAULT_PAGE_SIZE = 12

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
        verification_token = token_urlsafe(32)

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print("Email already exists")
            return make_response(jsonify({"error": "Email already exists"}), 400)

        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=email,
            phone_number=data['phone_number'],
            password=generate_password_hash(data['password']),
            user_type=data['user_type'],
            verification_token=verification_token
        )

        db.session.add(new_user)
        db.session.commit()

        send_verification_email(new_user.email, new_user.verification_token)

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
    @jwt_required()
    @user_type_required(['owner', 'admin'])
    def post(self):
        data = request.get_json()
        
        image_urls = []
        if 'image_urls' in data and isinstance(data['image_urls'], list):
            for image_url in data['image_urls']:
                uploaded_image = cloudinary.uploader.upload(image_url)
                image_urls.append(uploaded_image['secure_url'])
        
        new_property = Property(
            owner_id=data['owner_id'],
            number_of_rooms=data['number_of_rooms'],
            categories=data['categories'],
            location=data['location'],
            price=data['price'],
            description=data['description'],
            rating=data['rating'],
            image_urls=image_urls
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
    @jwt_required()
    @user_type_required(['tenant', 'admin'])
    def post(self):
        data = api.payload
        amount = data['amount']
        payment_date = data['payment_date']
        status = data['status']
        tenant_id = data['tenant_id']
        property_id = data['property_id']

        owner_phone_number = get_owner_phone_number(property_id)

        client_id = os.environ.get('PAYPAL_CLIENT_ID')
        client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')
        environment = SandboxEnvironment(client_id, client_secret)
        client = PayPalHttpClient(environment)

        request = OrdersCreateRequest()
        request.prefer('return=representation')
        request.request_body({
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": "USD",
                    "value": amount
                }
            }],
            "application_context": {
                "return_url": "https://your-redirect-url.com/success",
                "cancel_url": "https://your-redirect-url.com/cancel"
            }
        })

        try:
            response = client.execute(request)
            order_id = response.result.id

            new_payment = Payment(
                amount=amount,
                payment_date=payment_date,
                status=status,
                tenant_id=tenant_id,
                property_id=property_id
            )
            db.session.add(new_payment)
            db.session.commit()
            response_dict = {
                "order_id": order_id,
                "owner_phone_number": owner_phone_number,
                "amount": amount,
            }
            return make_response(jsonify(response_dict), 201)

        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
    
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

        image_url = ""
        if 'image' in data:
            uploaded_image = cloudinary.uploader.upload(data['image'])
            image_url = uploaded_image['secure_url']

        new_move = MoveAssistance(
            service_details=data['service_details'],
            image=image_url,
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
    @jwt_required()
    @user_type_required(['tenant', 'admin'])
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