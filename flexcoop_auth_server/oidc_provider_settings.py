from django.utils.translation import ugettext as _
from oidc_provider.lib.claims import ScopeClaims

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