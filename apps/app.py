from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import  SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

db= SQLAlchemy()
csrf = CSRFProtect()

# create_app関数を作成する
def create_app(config_key):
    # Flaskインスタンス生成
    app = Flask(__name__)
    app.config.from_object(config[config_key])


    db.init_app(app)

    Migrate(app,db)
    csrf.init_app(app)
    
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud,url_prefix="/crud")

    return app