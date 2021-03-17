from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


def create_app(in_config = {}):
    app = Flask(__name__)
    config = {
        "CACHE_TYPE": "SimpleCache",
        "CACHE_DEFAULT_TIMEOUT": 300,
        "DATABASE": 'file::memory:?cache=shared'
    }
    config.update(in_config)
    app.config.from_mapping(config)
    cache = Cache(config=config)
    cache.init_app(app)
    app.config["cache"] = cache
    return app
