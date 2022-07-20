CREATE TABLE marker(
    id SERIAL PRIMARY KEY,
    video_timestamp timestamp,
    lat decimal,
    lng decimal
);