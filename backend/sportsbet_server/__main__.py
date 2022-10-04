#!/usr/bin/env python3

import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


#from sportsbet_server import encoder


def main():
    connexion_app = connexion.App(__name__, specification_dir='./openapi/')
    flask_app = connexion_app.app
    flask_app.config['SQLAlCHEMY_ECHO'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rvera:123@localhost:3660/sportbet'
    flask_app.config['SQLALACHEMY_TRACK_MODIFICATIONS'] = False

    database = SQLAlchemy(flask_app)
    marshmallow = Marshmallow(flask_app)

    connexion_app.add_api('sportsbet_server.yaml',
     arguments={'title': 'SportsBet Backend 0.1.1'}, 
     pythonic_params=True,
     options = {"swagger_ui": True})

    connexion_app.run(port=8080)


if __name__ == '__main__':
    main()
