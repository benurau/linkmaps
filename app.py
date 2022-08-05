from sqlite3 import Timestamp
from flask import Flask
from flask import redirect ,render_template, request, session, jsonify
from backend.insert import insert_markers
from backend.fetch import fetch_markers


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('playerpage.html')


@app.route('/submit_markers', methods=["POST", "GET"])
def submit_markers_json():
   """
   json structure:
   d = {timestamps: [], lat: [], lng: [] ]}
   """
   
   timestamps = request.form["timestamp"]
   lats = request.form["lat"]
   longs = request.form["lng"]
   insert_markers(timestamps, lats, longs)
   # print(timestamps, lats, longs)
   return redirect("lolhentai.com")


def fetch_markers_json():
   markers = fetch_markers()
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