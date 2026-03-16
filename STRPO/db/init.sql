CREATE TABLE IF NOT EXISTS sensors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    plant_name TEXT NOT NULL,
    value FLOAT NOT NULL,
    unit TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Добавим несколько тестовых записей
INSERT INTO sensors (name, plant_name, value, unit) VALUES
    ('Температура', 'Роза', 23.5, '°C'),
    ('Влажность почвы', 'Кактус', 45.2, '%'),
    ('Освещённость', 'Фикус', 3200, 'lux');