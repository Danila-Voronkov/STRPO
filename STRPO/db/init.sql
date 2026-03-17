CREATE TABLE IF NOT EXISTS sensors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    plant_name TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sensors (name, plant_name, value, unit) VALUES
    ('1', '1', 23.5, '°C'),
    ('1', '1', 45.2, '%'),
    ('1', '1', 3200, 'lux');