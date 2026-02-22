import sqlite3
from pathlib import Path

DB_PATH = Path("casino_recon.db")

"""
Enable foreign key support in SQLite by default for all connections.
This ensures that any connection to the database will have foreign key constraints enforced.
"""
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

"""
Store money as text to preserve precision and avoid floating-point issues.
When performing calculations, convert the text to a Decimal in Python.
"""
def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_code TEXT UNIQUE NOT NULL,
            game_type TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            amount_wagered TEXT NOT NULL,
            amount_won TEXT NOT NULL,
            net_result TEXT NOT NULL,
            source_file TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (machine_id) REFERENCES machines(id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reconciliation_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_timestamp TEXT NOT NULL,
            total_wagered TEXT NOT NULL,
            total_won TEXT NOT NULL,
            total_net TEXT NOT NULL,
            discrepancy_flag INTEGER NOT NULL,
            notes TEXT
        );
    """)

    conn.commit()
    conn.close()