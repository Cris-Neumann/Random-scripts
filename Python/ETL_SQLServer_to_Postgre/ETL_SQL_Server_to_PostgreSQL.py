import os
import traceback
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from aux_functions import update_to_sql, insert_to_sql, credentials

# Fechas y ruta prinicpal
path = os.path.dirname(os.path.realpath(__file__))
today = datetime.today().strftime("%d-%m-%Y")
now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
cred = credentials(path)

# Origen: Conexion a BBDD SQL Server.
server = 'LAPTOP-N4RBDPIL\SQLEXPRESS'
db = cred['origen']['db']
engine = create_engine('mssql+pyodbc://@' + server + '/' + db + '?driver=SQL+Server')
source = pd.read_sql_query(""" SELECT * FROM tb_origen """, engine)

# Destino: Conexion a BBDD PostgreSQL.
user = cred['destino']['user']
passw = cred['destino']['passw']
host = cred['destino']['host']
port = cred['destino']['port']
db = cred['destino']['db']
engine = create_engine('postgresql://' + user + ':' + passw + '@' + host + ':' + port + '/' + db)
target = pd.read_sql('SELECT * FROM public."tb_destino"', engine)

# Filas de 'source' que no estan en 'target', es decir, cambios o nuevos registros.
changes = source[~source.apply(tuple,1).isin(target.apply(tuple,1))]
modified = changes[changes.id_usuario.isin(target.id_usuario)]
inserts = changes[~changes.id_usuario.isin(target.id_usuario)]

def main():
    try:
        update_len = update_to_sql(modified, 'tb_destino', 'id_usuario', engine)
        insert_len = insert_to_sql(inserts, 'tb_destino', engine)
        with open(path + r'/log.txt', 'a+') as f:
                    f.write("\n" + str(now) +': Actualizacion BBDD PostgreSQL con exito, ' + 
                    update_len + ' registros actualizados y ' + insert_len + ' registros ' +
                    'insertados.')
    except Exception as e:
        with open(path + r'/log.txt', 'a+') as f:
                    f.write("\n" + str(now) +': ERROR: Load funcion main(), ' 
                    'Traceback: ' + str(traceback.format_exc()))
        raise e

if __name__ == '__main__':
    main()
