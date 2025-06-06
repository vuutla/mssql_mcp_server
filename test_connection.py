import pymssql

config = {
    "server": "dataeserver.database.windows.net",
    "user": "sqleadmin",
    "password": "dataeserveradmin007$",
    "database": "Employee"
}

try:
    print("Attempting to connect to SQL Server...")
    conn = pymssql.connect(**config)
    cursor = conn.cursor()
    print("Connection successful!")
    
    print("\nTesting query execution...")
    cursor.execute("SELECT * FROM EMP")
    row = cursor.fetchone()
    print(f"Query result: {row}")
    
    cursor.close()
    conn.close()
    print("\nConnection test completed successfully!")
except Exception as e:
    print(f"Error: {str(e)}")
