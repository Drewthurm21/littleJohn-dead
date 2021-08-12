from flask_socketio import SocketIO

if os.environ.get(FLASK_ENV) == "production":
    origins = [
        'http://myURLhere',
        'https://myURLhere'
    ]
else:
    origins = '*'

socketio = SocketIO(cors_allowed_origins=origins)

