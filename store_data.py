import sqlite3

def store_data(processed_data, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY,
            price REAL,
            location TEXT,
            type TEXT,
            bedrooms INTEGER,
            bathrooms INTEGER,
            area REAL,
            land_area REAL
        )
    """)
    for item in processed_data:
        cursor.execute("""
            INSERT INTO properties VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (item['id'], item['price'], item['location'], item['type'], item['bedrooms'], item['bathrooms'], item['area'], item['land_area']))
    conn.commit()
    conn.close()
