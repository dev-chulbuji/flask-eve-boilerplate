from flask import current_app as app


class GroupModel:
    def __init__(self):
        pass

    def get_by_title(self, title):
        groups = app.data.driver.db['groups']
        return groups.find_one({'title': title})
