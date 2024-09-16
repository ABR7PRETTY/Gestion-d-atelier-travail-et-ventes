from flask_jwt_extended import create_access_token, get_jwt_identity
from account.model.User import User
from flask import jsonify, request
from extension import db, bcrypt


class UserController:
    def __init__(self):
        self.user_model = User

    def register(self):
        data = request.get_json()
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(nom=data['nom'],prenom=data['prenom'],username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    def login(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity={'username': user.username})
            return jsonify(access_token=access_token), 200
        return jsonify({'message': 'Invalid credentials'}), 401

    def protected(self):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
