import os
from envparse import env

MONGO_HOST = env.str('MONGO_HOST', default="")
MONGO_PORT = env.int('MONGO_PORT', default=27017)
MONGO_DBNAME = env.str('MONGO_DBNAME', default="")

RESOURCE_METHODS = ['GET', 'POST']

DOMAIN = {
	'user': {
		'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
        },
    	'schema': {
            'username': {
               	'type': 'string',
               	'unique': True
            },
            'password': {
               	'type': 'string'
            },
            'email': {
               	'type': 'string'
            }
        }
    }
}
