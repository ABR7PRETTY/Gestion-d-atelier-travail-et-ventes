from flask import Blueprint

api_account_bp = Blueprint('account_api', __name__, template_folder='templates', static_folder='static')

from account.view import api_route


