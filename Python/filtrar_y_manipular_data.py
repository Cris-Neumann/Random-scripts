#    A continuación filtraremos y manipularemos un archivo csv llamado "datos_pacientes" que posee los siguientes campos: 
#    RUT | Nombre | Genero | Fecha_nac | Previsión | Monto_Deuda | País_origen | Ciudad_Residencia | RUT_médico | Costo_consulta

import pandas as pd
import numpy as np

# Cargamos el csv en una Dataframe de pandas y vemos los tipos de datos de sus columnas:
df_pacientes = pd.read_csv("datos_pacientes.csv",sep=";")
print(df_pacientes.dtypes)

# Filtramos con el método "loc" el Dataframe, para obtener solo los pacientes con pais de origen distinto a Chile:
df_pacientes.loc[df_pacientes["País_origen"] != "Chile"]

# Al filtro anterior añadimos otro filtro: que además tengo un monto de deuda superior a $1.000.000 
df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"]>1000000)]

# Al filtro anterior añadimos otro filtro: que la prevsión sea "FONASA"
print(df_pacientes.loc[(df_pacientes["País_origen"] != "Chile") & (df_pacientes["Monto_Deuda"]>1000000) & (df_pacientes["Previsión"] == "FONASA")])

# Ahora creamos el siguiente filtro: pacientes cuyo país de origen es Chile, pero solo de las ciudades de Santiago o Concepción, 
# y que además tengan una deuda mayor a $1.000.000 y previsión FONASA.
df_pacientes.loc[(df_pacientes["País_origen"] == "Chile") & ((df_pacientes["Ciudad_Residencia"] == "Santiago") | 
(df_pacientes["Ciudad_Residencia"] == "Concepción")) & (df_pacientes["Monto_Deuda"]>1000000) & (df_pacientes["Previsión"] == "FONASA")]

# Ahora supondremos que hay un error del sistema y en el Dataframe aparecieron algunos RUT terminados en "J", y eliminaremos dichos registros
# y antes haremos una copia del Dataframe para trabajar sobre esa copia:
df_pac_copia = df_pacientes.copy()
df_pac_copia = df_pac_copia.loc[df_pac_copia["RUT"].str[-1:] != "J"]

# Ahora ordenaremos df_pacientes de forma ascendente mediante la columna “Monto_Deuda” y "Fecha_nac” 
df_pacientes = df_pacientes.sort_values(by=["Monto_Deuda","Fecha_nac"],ascending=True)

# Ahora extraemos la media, mínimo y máximo de la deuda por tipo de previsión mediante una pivot table (tabla dinámica en Excel)
pt = df_pacientes.pivot_table(index="Previsión",values="Monto_Deuda",aggfunc={np.mean,np.min,np.max})
print(pt)

# Ahora creamos una tabla dinámica por RUT_médico con la suma de cada Costo_consulta, transformando antes esta última columna a entero
df_pacientes["Costo_consulta"] = df_pacientes["Costo_consulta"].astype("int64")
pt2 = df_pacientes.pivot_table(index="RUT_medico",values="Costo_consulta",aggfunc=np.sum)
print(pt2)

# Finalmente haremos un merge (cruce, o "Buscarv" en Excel) entre este Dataframe "df_pacientes" y un Excel llamado "historial", el que posee data del
# historial médico de los pacientes y posee un campo llamado "RUT_pac", con el mismo formato que el campo RUT de "df_pacientes", mediante el cual cruzaremos:
df_historial = pd.read_excel('historial.xlsx')
df_cruce = df_pacientes.merge(df_historial,left_on="RUT",right_on="RUT_pac",how="left")