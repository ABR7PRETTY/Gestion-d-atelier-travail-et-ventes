from flask import Flask
from flask_migrate import Migrate
from michelin import api_michelin_bp
from account import api_account_bp
from flask_cors import CORS
from extension import db, jwt

app = Flask(__name__)

CORS(app, origins="*")

app.register_blueprint(api_michelin_bp, url_prefix='/api/michelin')
app.register_blueprint(api_account_bp, url_prefix='/api/user')


app.config['SECRET_KEY'] = 'charm_secret'
app.config['BASE_TEMPLATE_FOLDER'] = 'charm/templates'
app.config['UPLOAD_FOLDER'] = 'static'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ABR7Kalou@localhost:3306/DocMichelin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'I M ABR7'  # Remplacez par votre clé secrète

# Initialiser JWTManager
jwt.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)
