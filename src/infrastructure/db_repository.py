import pymysql

class MySQLRepository:
    def __init__(self):
        # Configuración base (ajusta el host si usas host.docker.internal)
        self.host = '127.0.0.1' 
        self.port = 3307
        self.user = 'root'
        self.password = ''
        self.db_name = 'examen_db'
        self._preparar_db()

    def _preparar_db(self):
        # 1. Conectar al servidor (sin elegir DB aún)
        conn = pymysql.connect(
            host=self.host, port=self.port, 
            user=self.user, password=self.password
        )
        try:
            with conn.cursor() as cur:
                # 2. Crear la base de datos si no existe
                cur.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
                conn.select_db(self.db_name)
                
                # 3. Crear la tabla si no existe
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS inscripciones (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        idioma VARCHAR(50),
                        nivel VARCHAR(50),
                        horario VARCHAR(50)
                    )
                """)
            conn.commit()
        finally:
            conn.close()

    def save(self, ins):
        conn = pymysql.connect(
            host=self.host, port=self.port, 
            user=self.user, password=self.password, db=self.db_name
        )
        try:
            with conn.cursor() as cur:
                sql = "INSERT INTO inscripciones (idioma, nivel, horario) VALUES (%s, %s, %s)"
                cur.execute(sql, (ins.idioma, ins.nivel, ins.horario))
            conn.commit()
        finally:
            conn.close()

    def get_all(self):
        conn = pymysql.connect(
            host=self.host, port=self.port, 
            user=self.user, password=self.password, db=self.db_name
        )
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cur:
                cur.execute("SELECT * FROM inscripciones")
                return cur.fetchall()
        finally:
            conn.close()