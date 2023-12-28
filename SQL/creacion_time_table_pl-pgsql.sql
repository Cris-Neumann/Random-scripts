-- Crearemos y poblaremos una tabla llamada "Tabla_tiempo", en la cual añadiremos todos los días entre el 01/01/2010 y 12/31/2040, separando la fecha en
-- varios campos útiles, como por ejemplo: año, mes, semana, día, etc. Usualmente este tipo de tablas se crean al crear una base de datos.

CREATE TABLE IF NOT EXISTS Tabla_tiempo(
   ID_fecha SERIAL PRIMARY KEY NOT NULL UNIQUE,
   fecha VARCHAR (50),
   año INTEGER,
   sem INTEGER,
   trimes INTEGER,
   año_sem VARCHAR (50),
   mes INTEGER,
   semana INTEGER,
   dia INTEGER);
DO
$$
DECLARE FechaInicio DATE := '2010-01-01'; 
DECLARE FechaCiclo DATE := '2010-01-01'; 
DECLARE FechaFin DATE := '2040-12-31'; 
BEGIN
	WHILE FechaCiclo <= FechaFin
	LOOP
		INSERT INTO Tabla_tiempo(fecha, año, sem, trimes, año_sem, mes, semana, dia)
		VALUES (
			to_char(FechaCiclo, 'DD/MM/YYYY'), DATE_PART('year', FechaCiclo),
			CASE     
				WHEN CAST(DATE_PART('month', FechaCiclo) AS INTEGER) IN (1,2,3,4,5,6) THEN 1
				WHEN CAST(DATE_PART('month', FechaCiclo) AS INTEGER) IN (7,8,9,10,11,12) THEN 2
			END, DATE_PART('quarter', FechaCiclo), CONCAT(DATE_PART('year', FechaCiclo), '_', 			
			CASE
				WHEN CAST(DATE_PART('month', FechaCiclo) AS INTEGER) IN (1,2,3,4,5,6) THEN 1
				WHEN CAST(DATE_PART('month', FechaCiclo) AS INTEGER) IN (7,8,9,10,11,12) THEN 2
			END), DATE_PART('month', FechaCiclo), DATE_PART('week', FechaCiclo), 
			DATE_PART('day', FechaCiclo)
			);
		 FechaCiclo := FechaCiclo + INTERVAL '1 day';
	END LOOP;
END
$$