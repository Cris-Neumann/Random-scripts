-- Desde consola -- DB destino en PostgreSQL
CREATE DATABASE db_destino;
\c db_destino;

-- Desde PGAdmin -- DB destino en PostgreSQL
CREATE TABLE tb_destino (
	id_usuario SERIAL PRIMARY KEY NOT NULL UNIQUE,
	rut	VARCHAR (100),
    nombre	VARCHAR (100),
    apellido VARCHAR (100));

INSERT INTO tb_destino (id_usuario, rut, nombre, apellido) 
VALUES 
    (1, '555555555', 'juan', 'perez'),
    (2, '6789', 'josefa', 'gonzalez'),
    (3, '2244669', 'jose', 'donoso'),
    (4, '1113377', 'david', 'diaz');
