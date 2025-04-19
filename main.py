import sqlite3

# Connect to the database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Drop the table if it already exists (ONLY FOR TESTING - remove in final version)
cursor.execute("DROP TABLE IF EXISTS tasks")

# Create the tasks table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tasks (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Priority TEXT,
        Category TEXT,
        Task TEXT,
        Completed BOOLEAN DEFAULT 0,
        Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Due_Date TEXT
    )
""")

# Commit changes and close connection
conn.commit()
conn.close()

print("Table created successfully!")

def connect_db():
    """Connects to the SQLite database and returns connection & cursor."""
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    return conn, cursor