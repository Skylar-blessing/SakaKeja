from flask import Flask, jsonify, make_response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from config import Config
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    from models import House, Tenant, Owner, Tenant_House, Owner_Tenant, Review

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    
    class Index(Resource):
        def get(self):
            response_dict = {
                "message": "Karibu kenya"
            }
            response = make_response(jsonify(response_dict), 200)

            return response

    api.add_resource(Index, "/")

    class Owners(Resource):
        def get(self):
            owners = [owner.to_dict() for owner in Owner.query.all()]
            return make_response(jsonify(owners), 200)

        def post(self):
            new_owner = Owner(
                id=request.form['id'],
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                phone_number=request.form['phone_number'],
                password=request.form['password']
            )
            db.session.add(new_owner)
            db.session.commit()

            response_dict = new_owner.to_dict()
            response = make_response(jsonify(response_dict), 201)

            return response

    api.add_resource(Owners, "/owners")
    print("Registering Owners resource")

    class Owner_by_Id(Resource):
        def get(self, id):
            response_dict = Owner.query.filter_by(id=id).first().to_dict()
            response = make_response(response_dict, 200)

            return response

        def patch(self, id):
            updated_one = Owner.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(updated_one, attr, request.form[attr])

            db.session.add(updated_one)
            db.session.commit()

            response_dict = updated_one.to_dict()
            response = make_response(response_dict, 200)

            return response

        def delete(self, id):
            selected_one = Owner.query.filter_by(id=id).first()

            db.session.delete(selected_one)
            db.session.commit()

            response_dict = {"message": "Deleted successfully"}
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response

    api.add_resource(Owner_by_Id, "/owners/<int:id>")
    
    
    
    class Tenants(Resource):
        def get(self):
            tenants = [tenant.to_dict() for tenant in Tenant.query.all()]
            return make_response(jsonify(tenants), 200)

        def post(self):
            new_tenant = Tenant(
                id=request.form['id'],
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                phone_number=request.form['phone_number'],
                password=request.form['password']
            )
            db.session.add(new_tenant)
            db.session.commit()

            response_dict = new_tenant.to_dict()
            response = make_response(jsonify(response_dict), 201)

            return response

    api.add_resource(Tenants, "/tenants")
    print("Registering Tenants resource")

    class Tenant_by_Id(Resource):
        def get(self, id):
            response_dict = Tenant.query.filter_by(id=id).first().to_dict()
            response = make_response(response_dict, 200)

            return response

        def patch(self, id):
            updated_one = Tenant.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(updated_one, attr, request.form[attr])

            db.session.add(updated_one)
            db.session.commit()

            response_dict = updated_one.to_dict()
            response = make_response(response_dict, 200)

            return response

        def delete(self, id):
            selected_one = Tenant.query.filter_by(id=id).first()

            db.session.delete(selected_one)
            db.session.commit()

            response_dict = {"message": "Deleted successfully"}
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response

    api.add_resource(Tenant_by_Id, "/tenants/<int:id>")
    
    
    class Houses(Resource):
        def get(self):
            houses = [house.to_dict() for house in House.query.all()]
            return make_response(jsonify(houses), 200)

        def post(self):
            new_house = House(
                id=request.form['id'],
                number_of_rooms=request.form['number_of_rooms'],
                categories=request.form['categories'],
                location=request.form['location'],
                price=request.form['price'],
                description=request.form['description'],
                rating=request.form['rating'],
                image_urls=request.form['image_urls']
            )
            db.session.add(new_house)
            db.session.commit()

            response_dict = new_house.to_dict()
            response = make_response(jsonify(response_dict), 201)

            return response

    api.add_resource(Houses, "/houses")
    print("Registering Houses resource")

    class House_by_Id(Resource):
        def get(self, id):
            response_dict = House.query.filter_by(id=id).first().to_dict()
            response = make_response(response_dict, 200)

            return response

        def patch(self, id):
            updated_one = House.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(updated_one, attr, request.form[attr])

            db.session.add(updated_one)
            db.session.commit()

            response_dict = updated_one.to_dict()
            response = make_response(response_dict, 200)

            return response

        def delete(self, id):
            selected_one = House.query.filter_by(id=id).first()

            db.session.delete(selected_one)
            db.session.commit()

            response_dict = {"message": "Deleted successfully"}
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response

    api.add_resource(House_by_Id, "/houses/<int:id>")
    
    
    class Reviews(Resource):
        def get(self):
            reviews = [review.to_dict() for review in Review.query.all()]
            return make_response(jsonify(reviews), 200)

        def post(self):
            new_review = Review(
                id=request.form['id'],
                reviews=request.form['reviews'],
                tenant_id=request.form['tenant_id'],    
                house_id=request.form['house_id']
                
            )
            db.session.add(new_review)
            db.session.commit()

            response_dict = new_review.to_dict()
            response = make_response(jsonify(response_dict), 201)

            return response

    api.add_resource(Reviews, "/reviews")
    print("Registering Reviews resource")

    class Review_by_Id(Resource):
        def get(self, id):
            response_dict = Review.query.filter_by(id=id).first().to_dict()
            response = make_response(response_dict, 200)

            return response

        def patch(self, id):
            updated_one = Review.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(updated_one, attr, request.form[attr])

            db.session.add(updated_one)
            db.session.commit()

            response_dict = updated_one.to_dict()
            response = make_response(response_dict, 200)

            return response

        def delete(self, id):
            selected_one = Review.query.filter_by(id=id).first()

            db.session.delete(selected_one)
            db.session.commit()

            response_dict = {"message": "Deleted successfully"}
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response

    api.add_resource(Review_by_Id, "/reviews/<int:id>")

    class Owners_Tenants(Resource):
        def get(self):
            owners_tenants = [owner_tenant.to_dict() for owner_tenant in Owner_Tenant.query.all()]
            return make_response(jsonify(owners_tenants), 200)

        def post(self):
            new_owner_tenant = Owner_Tenant(
                id=request.form['id'],
                owner_id=request.form['owner_id'],
                tenant_id=request.form['tenant_id'] 
            )
            db.session.add(new_owner_tenant)
            db.session.commit()

            response_dict = new_owner_tenant.to_dict()
            response = make_response(jsonify(response_dict), 201)

            return response

    api.add_resource(Owners_Tenants, "/owners_tenants")
    print("Registering Reviews resource")

    class Owner_Tenant_by_Id(Resource):
        def get(self, id):
            response_dict = Owner_Tenant.query.filter_by(id=id).first().to_dict()
            response = make_response(response_dict, 200)

            return response

        def patch(self, id):
            updated_one = Owner_Tenant.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(updated_one, attr, request.form[attr])

            db.session.add(updated_one)
            db.session.commit()

            response_dict = updated_one.to_dict()
            response = make_response(response_dict, 200)

            return response

        def delete(self, id):
            selected_one = Owner_Tenant.query.filter_by(id=id).first()

            db.session.delete(selected_one)
            db.session.commit()

            response_dict = {"message": "Deleted successfully"}
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response

    api.add_resource(Owner_Tenant_by_Id, "/owners_tenants/<int:id>")
    
    class Tenants_Houses(Resource):
        def get(self):
            tenants_houses = [tenant_house.to_dict() for tenant_house in Tenant_House.query.all()]
            return make_response(jsonify(tenants_houses), 200)

        def post(self):
            new_tenant_house = Tenant_House(
                id=request.form['id'],
                house_id=request.form['house_id'],
                tenant_id=request.form['tenant_id'] 
            )
            db.session.add(new_tenant_house)
            db.session.commit()

            response_dict = new_tenant_house.to_dict()
            response = make_response(jsonify(response_dict), 201)

            return response

    api.add_resource(Tenants_Houses, "/tenants_houses")
    print("Registering Tenants_Houses resource")

    class Tenant_House_by_Id(Resource):
        def get(self, id):
            response_dict = Tenant_House.query.filter_by(id=id).first().to_dict()
            response = make_response(response_dict, 200)

            return response

        def patch(self, id):
            updated_one = Tenant_House.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(updated_one, attr, request.form[attr])

            db.session.add(updated_one)
            db.session.commit()

            response_dict = updated_one.to_dict()
            response = make_response(response_dict, 200)

            return response

        def delete(self, id):
            selected_one = Tenant_House.query.filter_by(id=id).first()

            db.session.delete(selected_one)
            db.session.commit()

            response_dict = {"message": "Deleted successfully"}
            response = make_response(
                jsonify(response_dict),
                200
            )
            return response

    api.add_resource(Tenant_House_by_Id, "/tenants_houses/<int:id>")
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


