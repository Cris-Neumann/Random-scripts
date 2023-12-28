# Funciones de apoyo para ETL desde SQL Server hacia PostgreSQL.

def credentials(path):
    """Funcion que genera un diccionario con credenciales
    para conectarse a BBDD de origen y de destino.
    Args:
        path (string): Ruta con las credenciales.
    Returns:
        cred (dict): Diccionario con las credenciales.
    """
    import json
    with open(path + "/credentials.json") as file_credentials:
        cred = json.load(file_credentials).copy()      
    return cred

def update_to_sql(df, table_name, key_name, engine):
    """Funcion que actualiza tabla destino con modificaciones.
    Args:
        df (DataFrame): DataFrame con los registros a actualizar.
        table_name (string): Nombre de la tabla a actulizar.
        key_name (string): Nombre del campo clave de la tabla a actualizar.
        engine (engine): Objeto de SQLAlchemy que genera la conexion de Python a PostgreSQL.
    Returns:
        update_len (string): Cantidad de registros a actualizar.
    """
    if len(df) > 0:
        a = []
        update_len = str(len(df.copy()))
        table = table_name
        primary_key = key_name
        temp_table = f"{table_name}_temporary_table"
        for col in df.columns:
            if col == primary_key:
                continue
            a.append(f'"{col}"=s."{col}"')
        df.to_sql(temp_table, engine, if_exists='replace', index=False)
        update_stmt_1 = f'UPDATE public."{table}" f '
        update_stmt_2 = "SET "
        update_stmt_3 = ", ".join(a)
        update_stmt_4 = f' FROM public."{table}" t '
        update_stmt_5 = f' INNER JOIN (SELECT * FROM public."{temp_table}") \
            AS s ON s."{primary_key}"=t."{primary_key}" '
        update_stmt_6 = f' Where f."{primary_key}"=s."{primary_key}" '
        update_stmt_7 = update_stmt_1 + update_stmt_2 + update_stmt_3 + update_stmt_4 \
            + update_stmt_5 +  update_stmt_6 +";"
        with engine.begin() as cnx:
            cnx.execute(update_stmt_7)
        drop_temp = f'DROP TABLE public.{temp_table}'
        with engine.begin() as cnx:
            cnx.execute(drop_temp)
    else: 
        update_len = '0'
    return update_len

def insert_to_sql(df, table_name, engine):
    """Funcion que agrega nuevos registros a tabla destino.
    Args:
        df (DataFrame): DataFrame con los registros a insertar.
        table_name (string): Nombre de la tabla a la cual se haran insertos de data.
        engine (engine): Objeto de SQLAlchemy que genera la conexion de Python a PostgreSQL.
    Returns:
        None: None.
    """
    if len(df) > 0:
        table = table_name
        insert_len = str(len(df.copy()))
        temp_table = f"{table_name}_temporary_table"
        df.to_sql(temp_table, engine, if_exists='replace', index=False)
        insert_query_1 = f'INSERT INTO public.{table} (id_usuario,rut,nombre,apellido) \
        VALUES (%s,%s,%s,%s)'
        inserto = list(df.copy().apply(tuple,1))
        for row in range(0,len(inserto)):
            record_to_insert = inserto[row]
            with engine.begin() as cnx:
                cnx.execute(insert_query_1,record_to_insert)
        drop_temp = f'DROP TABLE public.{temp_table}'
        with engine.begin() as cnx:
            cnx.execute(drop_temp)
    else: 
        insert_len = '0'
    return insert_len