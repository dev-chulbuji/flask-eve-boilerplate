from groups.model import GroupModel


class GroupController:
    group_model = None

    def __init__(self):
        self.group_model = GroupModel()

    def get_by_title(self, title):
        if title == '':
            raise ValueError('Invalid title when getting group by title')

        group = self.group_model.get_by_title(title)

        if group is None:
            raise Exception(f'Error with getting group :: {title}')

        return group
