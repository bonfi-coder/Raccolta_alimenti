/**
Schema logico relazionale
comuni(codiceComune, nome, provincia, regione) -- PRIMARY KEY(codiceComune)
prodotti(codiceProdotto, nome, categoria, quantita, comune) -- PRIMARY KEY(codiceProdotti)
utenti(codiceUtente, username, password, comune) -- PRIMARY KEY(codiceUtente)
volontari(codiceVolontario, username, password, orario_inizio, orario_fine, ruolo)  -- PRIMARY KEY(codiceVolontario)
donatore(codiceDonatore, username, password)  -- PRIMARY KEY(codiceDonatore)

Vincoli di integrità referenziale:
- tra comune di prodotti e codiceComune di comuni
- tra comune di utenti e codiceComune di comuni
*/
DROP DATABASE IF EXISTS raccolta_alimenti;
CREATE DATABASE raccolta_alimenti;
USE raccolta_alimenti;

CREATE TABLE comuni (
    codiceComune CHAR(6),
    nome VARCHAR(50) NOT NULL,
    provincia VARCHAR(50) NOT NULL,
    regione VARCHAR(25) NOT NULL,  -- nome della regione
    PRIMARY KEY(codiceComune)
);

CREATE TABLE prodotti (
    codiceProdotto CHAR(4),
    nome VARCHAR(25) NOT NULL,
    categoria VARCHAR(15) NOT NULL CHECK(categoria IN("alimentari", "infanzia", "igiene", "abbigliamento")),
    quantita INT NOT NULL,
    comune CHAR(6) NOT NULL,
    PRIMARY KEY(codiceProdotto),
    FOREIGN KEY(comune) REFERENCES comuni(codiceComune)    
);

CREATE TABLE utenti (
    codiceUtente INT AUTO_INCREMENT,
    username VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    comune CHAR(6) NOT NULL,
    PRIMARY KEY(codiceUtente),
    FOREIGN KEY(comune) REFERENCES comuni(codiceComune)
);

CREATE TABLE volontari (
    codiceVolontario INT AUTO_INCREMENT,
    username VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    orario_inizio TIME NOT NULL,  -- ora:minuti:ss --phpmyadmin da errore, meglio usare TIME
    orario_fine TIME NOT NULL,  -- ora:minuti:ss  --phpmyadmin da errore, meglio usare TIME
    ruolo VARCHAR(10) NOT NULL CHECK(RUOLO IN("magazzino", "consegna")),
    PRIMARY KEY(codiceVolontario)
);

CREATE TABLE donatori (
    codiceDonatore INT AUTO_INCREMENT,
    username VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    PRIMARY KEY(codiceDonatore)
);