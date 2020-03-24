from eve import Eve
from auth.service import ApiAuthorize
from init import register_event_hook


def create_app(environment=None, configuration=None):
    app = Eve(auth=ApiAuthorize)

    register_event_hook(app)

    return app
