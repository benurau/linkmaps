from flask import Flask
from flask import redirect ,render_template, request, session, jsonify
from .backend.insert import insert_markers
from .backend.fetch import fetch_markers


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
   content = request.json
   timestamps = content["timestamps"]
   lats = content["lat"]
   lngs = content["lng"]
   insert_markers(timestamps, lats, lngs)


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