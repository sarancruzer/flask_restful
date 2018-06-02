#!flask/bin/python

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal

from flask_sqlalchemy import SQLAlchemy
import resources
from datetime import timedelta
from flask_jwt_extended import JWTManager

from shared.db import db
import models
from resources import userResources
from shared.route import init_routes


app = Flask(__name__, static_url_path="")
api = Api(app)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/aianr'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)


@app.before_first_request
def create_tables():
    db.create_all()

@app.before_request
def make_session_permanent():
    app.permanent_session_lifetime = timedelta(minutes=1)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)


app.config['JWT_BLACKLIST_ENABLED'] = False
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)
    
with app.app_context():
    db.init_app(app)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


init_routes(api)


if __name__ == '__main__':
    app.run(debug=True)
