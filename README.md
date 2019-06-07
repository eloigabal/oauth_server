# FLEXCoop authentication server
This server uses openId connect implementation to allow the authentication of users in the FLEXCoop Components.

The server is based on [django_oidc_provider](https://github.com/juanifioren/django-oidc-provider) package, with some minor modifications and customizations.

## Install

1. Create a virtualenv in python3
```bash
virtualenv -p python3 venv
```

2. Install requirements
```bash
source venv/bin/activate
pip install -r requirements.txt
```

3. Create the environemnt variables
```bash
export DJANGO_SECRET_KEY=""
export DATABASE_NAME=""
export DATABASE_USER=""
export DATABASE_PASSWORD=""
export DATABASE_PORT=
export DATABASE_HOST=""
export OAUTH_SERVER_UUID=OAUTH_SERVER_UUID=""
export DJANGO_LOG_LEVEL=""
```

4. Collect Statics into `static/` folder
```bash
python3 manage.py collectstatic --no-input
```

5. Configure the server to serve the static folder
   
   check the documentation of your server provider to do so.
 
6. Create the RSA key
```bash
python3 manage.py creatersakey
```

7. Create super user
```bash
python3 manage.py createsuperuser
```
  
8. Run the server
```bash
python3 manage.py runserver
```
