"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
import hashlib
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

    @api.route('/token', methods=['POST'])
    def create_token():

        email=request.json.get('email', None)
        email=request.json.get('password', None)
        access_token=create_access_token(identity=email)
        
        return jsonify(access_token=access_token)

    @api.route('/login', methods=['POST'])
    def login():

        body=request.get_json(force=True)
        email=body['email']
        password=hashlib.sha256(body['password'].encode('utf-8')).hexdigest()

        new_user=User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        access_token=create_access_token(identity=email)
        
        return jsonify(access_token=access_token)




