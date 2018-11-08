# FLEXCoop authentication server
This server uses openId connect implementation to allow the authentication of users in the FLEXCoop Components.

The server is based on '''django_oidc_provider''' package, with some minor modifications and customizations.

## Install

1. Create a virtualenv in python3
'''bash
virtualenv -p python3 venv
'''
2. Install requirements
'''bash
source venv/bin/activate
pip install -r requirements.txt
'''
3. Run the server
'''bash
python manage.py runserver
'''

## Usage
For demo purposes only, the project comes with an allready working sqlite database, this database contains 2 different users and 2 clients. Below is the information of them.

To manage users and clients, log-in as admin into the '/admin' service.

### User 1
Username: admin
Password: admin1234
Role: aggregator
### User2
Username: eloi
Password: eloi1234
Role: prosumer

### Client1
Name: Anonimized Client
ClientId: 209831
Scope: openid role flexId
redirect uri: 127.0.0.1:3000
### Client2
Name: Private Client
ClientId: 043323
Scope: openid flexId role profile email
redirect uri: 127.0.0.1:3001

