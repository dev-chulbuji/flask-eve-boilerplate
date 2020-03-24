from eve.auth import TokenAuth


class ApiAuthorize(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        # print(token, allowed_roles, resource, method)

        self.set_request_auth_value('test')

        return True
