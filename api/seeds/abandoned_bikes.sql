-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS locations;
DROP SEQUENCE IF EXISTS locations_id_seq;
DROP TABLE IF EXISTS bikes;
DROP SEQUENCE IF EXISTS bikes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS locations_id_seq;
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    latitude DECIMAL(8,6),
    longitude DECIMAL(9,6)
);

CREATE SEQUENCE IF NOT EXISTS bikes_id_seq;
CREATE TABLE bikes (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(255),
    colour VARCHAR(255),
    condition VARCHAR(255) CHECK (condition IN ('poor', 'fair', 'good', 'excellent')),
    date_found DATE,
    location_id INTEGER REFERENCES locations(id)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO locations (name, latitude, longitude) VALUES ('Rad Cam', 51.75, -1.25);
INSERT INTO locations (name, latitude, longitude) VALUES ('Westgate', 51.75, -1.26);

INSERT INTO bikes (brand, colour, condition, date_found, location_id)
    VALUES ('Raleigh', 'green', 'poor', '2022-12-22', 1);
INSERT INTO bikes (brand, colour, condition, date_found, location_id)
    VALUES ('Nigel Dean', 'red', 'good', '2022-12-23', 2);
INSERT INTO bikes (brand, colour, condition, date_found, location_id)
    VALUES ('Dawes', 'brown', 'fair', '2022-12-24', 2);