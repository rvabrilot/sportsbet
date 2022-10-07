import connexion
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Create the Connexion application instance
connexion_app = connexion.App(__name__, specification_dir='./openapi/')

# Get the underlying Flask app instance
flask_app = connexion_app.app

mysql_user = os.environ["MYSQL_USER"]
mysql_pass = os.environ["MYSQL_PASSWORD"]
mysql_db = os.environ["MYSQL_DATABASE"]
mysql_host = os.environ["MYSQL_HOST"]
sqlalchemy_uri = f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:3306/{mysql_db}?charset=utf8mb4&binary_prefix=true"

# Configure the SQLAlchemy part of the app instance
flask_app.config['SQLAlCHEMY_ECHO'] = True
flask_app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_uri
flask_app.config['SQLALACHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(flask_app)

# Initialize Marshmallow
ma = Marshmallow(flask_app)