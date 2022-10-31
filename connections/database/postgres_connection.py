import os

import psycopg2


def connect_to_postgres(log):
    conn = psycopg2.connect(database=os.environ.get("POSTGRES_DB"),
                            host=os.environ.get("POSTGRES_HOST"),
                            user=os.environ.get("POSTGRES_USER"),
                            password=os.environ.get("POSTGRES_PASSWORD"))

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    log.info('PostgreSQL database version: ')
    cur.execute('SELECT version()')

    # close the communication with the PostgreSQL
    cur.close()
    return conn


def close_postgres_connection(conn, log):
    log.debug("Closing postgres connection")
    conn.close()


def connect_to_mongo(log):
    pass


def close_mongo_connection(log):
    pass
