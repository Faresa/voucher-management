import sqlite3

# SQLite database file path
DATABASE_FILE = "database/database.db"

# Create the database tables
def initialize_database():
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS vouchers (
                    id INTEGER PRIMARY KEY,
                    code TEXT UNIQUE,
                    redemption_limit INTEGER,
                    expiration_date TEXT,
                    redeemed_times INTEGER DEFAULT 0,
                    active BOOLEAN DEFAULT True
                )
            """)
    except Exception as e:
        print(f"Error initializing database: {e}")

if __name__ == "__main__":
    initialize_database()
