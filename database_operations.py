import sqlite3

# SQL commands
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL
);
"""
DROP_TABLE = """
DROP TABLE IF EXISTS users;
"""

INSERT_DATA_QUERY = """
INSERT INTO users (name, email, age) VALUES
;
"""

# Define the operations
def connect_to_database():
    # Establish a connection to the SQLite database.
    return sqlite3.connect('dataops.db')

def create_table(conn):
    try:
        # Create the Cursor
        cur = conn.cursor()
        
        # Create table
        cur.execute(CREATE_TABLE_QUERY)

        # Print successful
        print("Table created or already exists.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def drop_table(conn):
    try:
        with conn:
            conn.execute(DROP_TABLE)
        print("Table dropped successfully.")
    except sqlite3.Error as e:
        print(f"Error dropping table: {e}")

def insert_data(conn, data):
    try:
        cur = conn.cursor()
        
        # Insert data
        insert_query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
        cur.executemany(insert_query, (data))
        
        # Commit the changes
        conn.commit()
        
        print("Data inserted successfully.")
        
        # Verify the insertion
        cur.execute("SELECT COUNT(*) FROM users")
        row_count = cur.fetchone()[0]
        print(f"Total rows in the users table: {row_count}")
        
    except sqlite3.IntegrityError as e:
        print(f"Error inserting data: {e}")

def read_data(conn):
    # Read all the data in the table
    try:
        cur = conn.cursor()
        
        read_query = "SELECT * FROM users;"
        rows = cur.execute(read_query)
        for row in rows:
            print(row)
    
    except sqlite3.Error as e:
        print(f"Error reading data: {e}")

def update_data(conn):
    # Update email format
    try:
        cur = conn.cursor()
        
        update_query = """
        UPDATE users 
        SET email = REPLACE(email, '[at]', '@')
        """
        cur.execute(update_query)
        conn.commit()
        
        print(f"Successfully updated {cur.rowcount} email addresses.")
    except sqlite3.Error as e:
        print(f"An error occurred while updating emails: {e}")

def delete_data(conn, age_limit):
    try:
        cur = conn.cursor()
        
        delete_query = "DELETE FROM users WHERE age > ?"
        cur.execute(delete_query, (age_limit))
        conn.commit()
        
        print(f"Deleted users older than {age_limit}.")
    
    except sqlite3.Error as e:
        print(f"Data in the age limit: {e}")

if __name__ == "__main__":
    with connect_to_database() as conn:
    
        create_table(conn)
        
        users = [
            ('Emily Johnson', 'emily.johnson[at]gmail.com', 28),
            ('Michael Rodriguez', 'michael_rodriguez[at]outlook.com', 45),
            ('Sarah Thompson', 'sarah.t@yahoo.com', 33),
            ('David Chen', 'davidchen[at]hotmail.com', 52),
            ('Jessica Martinez', 'jessica.martinez@gmail.com', 24),
            ('Robert Kim', 'robert.kim[at]protonmail.com', 61),
            ('Amanda Wilson', 'amanda_wilson[at]outlook.com', 39),
            ('Christopher Lee', 'chris.lee@gmail.com', 47),
            ('Elizabeth Brown', 'elizabeth.brown[at]yahoo.com', 56),
            ('William Garcia', 'william_garcia@hotmail.com', 31),
            ('Olivia Taylor', 'olivia.taylor[at]gmail.com', 42),
            ('Daniel Martinez', 'daniel.m[at]outlook.com', 35),
            ('Sophia Nguyen', 'sophia_nguyen@yahoo.com', 27),
            ('James Anderson', 'james.anderson[at]protonmail.com', 68),
            ('Emma Wright', 'emma.wright@gmail.com', 22),
            ('Alexander Park', 'alex.park[at]hotmail.com', 50),
            ('Isabella Rodriguez', 'isabella.r@yahoo.com', 36),
            ('Ryan Thompson', 'ryan.thompson[at]gmail.com', 44),
            ('Ava Chen', 'ava.chen@outlook.com', 29),
            ('Matthew Kim', 'matthew.kim[at]protonmail.com', 57),
            ('Mia Johnson', 'mia.johnson@gmail.com', 41),
            ('Ethan Garcia', 'ethan_garcia[at]yahoo.com', 34),
            ('Charlotte Lee', 'charlotte.lee@hotmail.com', 26),
            ('Benjamin Martinez', 'ben.martinez[at]outlook.com', 63),
            ('Abigail Wilson', 'abigail.wilson@gmail.com', 37),
            ('Logan Brown', 'logan.brown[at]yahoo.com', 48),
            ('Harper Rodriguez', 'harper.r@protonmail.com', 25),
            ('Elijah Taylor', 'elijah.taylor[at]gmail.com', 54),
            ('Amelia Nguyen', 'amelia.nguyen@hotmail.com', 32),
            ('Lucas Anderson', 'lucas.anderson[at]outlook.com', 59)
        ]

        insert_data(conn, users)
        print("\nAll Data:")
        read_data(conn)
        
        print("\nUpdating user data...")
        update_data(conn)
        
        print("\nAll Data After Update:")
        read_data(conn)
        
        print("\nDeleting users older than 60...")
        delete_data(conn, 60)
        
        print("\nAll Data After Deletion:")
        read_data(conn)