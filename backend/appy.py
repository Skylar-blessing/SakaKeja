# from flask import Flask, jsonify, make_response, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_restful import Api, Resource
# from flask_cors import CORS
# from config import Config
# from sqlalchemy.exc import IntegrityError

# db = SQLAlchemy()
# migrate = Migrate()
# api = Api()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     CORS(app)

#     db.init_app(app)
#     migrate.init_app(app, db)
#     api.init_app(app)

#     # Import models here to avoid circular import
#     # from models import House, Tenant, Owner, Tenant_House, Owner_Tenant, Review

#     class Index(Resource):
#         def get(self):
#             response_dict = {
#                 "message": "Karibu saka keja mtaani"
#             }
#             response = make_response(jsonify(response_dict), 200)

#             return response

#     api.add_resource(Index, "/")

    # class Owners(Resource):
    #     def get(self):
    #         owners = [owner.to_dict() for owner in Owner.query.all()]
    #         return make_response(jsonify(owners), 200)

    #     def post(self):
    #         new_owner = Owner(
    #             id=request.form['id'],
    #             first_name=request.form['first_name'],
    #             last_name=request.form['last_name'],
    #             email=request.form['email'],
    #             phone_number=request.form['phone_number'],
    #             password=request.form['password']
    #         )
    #         db.session.add(new_owner)
    #         db.session.commit()

    #         response_dict = new_owner.to_dict()
    #         response = make_response(jsonify(response_dict), 201)

    #         return response

    # api.add_resource(Owners, "/owners")
    
    # print("Registering Owners resource")

    # class Owner_by_Id(Resource):
    #     def get(self, id):
    #         response_dict = Owner.query.filter_by(id=id).first().to_dict()
    #         response = make_response(response_dict, 200)

    #         return response

    #     def patch(self, id):
    #         updated_one = Owner.query.filter_by(id=id).first()
    #         for attr in request.form:
    #             setattr(updated_one, attr, request.form[attr])

    #         db.session.add(updated_one)
    #         db.session.commit()

    #         response_dict = updated_one.to_dict()
    #         response = make_response(response_dict, 200)

    #         return response

    #     def delete(self, id):
    #         selected_one = Owner.query.filter_by(id=id).first()

    #         db.session.delete(selected_one)
    #         db.session.commit()

    #         response_dict = {"message": "Deleted successfully"}
    #         response = make_response(
    #             jsonify(response_dict),
    #             200
    #         )
    #         return response

    # api.add_resource(Owner_by_Id, "/owners/<int:id>")

#     return app



# if __name__ == '__main__':
#     app.run()
    
    
