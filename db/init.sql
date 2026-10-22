CREATE TABLE IF NOT EXISTS inferencias (
    id BIGSERIAL PRIMARY KEY,
    mensaje TEXT NOT NULL CHECK (length(trim(mensaje)) > 0),
    categoria VARCHAR(20) NOT NULL CHECK (categoria IN ('feat', 'fix', 'docs', 'test', 'chore', 'refactor')),
    creada_en TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_inferencias_creada_en
    ON inferencias (creada_en DESC);
