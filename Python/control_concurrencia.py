### Control de concurrencia en escritura de tablas Delta ###
### Cuando exista concurrencia, esperará ciertos segundos antes de un retry ###

def overwrite_delta_table(df, delta_table_name, mode="overwrite"):
    df.write.format("delta").mode(mode).saveAsTable(delta_table_name)

max_retries = 5
retry_delay_seconds = 30
for attempt in range(max_retries):
    try:
        overwrite_delta_table(df_to_save, delta_table, mode="overwrite")
        break
    except Exception as e:
        if "Concurrent" in e.__class__.__name__ or "Concurrent" in str(e):
            waiting_seconds = retry_delay_seconds * (1 + attempt)
            print(f'Concurrency issue detected ({e.__class__.__name__}). Esperando {waiting_seconds} segundos antes de reintentar...')
            if attempt < max_retries - 1:
                time.sleep(waiting_seconds)
        else: raise e
