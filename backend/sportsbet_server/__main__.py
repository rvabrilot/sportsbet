#!/usr/bin/env python3

import connexion

#from sportsbet_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    #app.app.json = encoder.JSONEncoder
    app.add_api('sportsbet_server.yaml',
     arguments={'title': 'SportsBet Backend 0.1.1'}, 
     pythonic_params=True,
     options = {"swagger_ui": True})
    app.run(port=8080)


if __name__ == '__main__':
    main()
