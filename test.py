
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

    create table if not exists salle (
    id_salle integer primary key autoincrement,
    nom_salle text not null,
    capacite integer,
    type_projection text
    );

    create table if not exists reservation (
    id_res integer primary key autoincrement,
    nom_cli text not null,
    id_film integer,
    id_salle integer,
    date_res text,
    prix real,
    foreign key (id_film) references film(id_film),
    foreign key (id_salle) references salle(id_salle)
    );
    """)

    db.commit()
    db.close()


    def supp_tab(nom_table, nom_colone):
        db.execute("f,delete from {Table} where {column}=", (table, colone))
        db.commit()
        db.close()


