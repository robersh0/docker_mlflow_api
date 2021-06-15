import os

POSTGRES = {
    'user': os.getenv('POSTGRES_USER'),
    'pw': os.getenv('POSTGRES_PASSWORD'),
    'db': os.getenv('POSTGRES_DB'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
}

# General configuration
CONFIG = {
    'database': {
        'uri': 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    },
    'sentry': {
        'config': {
            'release': '0.1.0'
        },
        'dsn': os.getenv('SENTRY_DSN')
    },
    'app': {
        'port': os.getenv('PUBLIC_PORT'),
        'root': os.getenv('ROOT_PATH')
    }
}
