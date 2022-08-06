from sqlite3 import Timestamp
from flask import Flask
from flask import redirect ,render_template, request, session, jsonify
from backend.insert import insert_markers
from backend.fetch import fetch_markers
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri
db = SQLAlchemy(app)

@app.route('/')
def home():
   return render_template('playerpage.html')


@app.route('/submit_markers', methods=["POST", "GET"])
def submit_markers_json():
   """
   json structure:
   d = {timestamps: [], lat: [], lng: [] ]}
   """
   
   timestamp = request.form["timestamp"]
   lat = request.form["lat"]
   long = request.form["lng"]
   #insert_markers(timestamps, lats, longs)

   sql = "INSERT INTO marker (video_timestamp, lat, lng) VALUES (:video_timestamp, :lat, :lng)"
   db.session.execute(sql, {"video_timestamp": timestamp, "lat": lat, "lng": long})
   db.session.commit()

   #print(timestamps, lats, longs)

def fm():
   sql = "SELECT video_timestamp, lat, lng FROM marker"
   result = db.session.execute(sql)
   return result


@app.route('/get_markers', methods=["GET"])
def fetch_markers_json():
   markers = fm()
   timestamps, lats, lngs = [], [], []
   for marker in markers:
      timestamps.append(marker[0])
      lats.append(marker[1])
      lngs.append(marker[2])
   d = {"timestamps": timestamps,
        "lats": lats,
        "lngs": lngs
        }
   return jsonify(d)


if __name__ == '__main__':
   app.run()