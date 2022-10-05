#!/usr/bin/env python3

import connexion


def main():
    connexion_app = connexion.App(__name__, specification_dir='./openapi/')

    connexion_app.add_api('sportsbet_server.yaml',
     arguments={'title': 'SportsBet Backend 0.1.1'}, 
     pythonic_params=True,
     options = {"swagger_ui": True})

    connexion_app.run(port=8080)


if __name__ == '__main__':
    main()
