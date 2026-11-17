import sqlite3

DB_NAME = "crypto_prices.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin_name TEXT,
            symbol TEXT,
            price REAL,
            market_cap REAL,
            volume REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_price(coin_name, symbol, price, market_cap, volume):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO prices
        (coin_name, symbol, price, market_cap, volume)
        VALUES (?, ?, ?, ?, ?)
    """, (coin_name, symbol, price, market_cap, volume))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT coin_name, symbol, price, timestamp
        FROM prices
        ORDER BY id DESC
        LIMIT 20
    """)

    records = cursor.fetchall()
    conn.close()

    return records