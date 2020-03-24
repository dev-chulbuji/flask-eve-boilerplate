import os

from auth.service import ApiAuthorize
from common.model.roles import RoleModel

MONGO_HOST = os.environ.get('MONGO_HOST', '127.0.0.1')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'beluga-auth')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'beluga-auth')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'beluga-auth')
MONGO_AUTH_SOURCE = os.environ.get('MONGO_AUTH_SOURCE', 'beluga-auth')

OPLOG = True
EMBEDDING = True
URL_PREFIX = 'api'

project_schema = {
    'title': {
        'type': 'string'
    },
    'group': {
        'type': 'objectid',
        'required': True,
        'data_relation': {
            'resource': 'groups',
            'field': '_id',
            'embeddable': True,
        },
    }
}

group_schema = {
    'title': {
        'type': 'string',
        'unique': True,
    },
    'users': {
        'type': 'list',
    }
}

user_schema = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
        'unique': True,
    },
    'token': {
        'type': 'string'
    },
    'roles': {
        'type': 'list',
        'allowed': RoleModel.values_list
    }
}

users = {
    'item_title': 'user',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'authentication': ApiAuthorize,
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'item_methods': ['GET'],
    'resource_methods': ['GET', 'POST'],
    'schema': user_schema,
}
groups = {
    'item_title': 'group',
    'authentication': ApiAuthorize,
    'cache_expires': 10,
    'item_methods': ['GET'],
    'resource_methods': ['GET', 'POST'],
    'schema': group_schema
}
projects = {
    'item_title': 'project',
    'authentication': ApiAuthorize,
    'cache_expires': 10,
    'item_methods': ['GET'],
    'resource_methods': ['GET', 'POST'],
    'schema': project_schema
}

DOMAIN = {
    'users': users,
    'groups': groups,
    'projects': projects
}
