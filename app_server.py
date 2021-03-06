# app_server.py

import os
import sys

from flask import Flask
from flask_restplus import Resource, Api

# Import Resources
from apis.classifier import api as module

# Import Load models module
from apis import models as model
from apis import classifier

app = Flask(__name__)
api = Api(  app,
            version='1.0',
            title='Cat, Dog Classifier - API docs',
            description='Identifies the uploaded image is a Cat or Dog.'
)

app.config.SWAGGER_UI_JSONEDITOR = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'


# Endpoints
api.add_namespace(module, path='/v1/classifier')


def load_models():
    print(" * Loading models please wait...")
    model.init()
    print(" * Models loaded successfully")
    classifier.ClassName('')


if __name__ == '__main__':
    load_models()
    app.run(host='0.0.0.0', debug=True)
else:
    load_models()
