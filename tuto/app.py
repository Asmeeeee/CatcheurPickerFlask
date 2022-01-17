from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),p
        )
    )

from flask_sqlalchemy import SQLAlchemy
app.config['SECRET_KEY'] = "d3f9e45b-d14e-4fca-b075-72b2a409c81d"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../tuto.db')
)
db = SQLAlchemy(app)

# pour lancer aller dans venv et faire virtualenv -p python3 venv
# source venv/bin/activate
# pour installer flask python-dotenv
# pip freeze pour voir ce qui est installer