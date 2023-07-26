import random
from flask import Flask
from app import db, create_app
from models import Owner, Tenant, House, Review, Owner_Tenant, Tenant_House
app = create_app()

def create_owners(num_owners):
    for i in range(num_owners):
        first_name = f'OwnerFirstName{i}'
        last_name = f'OwnerLastName{i}'
        email = f'owner{i}_{random.randint(1000, 9999)}@example.com'  
        phone_number = f'001-234-567-890{i:02d}'
        password = f'password{i}'
        
        owner = Owner(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )
        db.session.add(owner)
    db.session.commit()

def create_tenants(num_tenants):
    for i in range(num_tenants):
        first_name = f'TenantFirstName{i}'
        last_name = f'TenantLastName{i}'
        email = f'tenant{i}_{random.randint(1000, 9999)}@example.com'  
        phone_number = f'001-987-654-321{i:02d}'
        password = f'password{i}'
        
        tenant = Tenant(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )
        db.session.add(tenant)
    db.session.commit()

def create_houses(num_houses):
    for i in range(num_houses):
        number_of_rooms = random.randint(1, 5)
        categories = random.choice(['Apartment', 'Condo', 'House'])
        location = f'Location{i}'
        price = random.randint(500, 5000)
        description = f'Description for House {i}'
        rating = random.uniform(1, 5)
        image_urls = [
            f'https://example.com/image{i}_1.jpg',
            f'https://example.com/image{i}_2.jpg',
            f'https://example.com/image{i}_3.jpg'
        ]
        
        house = House(
            number_of_rooms=number_of_rooms,
            categories=categories,
            location=location,
            price=price,
            description=description,
            rating=rating,
            image_urls=image_urls
        )
        db.session.add(house)
    db.session.commit()

def create_reviews(num_reviews):
    tenants = Tenant.query.all()
    houses = House.query.all()
    
    for i in range(num_reviews):
        tenant = random.choice(tenants)
        house = random.choice(houses)
        review_text = f'Review {i} for House {house.id} by Tenant {tenant.id}'
        
        review = Review(
            reviews=review_text,
            house=house,
            tenant=tenant
        )
        db.session.add(review)
    db.session.commit()

def create_owner_tenant_relations():
    owners = Owner.query.all()
    tenants = Tenant.query.all()
    
    for owner in owners:
        tenant = random.choice(tenants)
        
        owner_tenant_relation = Owner_Tenant(
            owner_id=owner.id, 
            tenant_id=tenant.id  
        )
        db.session.add(owner_tenant_relation)
    db.session.commit()

def create_tenant_house_relations():
    tenants = Tenant.query.all()
    houses = House.query.all()
    
    for tenant in tenants:
        house = random.choice(houses)
        
        tenant_house_relation = Tenant_House(
            tenant_id=tenant.id,  
            house_id=house.id  
        )
        db.session.add(tenant_house_relation)
    db.session.commit()

def initialize_database():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    initialize_database()
    
    with app.app_context():
        num_owners = 10
        num_tenants = 10
        num_houses = 10
        num_reviews = 10

        create_owners(num_owners)
        create_tenants(num_tenants)
        create_houses(num_houses)
        create_reviews(num_reviews)
        create_owner_tenant_relations()
        create_tenant_house_relations()
        