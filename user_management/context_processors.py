from flexcoop_auth_server import settings


def oauth_logo(request):
    return {"oauth_logo": settings.OAUTH_SERVER_LOGO}
