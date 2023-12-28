-- DB origen en SQL Server
CREATE DATABASE db_origen;
GO
USE db_origen
CREATE TABLE tb_origen(
	id_usuario INT,
	rut VARCHAR(100),
	nombre VARCHAR(100),
	apellido VARCHAR(100)
)
INSERT INTO tb_origen (id_usuario, rut, nombre, apellido) 
VALUES 
    (1, '12345', 'juan', 'perez'),
    (2, '6789', 'maria', 'gonzalez'),
    (3, '2244669', 'jose', 'soto'),
    (4, '1113377', 'david', 'diaz'),
    (5, '555555', 'joel', 'gutierrez'),
    (6, '777777', 'felpe', 'urrutia');
