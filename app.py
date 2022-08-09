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

@app.route('/', methods=['POST', 'GET'])
def home2():
   videoid = request.form["videoid"]
   return render_template('playerpage.html', videoid=videoid)


"""
@app.route('/playerpage', methods=['POST', 'GET'])
def playerpage():
   print("before")
   videoid = request.form["videoid"]
   print(videoid)
   return render_template('playerpage.html', videoid=videoid)
"""

@app.route('/submit_markers', methods=["POST", "GET"])
def submit_markers_json():
   """
   json structure:
   d = {timestamps: [], lat: [], lng: [] ]}
   """
   link = request.form["link"]
   timestamp = request.form["timestamp"]
   lat = request.form["lat"]
   long = request.form["lng"]
   print(link, timestamp, lat, long)
   sql = "INSERT INTO marker (video_timestamp, lat, lng, link) VALUES (:video_timestamp, :lat, :lng, :link)"
   db.session.execute(sql, {"video_timestamp": timestamp, "lat": lat, "lng": long, "link": link})
   db.session.commit()


def fm():
   sql = "SELECT video_timestamp, lat, lng, link FROM marker"
   result = db.session.execute(sql)
   return result


@app.route('/get_markers', methods=["GET"])
def fetch_markers_json():
   markers = fm()
   timestamps, lats, lngs, links = [], [], [], []

   for marker in markers:
      if marker[3] != "v_V0mErWGpk":
         timestamps.append(marker[0])
         lats.append(marker[1])
         lngs.append(marker[2])
         links.append(f"https://www.youtube.com/watch?v={marker[3]}")

   d = {"timestamps": timestamps,
        "lats": lats,
        "lngs": lngs,
        "links": links
        }
   return jsonify(d)


if __name__ == '__main__':
   app.run()