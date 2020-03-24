from enum import Enum
from common.decorator import values_list


@values_list
class RoleModel(Enum):
    ADMIN = 'admin'
    USER = 'user'
