import sqlite3
from datetime import datetime

class DataBase:
    def __init__(self, DB_NAME="bot.db"):
        self.DB_NAME = DB_NAME
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.DB_NAME)

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS analizler (
                    user_id TEXT PRIMARY KEY,
                    cevaplar TEXT,
                    ozellikler TEXT,
                    meslek TEXT,
                    tarih TEXT
                )
            """)
            conn.commit()

    def kaydet(self, user_id, cevaplar, ozellikler, meslek):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO analizler (user_id, cevaplar, ozellikler, meslek, tarih)
                VALUES (?, ?, ?, ?, ?)
            """, (
                user_id,
                ",".join(cevaplar),
                ",".join(ozellikler),
                meslek,
                datetime.utcnow().isoformat()
            ))
            conn.commit()

    def getir(self, user_id):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM analizler WHERE user_id = ?", (user_id,))
            return cursor.fetchone()
