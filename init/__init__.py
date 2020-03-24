from projects.controller import ProjectController


def pre_get_callback(resource, request, lookup):
    pass


def register_event_hook(app):
    project_controller = ProjectController()

    app.on_pre_GET += pre_get_callback
    app.on_pre_GET_projects += project_controller.on_pre_GET_items
