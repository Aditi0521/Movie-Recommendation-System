import sqlite3


def view_table(table_name):
    try:
        # Connect to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # Execute the query to retrieve all rows from the specified table
        c.execute(f"SELECT * FROM {table_name};")

        # Fetch all rows from the result of the query
        rows = c.fetchall()

        # Close the database connection
        conn.close()

        # Return the fetched rows
        return rows
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []


# View the contents of the users table
users_data = view_table('users')
print("Users Table:")
for row in users_data:
    print(row)
