from flask import Flask

def create_app():
    app = Flask(__name__) 
    from .game import game
    app.register_blueprint(game)
    return app