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
export SITE_URL=""
export EMAIL_HOST="smtp.gmail.com"
export EMAIL_USER=""
export EMAIL_PASSWORD=""
export EMAIL_PORT="587"


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

9. Server administration
The server administration is reached under the endpoint 
```
<server-adress>/accounts/login/
```

<br><br>

## Adding flexcoop users
The user login is found under
```
<server-adress>/accounts/login/
```

where you also find a link to the page 
```
<server-adress>/accounts/login/signup
```
that allows to create new 'flexcoop' users. 

Using this method, the anonimized id is generated by the server and the users role is set to 'Prosumer'

<BR>
It is also possible to create users using the django servers admin console and the 'add user' function. To allow login via oAuth, one needs to set a role and supply an anonimized id for the user in the upper of the two 'Profile/Flex user' settings of the user.   
<br><br>

The administrator console allows to change the role of a user to prosumer or agregator.



<br><br>
## Adding backend clients

These are the steps needed to a web-backend-client that allows its users to log into the server using oAuth2/OpenID.

1. In the django admin console , navigate to Client / Add client

2. Choose a name for the client

3. The owner is numerical user id, use 0 for the admin

4. Choose client type confidential and code (Authorization flow) if you are using oAuth methods provided in the backend-mockup demo

5. Require consent and reuse consent

6. Press 'Save and continue editing' at the end of the page

7. If no error is issued, the django server will generate a client id and a client secret that need to be used by this client

8. Fill in the scopes (one per line): 
```
openid
role
<client_id>
```

9. Fill in the full Redirect URIs used by the oAuth lib - in case of the backend-mockup, these were
```
http://127.0.0.1:8080/login/authorized
http://localhost:8080/login/authorized
https://<cluster-adress>/login/authorized
```

10. Fill in session management
```
http://127.0.0.1:8080/
http://localhost:8080/
https://<cluster-adress>/
<client_id>
```