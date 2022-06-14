import sqlite3

def heroi_table():
    con = sqlite3.connect('dbeaver_banco.sqlite')
    cur = con.cursor()

    herois_sql= """
    CREATE TABLE IF NOT EXISTS heroi(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    nivel INTEGER NOT NULL,
    forca INTEGER NOT NULL,
    defesa INTEGER NOT NULL, 
    vida INTEGER NOT NULL,
    mana DECIMAL(7,2) NOT NULL,
    moedas DECIMAL(7,2) NOT NULL,
    exp DECIMAL(7,2) NOT NULL
    )
    """
    
    cur.execute(herois_sql)
    con.commit()
    con.close()

heroi_table()


def monstro_table():
    con = sqlite3.connect('dbeaver_banco.sqlite')
    cur = con.cursor()

    monstro_sql= """
    CREATE TABLE IF NOT EXISTS monstro(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    nivel INTEGER NOT NULL,
    forca INTEGER NOT NULL,
    defesa INTEGER NOT NULL,
    vida INTEGER NOT NULL,
    mana DECIMAL,
    tipo VARCHAR,
    xp_recompensa DECIMAL NOT NULL,
    moedas_recompensa DECIMAL NOT NULL,
    boss BOLEAN,
    agressivo BOLEAN
    )
    """

    cur.execute(monstro_sql)
    con.commit()
    con.close()

monstro_table()


def batalhas():
    con = sqlite3.connect('dbeaver_banco.sqlite')
    cur = con.cursor()

    batalhas_sql = """
    CREATE TABLE IF NOT EXISTS batalhas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATA,
    hora TIME,
    horoi_ganhou BOLEAN,
    multiplicador DECIMAL
    
    )
    """

    cur.execute(batalhas_sql)
    con.commit()
    con.close()

batalhas()


def heroi_poder():
    con = sqlite3.connect('dbeaver_banco.sqlite')
    cur = con.cursor()
    
    poder_heroi_sql = """
    CREATE TABLE IF NOT EXISTS heroi_poder(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    heroi_id INTEGER NOT NULL,
    poder_id INTEGER NOT NULL
    )
    """
    cur.execute(poder_heroi_sql)
    con.commit()
    con.close()

heroi_poder()


def monstro_poder():
    con = sqlite3.connect('dbeaver_banco.sqlite')
    cur = con.cursor()

    poder_monstro_sql = """
    CREATE TABLE IF NOT EXISTS monstro_pode(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monstro_id INTEGER,
    poder_id INTEGER
    )
    """

    cur.execute(poder_monstro_sql)
    con.commit()
    con.close()

monstro_poder()




def guerra_table():
    con = sqlite3.connect('dbeaver_banco.sqlite')
    cur = con.cursor()

    monstro_heroi_batalha_sql = """
    CREATE TABLE IF NOT EXISTS monstro_heroi_batalha(
        id INTERGER PRIMARY KEY,
        monstro_id INTEGER NOT NULL,
        batalha_id INTEGER NOT NULL,
        heroi_id INTEGER NOT NULL
    )
    """

    cur.execute(monstro_heroi_batalha_sql)
    con.commit()
    con.close()

guerra_table()

