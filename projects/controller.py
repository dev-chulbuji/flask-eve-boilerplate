from groups.controller import GroupController


class ProjectController:
    group_controller = None

    def __init__(self):
        self.group_controller = GroupController()

    def on_pre_GET_items(self, request, lookup):
        user_part = 'channel-server'
        group = self.group_controller.get_by_title(user_part)

        lookup["group"] = {'$eq': group.get('_id')}
        print(lookup)
        pass
