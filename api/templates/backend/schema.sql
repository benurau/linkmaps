CREATE TABLE marker(
    id SERIAL PRIMARY KEY,
    video_timestamp float,
    lat decimal,
    lng decimal,
    link TEXT
);