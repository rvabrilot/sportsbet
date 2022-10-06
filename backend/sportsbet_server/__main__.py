#!/usr/bin/env python3

import connexion

from sportsbet_server.config import connexion_app

def main():  
    
    connexion_app.add_api('sportsbet_server.yaml',
     arguments={'title': 'SportsBet Backend 0.1.1'}, 
     pythonic_params=True,
     options = {"swagger_ui": True})

    connexion_app.run(port=8080)


if __name__ == '__main__':
    main()
