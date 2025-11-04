try:
    import mysql.connector as mysql_connector
except Exception:
    mysql_connector = None


# Establish the MySQL database connection
def connect_to_mysql(host, user, password, database, port=3306):
    """Attempt to connect to MySQL and return the connection or None.
    Provides helpful messages when connection fails."""
    if mysql_connector is None:
        print("mysql-connector is not installed for this Python interpreter.")
        print("Install it with: python -m pip install mysql-connector-python")
        return None

    try:
        connection = mysql_connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )
        print("Connection established successfully.")
        return connection
    except mysql_connector.Error as err:
        errno = getattr(err, 'errno', None)
        print(f"Error connecting to MySQL: {err}")
        if errno == 2003:
            print("(2003) Can't connect to MySQL server. Is the MySQL server running and reachable on the host/port?")
            print("On Windows try: Open Services (services.msc) and start MySQL or use the MySQL installer to start the server.")
        elif errno == 1045:
            print("(1045) Access denied: check your username and password.")
        else:
            print("Check host, port, username, password and that the MySQL server accepts TCP connections.")
        return None

# Function to fetch data from a table
def fetch_data_from_table(connection, query):
    try:
        cursor = connection.cursor(dictionary=True)  # Using dictionary cursor for easier access to columns by name
    except Exception as e:
        print(f"Error creating cursor: {e}")
        return None

    try:
        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all rows
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        try:
            cursor.close()
        except Exception:
            pass

# Function to sort the data (by a specific column)
def sort_data(data, sort_by_column):
    # Sort the data based on the column name (e.g., 'age')
    return sorted(data, key=lambda x: x[sort_by_column])

# Main function to run the process
def main():
    # MySQL connection parameters
    host = 'localhost'  # Change this to your MySQL host
    user = 'root'  # Change this to your MySQL username
    password = 'yourpassword'  # Change this to your MySQL password
    database = 'yourdatabase'  # Change this to your MySQL database name

    # Connect to MySQL database
    connection = connect_to_mysql(host, user, password, database)
    if connection:
        # Example query to get data from a table (change 'your_table' to your actual table name)
        query = "SELECT * FROM your_table"

        # Fetch the data
        data = fetch_data_from_table(connection, query)

        if data:
            print("Original Data:")
            for row in data:
                print(row)

            # Sort the data by a specific column, e.g., 'age' or 'name'
            sorted_data = sort_data(data, 'your_column_to_sort_by')  # Replace with actual column name

            print("\nSorted Data:")
            for row in sorted_data:
                print(row)
        
        # Close the connection
        connection.close()
    else:
        # Fallback: create mock data so the script can demonstrate sorting and output even when DB is unavailable
        print("\nFalling back to mock data (MySQL connection not available). Showing sample output instead.")
        data = [
            {"id": 3, "name": "Alice", "age": 30},
            {"id": 1, "name": "Bob", "age": 25},
            {"id": 2, "name": "Charlie", "age": 35},
        ]

        print("Original Data:")
        for row in data:
            print(row)

        # Demonstrate sorting by 'age'
        try:
            sorted_data = sort_data(data, 'age')
            print("\nSorted Data (by age):")
            for row in sorted_data:
                print(row)
        except Exception as e:
            print(f"Error sorting mock data: {e}")

# Run the main function
if __name__ == "__main__":
    main()
