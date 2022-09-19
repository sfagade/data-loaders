import os

import psycopg2
from dotenv import load_dotenv
from configuration import init_logger


load_dotenv()
log = init_logger("POSTGRES CONNECT")


def connect_to_db():
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


def close_db_connection(conn):
    log.debug("Closing postgres connection")
    conn.close()
