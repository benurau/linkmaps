import db


def fetch_pairs():
    sql = "SELECT video_timestamp, lat, lng FROM marker"
    result = db.session.execute(sql)
    return result