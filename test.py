
import sqlite3

# --- GESTION DE BASE DE DONNÉES CINÉMA ---

# - FONCTION DE CRÉATION DE LA BASE DE DONNÉES -

def creer_tab():
    db = sqlite3.connect("cinema.db")
    cursor = db.cursor()
    cursor.executescript("""create table if not exists film (id_film integer primary key autoincrement,
    titre text not null,
    genre text,
    duree integer
    );

    create table if not exists client (
    id_client integer primary key autoincrement,
    nom_client text not null,
    numero_telephone varchar,
    email varchar,
    );

    create table if not exists reservation (
    id_res integer primary key autoincrement,
    id_client text not null,
    id_film integer,
    nom_salle integer,
    type_de_projection varchar,
    date_res varchar,
    prix real,
    foreign key (id_film) references film(id_film),
    foreign key (id_client) references salle(id_client),
    );
    """)

    db.commit()
    db.close()


    def supp_tab(nom_table, nom_colone):
        db.execute("f,delete from {Table} where {column}=", (table, colone))
        db.commit()
        db.close()


