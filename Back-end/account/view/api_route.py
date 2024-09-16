from account import api_account_bp
from account.controller.UserController import UserController

user_controller = UserController()


@api_account_bp.route('/register', methods=['POST'])
def add_user():
    return user_controller.register()


@api_account_bp.route('/login', methods=['POST'])
def log_user():
    return user_controller.login()


@api_account_bp.route('/protected', methods=['GET'])
def protected():
    return user_controller.protected()