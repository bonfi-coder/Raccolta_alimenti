"""
Script python per l'estrazione dei dati relativi ai comuni
@author: Bonfante Stefano
@version: 1.0 201-04-03
"""
import csv
import pymysql
import logging
import time
from datetime import datetime
global first_line

__author__ = "Bonfante Stefano"
__version__ = "1.0 2021-04-03"


def connection_to_database(databaseName):
    """
    Crea la connessione e il cursor per il database.
    """
    connection = pymysql.connect(host="127.0.0.1", user="root",passwd="", database=databaseName)
    logger.info("Apertura connessione con database: host: 127.0.0.1, user: root password: , database: " + databaseName)
    print("Apertura connessione con il database:")
    print("Host: 127.0.0.1")
    print("User: root")
    print("Password: ")
    print("Database: " + databaseName)
    cursor = connection.cursor()
    
    return cursor, connection


def insert_to_database(sql, cursor):
    """
    Esegue gli insert per la tabella comuni del database.
    """
    for query in sql:
        cursor.execute(query)


def get_comuni(file_comuni):
    """
    Preso in input il file dei comuni ne
    estrae le informazioni necessarie.
    """
    count = 0
    sql = []
    with open(file_comuni, encoding="utf-8") as f:
        for line in f:
            if count == 3:
                line = line.replace("\t", " ")
                line = line.replace("\n", "")
                line = line.split(",")
                insert = "INSERT INTO comuni(codiceComune, nome, provincia, regione) VALUES (\""+line[4]+"\", \""+line[6]+"\", \""+line[11]+"\", \""+line[10]+"\");"
                sql.append(insert)
            else:
                first_line = False
                count += 1
    return sql
    
    
def write_comuni(file_sql_comuni):
    """
    Preso in input una lista di istruzioni sql le scrive
    all'interno del file di output.
    """

def log(file_log):
    """ Inizializza il file di log
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(file_log)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s;%(created)f;%(levelname)s;%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Nuova esecuzione dello script")

    return logger


def start():
    logger.info("Esecuzione script estrazioneComuni.py")
    file_comuni = "../flussi/Elenco-comuni-italiani.csv"
    file_sql_comuni = ".//comuni.dump.sql" # non usato
    databaseName = "raccolta_alimenti"
    print("Recupero informazioni sui comuni")
    logger.info("Recupero informazioni sui comuni")
    sql = get_comuni(file_comuni)
    cursor, connection = connection_to_database(databaseName)
    print("Scrittura su database")
    logger.info("Scrittura su database")
    insert_to_database(sql, cursor)
    #get_comuni(file_comuni, cursor)
    connection.commit()
    connection.close()
    print("Chiusura connessione con il database")
    logger.info("Chiusura connessione con il database")
    logger.info("Esecuzione script estrazioneComuni.py terminata!\n")
    

if __name__ == "__main__":
    print("Esecuzione script estrazioneComuni.py")
    logger = log("..//log//trace.log")
    start()
    print("Esecuzione script estrazioneComuni.py terminata!")
    
    
    