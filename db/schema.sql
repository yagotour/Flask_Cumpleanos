DROP TABLE IF EXISTS datos;

CREATE TABLE datos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nombre TEXT NOT NULL,
    observaciones TEXT NULL
);