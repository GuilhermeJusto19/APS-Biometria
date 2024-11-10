import sqlite3

class BancoDados():

    def conecta_db(self):
        self.conn = sqlite3.connect("gov_app.db")
        print("Conexão estabelecida com o banco de dados")
        self.cursor = self.conn.cursor()

    def desconecta_db(self):
        print("Conexão encerrada com o banco de dados")
        self.conn.close()

    def monta_tabelas(self):
        self.conecta_db()

        self.comando_tabela_user = """CREATE TABLE IF NOT EXISTS 
            users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                role INTEGER
            )"""
        
        self.cursor.execute(self.comando_tabela_user)
        self.conn.commit()

        self.comando_tabela_fingerprint = """CREATE TABLE IF NOT EXISTS 
            fingerprint (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value TEXT,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )"""
        self.cursor.execute(self.comando_tabela_fingerprint)

        self.comando_tabela_propriedades = """CREATE TABLE IF NOT EXISTS 
            propriedades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                info TEXT,
                acl INTEGER
            )"""  
        self.cursor.execute(self.comando_tabela_propriedades)
        self.conn.commit()

        self.desconecta_db()
    
    def inserir_user(self, username, password, role):
        self.conecta_db()
        self.cursor.execute("""INSERT INTO users (username, password, role) VALUES (?,?,?)""", (username, password, role))
        print(f'INSERIDO USER {username}')
        self.conn.commit()
        self.desconecta_db()
    
    def select_lista(self):
        self.conecta_db()
        lista_dados = self.cursor.execute("""SELECT id, username, password FROM users ORDER BY username ASC; """)
        return lista_dados
    
    def pesquisar_lista(self, username):
        self.conecta_db()
        username = username + '%'
        lista_dados = self.cursor.execute("""SELECT id, username, password FROM users WHERE username LIKE ?; """, [username])
        return lista_dados
    
    def altenticar_user(self, username, password):
        self.conecta_db()
        self.cursor.execute("""SELECT username, password FROM users WHERE username = ? AND password = ?; """, [username, password])

        if self.cursor.fetchall():
            acesso = False
        else:
            acesso = True
        
        return acesso