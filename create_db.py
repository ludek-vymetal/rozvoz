import sqlite3

conn = sqlite3.connect('databaze.db')
c = conn.cursor()

c.execute("""
CREATE TABLE log_finance (
    id_zaznamu INTEGER PRIMARY KEY AUTOINCREMENT,
    id_restaurace INTEGER,
    castka REAL NOT NULL,
    castka_celkove REAL NOT NULL,
    popis TEXT NOT NULL,
    datum_provedeni DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

c.execute("""
CREATE TABLE uzivatele (
    id_uzivatele INTEGER PRIMARY KEY AUTOINCREMENT,
    jmeno TEXT NOT NULL,
    prijmeni TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefon TEXT,
    heslo TEXT NOT NULL,
    role TEXT NOT NULL,
    datum_registrace DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

c.execute("""
CREATE TABLE adresy_uzivatele (
    id_adresy INTEGER PRIMARY KEY AUTOINCREMENT,
    id_uzivatele INTEGER,
    nazev_adresy TEXT NOT NULL,
    adresa_ulice TEXT NOT NULL,
    adresa_cislo_domu TEXT NOT NULL,
    adresa_psc TEXT NOT NULL,
    adresa_mesto TEXT NOT NULL,
    hlavni_adresa BOOLEAN DEFAULT 0,
    FOREIGN KEY (id_uzivatele) REFERENCES uzivatele(id_uzivatele)
);
""")

c.execute("""
CREATE TABLE restaurace (
    id_restaurace INTEGER PRIMARY KEY AUTOINCREMENT,
    nazev TEXT NOT NULL,
    popis TEXT,
    email TEXT NOT NULL,
    telefon TEXT,
    adresa_ulice TEXT NOT NULL,
    adresa_cislo_domu TEXT NOT NULL,
    adresa_psc TEXT NOT NULL,
    adresa_mesto TEXT NOT NULL,
    image_url TEXT NOT NULL,
    id_spravce INTEGER NOT NULL,
    FOREIGN KEY (id_spravce) REFERENCES uzivatele(id_uzivatele)
);
""")

c.execute("""
CREATE TABLE produkty (
    id_produktu INTEGER PRIMARY KEY AUTOINCREMENT,
    id_restaurace INTEGER,
    nazev TEXT NOT NULL,
    image_url TEXT NOT NULL,
    popis TEXT,
    dostupnost BOOLEAN DEFAULT 1,
    FOREIGN KEY (id_restaurace) REFERENCES restaurace(id_restaurace)
);
""")

c.execute("""
CREATE TABLE nabidka_produktu (
    id_nabidky INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produktu INTEGER NOT NULL,
    castka REAL NOT NULL,
    platna_od DATETIME NOT NULL,
    platna_do DATETIME,
    FOREIGN KEY (id_produktu) REFERENCES produkty(id_produktu)
);
""")


c.execute("""
CREATE TABLE objednavky (
    id_objednavky INTEGER PRIMARY KEY AUTOINCREMENT,
    id_uzivatele INTEGER,
    datum_vytvoreni DATETIME DEFAULT CURRENT_TIMESTAMP,
    poznamka_pro_kurýra TEXT,
    jídlo_pripraveno BOOLEAN DEFAULT 0,
    doruceno BOOLEAN DEFAULT 0
);
""")

c.execute("""
CREATE TABLE objednavky_produkty (
    id_objednavky_produkty INTEGER PRIMARY KEY AUTOINCREMENT,
    id_objednavky INTEGER NOT NULL,
    id_nabidky INTEGER NOT NULL
);
""")

c.execute("""
CREATE TABLE doruceni_objednavky (
    id_doruceni INTEGER PRIMARY KEY AUTOINCREMENT,
    id_objednavky INTEGER NOT NULL,
    id_poslicka INTEGER,
    stav TEXT NOT NULL
);
""")

c.execute("""
CREATE TABLE operace_doruceni_objednavky (
    id_operace INTEGER PRIMARY KEY AUTOINCREMENT,
    id_doruceni INTEGER NOT NULL,
    id_objednavnky_produkty INTEGER NOT NULL,
    datum_prevzeti DATETIME,
    stav TEXT NOT NULL
);
""")

c.execute("""
CREATE TABLE log_system (
    id_zaznamu INTEGER PRIMARY KEY AUTOINCREMENT,
    zmena TEXT NOT NULL,
    datum_provedeni DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()