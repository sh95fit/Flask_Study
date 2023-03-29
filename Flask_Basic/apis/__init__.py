from flask import Blueprint
from flask_restx import Api


blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

api = Api(
    blueprint,
    title="Hun's Flask API",
    version='1.0',
    doc='/docs',
    description="Hun's Flask API Docs"
)


# TODO : add namespace to Blueprint
