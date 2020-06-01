CREATE TABLE metrics
(
  id SERIAL,
  timestamp TIMESTAMPTZ NOT NULL,
  temperature DOUBLE PRECISION NOT NULL,
  duration TEXT NOT NULL,

  PRIMARY KEY (id)
);

CREATE TABLE logs
(
  id SERIAL,
  url TEXT NOT NULL,
  http_method character varying(10) NOT NULL,
  status_code INT NOT NULL,
  accessed_on TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

  PRIMARY KEY (id)
);