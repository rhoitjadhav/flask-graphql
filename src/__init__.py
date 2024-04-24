from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints here
    from src.views import users_bp

    app.register_blueprint(users_bp)

    from src.graphql.trips_graphql import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.route("/test1/")
    def test_page():
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
