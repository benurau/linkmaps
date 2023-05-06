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


def insert_markers(timestamp: float, lat:float, lng:float):
    sql = "INSERT INTO marker (video_timestamp, lat, lng) VALUES (:video_timestamp, :lat, :lng)"
    db.session.execute(sql, {"video_timestamp": timestamp, "lat": lat, "lng": lng})
    db.session.commit()
