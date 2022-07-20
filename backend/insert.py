import db


def insert_pairs(timestamps: list, lats:list, lngs:list):
    for inx in range(len(timestamps)):
        timestamp = timestamps[inx]
        lat = lats[inx]
        lng = lngs[inx]
        sql = "INSERT INTO marker (video_timestamp, lat, lng) VALUES (:video_timestamp, :lat, :lng)"
        db.session.execute(sql, {"video_timestamp": timestamp, "lat": lat, "lng": lng})
    db.session.commit()
