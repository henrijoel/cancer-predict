importer  sqlite3

#création de la base de donné
connexion  =  sqlite3 . connecter ( 'base de données.db' )

avec  open ( 'shema.sql' ) comme  f :
    connexion . executescript ( f . read ())

#vous créez un objet Cursor qui vous permet d'utiliser sa méthode execute()
# cur = connexion.cursor()
#
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# (« Premier message », « Contenu du premier message »)
# )
#
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
# ('Deuxième message', 'Contenu du deuxième message')
# )
#
# connexion.commit()
# connexion.fermée()