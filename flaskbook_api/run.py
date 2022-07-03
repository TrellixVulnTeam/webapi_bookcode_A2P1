import os
from flaskbook_api.api import create_app
config = os.environ.get("CONFIG","local")
app= create_app(config)