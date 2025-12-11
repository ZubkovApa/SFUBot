import sqlite3
from pathlib import Path
from typing import Optional, Dict, Any

DB_PATH = Path(__file__).resolve().parents[1] / 'data' / 'bot.sqlite3'
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER UNIQUE,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        phone TEXT,
        city TEXT,
        level TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def save_user(data: Dict[str, Any]) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO users (tg_id, first_name, last_name, email, phone, city, level)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(tg_id) DO UPDATE SET
        first_name=excluded.first_name,
        last_name=excluded.last_name,
        email=excluded.email,
        phone=excluded.phone,
        city=excluded.city,
        level=excluded.level
    ''', (
        data.get('tg_id'),
        data.get('first_name'),
        data.get('last_name'),
        data.get('email'),
        data.get('phone'),
        data.get('city'),
        data.get('level'),
    ))
    conn.commit()
    cur.execute('SELECT id FROM users WHERE tg_id = ?', (data.get('tg_id'),))
    row = cur.fetchone()
    rowid = row['id'] if row else None
    conn.close()
    return rowid

def user_exists(tg_id: int) -> Optional[sqlite3.Row]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE tg_id = ?', (tg_id,))
    row = cur.fetchone()
    conn.close()
    return row

# Тест
