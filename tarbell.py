# Short project name
NAME = "tarbell-site"

# Descriptive title of project
TITLE = "Tarbell"

SPREADSHEET_KEY = "0Ak3IIavLYTovdDFGaVFMalo5dHBuQ25wWi1mT3prZGc"

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'tarbell-site',
    'title': 'Tarbell'
}

S3_BUCKETS = {
    "production": "s3://apps.chicagotribune.com//tarbell-site/",
    "staging": "s3://apps.beta.tribapps.com//tarbell-site/",
}

# Repository this project is based on (used for updates)
TEMPLATE_REPO_URL = "https://github.com/newsapps/tarbell-template"

import tarbell
import os
from flask import Blueprint

blueprint = Blueprint('tarbell_site', __name__)

def get_tutorial():
    path = os.path.join(os.path.dirname(tarbell.__file__), "docs/tutorial.rst")
    try:
        return open(path, 'r').read()
    except IOError:
        return None

@blueprint.app_context_processor
def context_processor():
    return {
        'tutorial': get_tutorial(),
    }
