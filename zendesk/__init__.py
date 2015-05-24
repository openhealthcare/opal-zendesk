"""
Plugin definition for the zendesk OPAL plugin
"""
from opal.core import plugins

from zendesk.urls import urlpatterns

class ZendeskPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.zendesk': [
            # 'js/zendesk/app.js',
            # 'js/zendesk/controllers/larry.js',
            # 'js/zendesk/services/larry.js',
        ]
    }
    head_extra = ['zendesk/snippet.html']
    
    def restricted_teams(self, user):
        """
        Return any restricted teams for particualr users that our
        plugin may define.
        """
        return []

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def flows(self):
        """
        Return any custom flows that our plugin may define
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}


plugins.register(ZendeskPlugin)
