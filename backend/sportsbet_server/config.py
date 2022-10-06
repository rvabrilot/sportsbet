import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Create the Connexion application instance
connexion_app = connexion.App(__name__, specification_dir='./openapi/')

# Get the underlying Flask app instance
flask_app = connexion_app.app

# Configure the SQLAlchemy part of the app instance
flask_app.config['SQLAlCHEMY_ECHO'] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rvera:123@localhost:3306/sportbet?charset=utf8mb4&binary_prefix=true"'
flask_app.config['SQLALACHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(flask_app)

# Initialize Marshmallow
ma = Marshmallow(flask_app)