from flask import Blueprint
from michelin.views import api_route


api_michelin_bp = Blueprint('michelin_api', __name__, template_folder='templates', static_folder='static')

