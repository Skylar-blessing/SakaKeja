import random
import string
from faker import Faker
from app import app, db
from models import User, Property, Payment, MoveAssistance, Review

fake = Faker()

def generate_random_password():
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        if any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in string.punctuation for char in password):
            return password


def seed_users():
    for _ in range(70):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.phone_number()
        password = generate_random_password()
        user_type = random.choice(['owner', 'tenant', 'admin'])[:20]  
        user = User(first_name=first_name, last_name=last_name, email=email,
                    phone_number=phone_number, password=password, user_type=user_type)
        db.session.add(user)
    db.session.commit()

def seed_properties():
    users = User.query.all()
    for _ in range(60):
        owner = random.choice(users)
        number_of_rooms = fake.random_int(min=1, max=10)
        categories = ' '.join(fake.words(nb=3))
        location = fake.address()
        price = fake.random_int(min=500, max=5000)
        description = fake.paragraph()
        rating = round(random.uniform(1.0, 5.0), 1)
        image_urls = [fake.image_url() for _ in range(3)]
        property = Property(owner=owner, number_of_rooms=number_of_rooms, categories=categories,
                            location=location, price=price, description=description,
                            rating=rating, image_urls=image_urls)
        db.session.add(property)
    db.session.commit()

def seed_payments():
    users = User.query.filter_by(user_type='tenant').all()
    properties = Property.query.all()
    for _ in range(50):
        tenant = random.choice(users)
        property = random.choice(properties)
        amount = fake.random_int(min=100, max=1000)
        payment_date = fake.date_between(start_date='-1y', end_date='today')
        status = random.choice(['paid', 'pending', 'failed'])
        payment = Payment(tenant=tenant, property=property, amount=amount,
                          payment_date=payment_date, status=status)
        db.session.add(payment)
    db.session.commit()

def seed_move_assistance():
    users = User.query.filter_by(user_type='tenant').all()
    for _ in range(5):
        tenant = random.choice(users)
        service_details = fake.text(max_nb_chars=200)
        status = random.choice(['requested', 'in_progress', 'completed'])
        move_assistance = MoveAssistance(tenant=tenant, service_details=service_details, status=status)
        db.session.add(move_assistance)
    db.session.commit()

def seed_reviews():
    users = User.query.filter_by(user_type='tenant').all()
    properties = Property.query.all()
    for _ in range(70):
        tenant = random.choice(users)
        property = random.choice(properties)
        review_text = fake.paragraph()
        rating = random.randint(1, 5)
        review = Review(tenant=tenant, property=property, review_text=review_text, rating=rating)
        db.session.add(review)
    db.session.commit()

def seed_all():
    seed_users()
    seed_properties()
    seed_payments()
    seed_move_assistance()
    seed_reviews()

if __name__ == '__main__':
    with app.app_context():
        seed_all()
