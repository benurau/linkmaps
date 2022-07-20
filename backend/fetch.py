import os
from flask_sqlalchemy import SQLAlchemy

import os
from flask import Flask


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)



def fetch_markers():
    sql = "SELECT video_timestamp, lat, lng FROM marker"
    result = db.session.execute(sql)
    return result