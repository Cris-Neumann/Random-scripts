-- Uso de comandos ROW_NUMBER, OVER Y PARTITION BY:
-- "ROW_NUMBER" PONE NUMEROS ENTEROS DESDE 1 EN ADELANTE PARA UNA PARTICION ELEGIDA.
-- "OVER" ES UN OPERADOR AUXILIAR QUE SIRVE PARA DECIR POR EJ: APLICATE "SOBRE" UNA PARTICION.
-- "PARTITION" CREA UNA PARTICION POR ALGUN CAMPO QUE QUERAMOS (POR EJ POR RUT, Y CON SU ORDER BY CORRESPONDIENTE),
-- PARA LUEGO IDEALMENTE COMBINARLA CON ROW_NUMBER, DONDE LE PONDRÁ UN NÚMERO CORRELATIVO A CADA ELEMENTO DE LA PARTICION, 
-- Y SI LA PARTICION ESTÁ ORDENADA DESCEDIENTEMENTE, ENTONCES AL PONER ROW_NUMBER=1 EN UN FILTRO POSTERIOR, 
--  PODREMOS OBTENER EL 1ER ELEMENTO DE CADA PARTICION. ABAJO UN BUEN EJ:

USE DB_Operaciones
;WITH x AS
(
  SELECT [RUT]
      ,[ESTADO]
      ,[FECAPR]
      ,[FECMODIF]
      ,rn = ROW_NUMBER() OVER 
   	  (
      	    PARTITION BY [RUT]
            ORDER BY [RUT], [FECMODIF] DESC
          )
  FROM [DB_Operaciones_WOP].[dbo].[KYC_CLIENTE_CONTROL_ALL]
)
SELECT * FROM x WHERE rn = 1
AND LEFT(RUT, NULLIF(LEN(RUT)-1,-1)) IN (
78953430
)

----------------------------------------------------------------------------------------------------------------------------------------------------------------
-- USO DE "RANK": SIMILAR AL ROW_NUMBER, SOLO QUE PARA "EMPATES" PROPORCIONA EL MISMO VALOR ENTERO PARA TODOS LOS EMPATES

USE DB_Operaciones
BEGIN  
;with OPS as (
  SELECT  h.id_operacion AS 'ID', 
		   O.RUT_CLIENTE AS 'RUT CLIENTE',
		   O.NOMBRE_CLIENTE AS 'NOMBRE CLIENTE', 
		   O.SEGMENTO AS 'SEGMENTO', 
		   T.NOMBRE AS 'TIPO OPERACION',
		   CONVERT(varchar,O.FECHA_INGRESO_INICIO,3) AS 'FECHA INGRESO',
		   FORMAT(O.FECHA_INGRESO_INICIO,'HH:mm:ss') AS 'HORA INGRESO',
		   CONVERT(varchar,H.FECHA_MODIFICACION,3) AS 'FECHA INGRESO MIDDLE',
		   FORMAT(H.FECHA_MODIFICACION,'HH:mm:ss') AS 'HORA INGRESO MIDDLE',
		   M.NOMBRE AS 'MONEDA',
		   O.MONTO AS 'MONTO',
           o.CANT_OPERACIONES AS 'CANT OP.',
  rank() over (partition by h.id_operacion order by  H.ID_OPERACION ,H.FECHA_MODIFICACION DESC) as [r]
  FROM CO_OPERACION_HISTORIA H
	  LEFT JOIN CO_OPERACION O ON H.ID_OPERACION = O.ID
	  LEFT JOIN CO_MONEDA M ON O.ID_MONEDA = M.ID
	  LEFT JOIN CO_ESTADO E ON O.ID_ESTADO = E.ID
	  LEFT JOIN CO_TIPO_OPERACION T ON T.ID = O.ID_TIPO_OPERACION
	  LEFT JOIN CO_EVENTO_OPERACION EV ON  EV.ID = O.ID_EVENTO
  WHERE 
	    DAY(H.FECHA_MODIFICACION) BETWEEN '05' AND '11'       
    AND MONTH(H.FECHA_MODIFICACION)=01 ---------Mes a consultar
    AND YEAR(H.FECHA_MODIFICACION)=2022 --------Año a consultar
    AND H.ID_ESTADO = 1 AND O.ELIMINADO = 0 AND O.ID_TIPO_NEGOCIO = 2)     
select *
from OPS
where [r] = 1
ORDER BY 8
END
