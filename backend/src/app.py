# compose_flask/app.py
from flask import Flask
from flask_migrate import Migrate
from models.database import database
from config import CONFIG

app = Flask(__name__)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['database']['uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SENTRY_CONFIG'] = CONFIG['sentry']['config']
    app.config['APPLICATION_ROOT'] = CONFIG['app']['root']

    database.init_app(app)
    database.create_all(bind=None)

    # Migrate
    migrate = Migrate(app, database)


@app.route('/')
def hello():
    return 'This is the response'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
