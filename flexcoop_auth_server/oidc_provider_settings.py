from django.utils.translation import ugettext as _
from oidc_provider.lib.claims import ScopeClaims
from oidc_provider.lib.utils.token import decode_id_token
from user_management.models import FlexUser
from django.contrib.sessions.models import Session


class CustomScopeClaims(ScopeClaims):

    info_role = (
        _(u'Role'),
        _(u'Obtain the role of this user in FLEXCoop environment.'),
    )

    def scope_role(self):
        # self.user - Django user instance.
        # self.userinfo - Dict returned by OIDC_USERINFO function.
        # self.scopes - List of scopes requested.
        # self.client - Client requesting this claims.
        dic = {
            'role': self.user.user_info.role,
        }
        return dic

    info_flexId = (
        _(u'flexId'),
        _(u'Obtain the anonimized Id of this user in FLEXCoop environment.'),
    )

    def scope_flexId(self):
        # self.user - Django user instance.
        # self.userinfo - Dict returned by OIDC_USERINFO function.
        # self.scopes - List of scopes requested.
        # self.client - Client requesting this claims.
        dic = {
            'flexId': self.user.user_info.anonimizedId,
        }
        return dic


def uid_sub_token_id(user):
    return str(user.user_info.anonimizedId)

def end_session(request, id_token, post_logout_redirect_uri, state, client, next_page):
    # get session from token:
    token_info = decode_id_token(id_token, client)
    if "session_state" in token_info:
        session = Session.objects.get(session_key=token_info['session_state']).delete()

def add_session_id(dic, user, token, request):
    dic.update({'session_state': request.session.session_key})
    return dic

